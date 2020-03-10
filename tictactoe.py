import os
from MinMax import MinMax

class TicTacToe(object):

    def __init__(self) -> None:
        self.board = [str(x) for x in range(1,10)]
        

    def __eq__(self, other):
        return self.__class__ == other.__class__


    def __str__(self) -> str:
        string = ''
        for i in range(0,7, 3):
            for j in range(3):
                string += f'{self.board[i+j]} '
            string += '\n'
        return string
        

    def _check_victory(self) -> str:
        for x in ('X', 'O'):
            for i in range(3):
                #checando as linhas horizontais
                if self.board[3*i] == self.board[3*i + 1] == self.board[3*i + 2] == x:
                    return x

                #checando as linhas verticais
                if self.board[i] == self.board[i + 3] == self.board[i + 6] == x:
                    return x

            #checando as diagonais
            if self.board[0] == self.board[4] == self.board[8] == x:
                return x
            if self.board[2] == self.board[4] == self.board[6] == x:
                return x

        return None
    

    def is_over(self) -> str:
        result = self._check_victory()
        
        if  result is not None:
            return result

        for x in self.board:
            if x.isdigit():
                return None
        return 'Empate'


    def result(self) -> str:
        result = self.is_over()
        return result


    def move(self, position: int, player: str) -> None:
        self.board[position] = player


    def get_moves(self) -> list:
        moves = [int(x)-1 for x in self.board if x.isdigit()]
        return moves
        
    
    def turn(self, player) -> int:

        avaliable_positions = self.get_moves()

        while True:
            try:
                position = int(input("Insira a posição desejada: "))-1
                if position not in avaliable_positions:
                    raise ValueError

                if self.board[position].isdigit():
                    self.board[position] = player
                    break

            except TypeError:
                print('Por insira um digito de 1 a 9\n')
            except  ValueError:
                print('Posição inválida\n')
    
        return position
    

if __name__ == '__main__':
    turn_player_x = False
    game = TicTacToe()
    computer = MinMax(game, ('O', 'X'))
    computer2 = MinMax(game, ('X', 'O'))

    while not game.is_over():
        print(game)
		
        if(turn_player_x):
            best_move = computer2.get_decision(game, computer2.players)
            game.move(best_move, 'x')
        else:
            best_move = computer.get_decision(game, computer.players)
            game.move(best_move, 'O')
            
        turn_player_x = not turn_player_x
        
    print(game.result())
