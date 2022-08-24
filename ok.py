import random


class setup:
    

    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self, board):
        

        for i in range(3):
            display = ' | '.join(board[i * 3:i * 3 + 3])

            if i in range(2):
                sep = f"\n{'- ' * 5}\n"

            else:
                sep = '\n'

            print(display, end=sep)

    def get_turn(self):
        
        option = True if input('Do you want to go first (y/n)? ').lower() == 'y' else False

        if option:
            return ('X', 'O')

        return ('O', 'X')


class playing(setup):
    
    def __init__(self):
        super().__init__()
        self.human, self.bot = setup().get_turn()
        self.winner_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]

    def get_possible_moves(self):
        return [self.board.index(place) for place in self.board if place in [str(i) for i in range(1, 10)]]

    def human_move(self):
        try:
            place = int(input('\nWhere do you want to place?')) - 1

            if place in self.get_possible_moves() and place > -1:
                self.board[place] = self.human

            else:
                print('Invalid Move')
                print(self.display_board(self.board))
                self.human_move()

        except:
            print('Invalid Move')
            print(self.display_board(self.board))
            self.human_move()

    def is_winner(self, board):
        if not self.get_possible_moves():
            return 'Tie'

        for winner in self.winner_combo:
            if board[winner[0]] == board[winner[1]] == board[winner[2]] == board[winner[0]]:
                return board[winner[0]]

    def bot_move(self):
        possible_moves = self.get_possible_moves()

        if possible_moves:
            for move in possible_moves:  # Checking if bot can win
                self.board[move] = self.bot

                if self.is_winner(self.board):
                    self.board[move] = self.bot
                    return

                self.board[move] = str(move + 1)

            for move in possible_moves:  # Checking if player can win
                self.board[move] = self.human

                if self.is_winner(self.board):
                    self.board[move] = self.bot
                    return

                self.board[move] = str(move + 1)

            self.board[random.choice(possible_moves)] = self.bot

    def main(self):
        print(f'\nYou: {self.human}\nBot: {self.bot}\n')

        if self.bot == 'X':
            self.bot_move()

        self.display_board(self.board)

        while not self.is_winner(self.board):
            self.human_move()
            self.bot_move()
            self.display_board(self.board)

            if self.is_winner(self.board) == self.human:
                print('\nHuman Won')
                

            
            elif self.is_winner(self.board) == self.bot:
                print('\nBot Won')


            else:
                
                print('\nHuman and Bot got tied')


playing().main()