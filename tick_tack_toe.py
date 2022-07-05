import random


class Game:
    def __init__(self):
        self.board = self.create_board()
        self.winner = None

    def __str__(self):
        rules = '''Игра крестики нолики наоборот:\n
         Проигрывает игрок, у которого собралась последовательность
         из 5 символов по вертикали, горизонтали или диагонали.
         Игровое поле 10х10, каждая клетка содержит номер.
         Для того чтобы совершить ход введите номер незанятой клетки.
         Вы играете за Х.
        '''
        return rules

    def show_board(self):
        for item in self.board:
            for cell in item:
                if len(str(cell)) < 2:
                    cell = f' {cell}'
                print(cell, end=' ')
            print('')

    def refresh_table(self, move: int, side: str) -> list:
        for item in self.board:
            if move in item:
                item[item.index(move)] = side
        self.winner = self.who_win(self.board)
        return self.board

    @staticmethod
    def who_win(board):
        loser = None
        for y in range(6):
            for x in range(6):
                ch = board[y][x]
                win = True
                for i in range(1, 5):
                    if (board[y + i][x + i] != ch) and (board[y - i][x + i] != ch) :
                        win = False
                        break
                if win:
                    if ch == 'X':
                        loser = 'X'
                    elif ch == 'O':
                        loser = 'O'

        for y in range(4, 10):
            for x in range(6):
                ch = board[y][x]
                win = True
                for i in range(1, 5):
                    if board[y - i][x] != ch:
                        win = False
                        break
                if win:
                    if ch == 'X':
                        loser = 'X'
                    elif ch == 'O':
                        loser = 'O'

        for x in range(4, 10):
            for y in range(6):
                ch = board[y][x]
                win = True
                for i in range(1, 5):
                    if board[y][x - i] != ch:
                        win = False
                        break
                if win:
                    if ch == 'X':
                        loser = 'X'
                    elif ch == 'O':
                        loser = 'O'

        return loser

    def computer_move(self) -> int:
        while True:
            move = random.randint(1, 100)
            if self.cell_is_occupied(self.board, move):
                continue
            else:
                print(f'Ход компьютера - {move}')
                return move

    def player_move(self) -> int:
        while True:
            print('Ваш ход:')
            try:
                move = int(input('> '))
                if self.cell_is_occupied(self.board, move):
                    print('Ячейка должна быть не занята.')
                    continue
                return move
            except:
                print('Ввод должен содержать цифры от 1 до 100.')

    @staticmethod
    def create_board() -> list:
        cell_list = []
        count = 0
        for i in range(10):
            cell_list.append([0] * int(10))
            for j in range(10):
                count += 1
                cell_list[i][j] = count
        return cell_list

    @staticmethod
    def cell_is_occupied(board, cell: int) -> bool:
        if cell <= 10:
            occupied = cell not in board[0]
        else:
            occupied = cell not in board[(cell - 1) // 10]
        return occupied


if __name__ == '__main__':
    game = Game()
    print(game)
    game.show_board()
    while True:
        player_move = game.player_move()
        game.refresh_table(player_move, 'X')
        if game.winner:
            print('Победил компьютер!')
            exit()

        computer_move = game.computer_move()
        game.refresh_table(computer_move, 'O')
        game.show_board()
        if game.winner:
            print('Победил игрок!')
            exit()
