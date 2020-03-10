import socket
import pickle
import struct
import argparse
from msg_utils import send_msg, recv_msg


parser = argparse.ArgumentParser()
parser.add_argument('-P', '--PORT', type=int, default=8888)
parser.add_argument('-H', '--HOST', type=str, default='127.0.0.1')

args = parser.parse_args()


HOST, PORT = args.HOST, args.PORT


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    msg = recv_msg(s)
    game = pickle.loads(msg)

    msg = recv_msg(s)
    print(pickle.loads(msg))
    ai = input()

    msg = recv_msg(s)
    print(pickle.loads(msg))
    player1 = input().upper()

    send_msg(s, pickle.dumps(ai))
    send_msg(s, pickle.dumps(player1))

    if player1.upper() == 'O':
        position = recv_msg(s)
        game.move(pickle.loads(position), 'X')
        player2 = 'X'       
    else:
        player2 = 'O'

    print(game)    
    while not game.is_over():
        position_player = game.turn(player1)
        send_msg(s, pickle.dumps(position_player))
        print(game)

        if game.is_over():
            break
        
        position_enemy = pickle.loads(recv_msg(s))
        game.move(position_enemy, player2)
        print(game)

    print(game.result())


