import socket
import pickle
import argparse
from tictactoe import TicTacToe
from minmax import MinMax
import struct
from msg_utils import send_msg, recv_msg


def setup(socket, game):
    send_msg(socket, pickle.dumps(game))
    send_msg(socket, pickle.dumps('AI or Player (A/P)?'))
    send_msg(socket, pickle.dumps('Choose X or O'))

    ai = pickle.loads(recv_msg(socket))
    player = pickle.loads(recv_msg(socket))
    return (ai, player)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--PORT', type=int, default=8888)
    args = parser.parse_args()
    
    HOST = socket.gethostbyname('0.0.0.0')
    PORT = args.PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print(HOST, PORT)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connecting address: ", addr)
            game = TicTacToe()
            ai, player2 = setup(conn, game)
            pc = None
            print(player2)

            if player2.upper() == 'X':
                player1 = 'O'
                position = pickle.loads(recv_msg(conn))
            
                game.move(position, 'X')
                print(game)
            else:
                player1 = 'X'

            if ai.upper() == 'A':
                pc = MinMax(game, (player1, player2))

            while not game.is_over():
                print(game)
                if pc is not None:
                    position_player = pc.get_decision(game, pc.players)
                    game.move(position_player, player1)
                else:
                    position_player = game.turn(player1)
                    
                    
                send_msg(conn, pickle.dumps(position_player))
                print(game)
                if game.is_over():
                    break
                
                position_enemy = pickle.loads(recv_msg(conn))
                game.move(position_enemy, player2)
                
            print(game.result())
                
                
