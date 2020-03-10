import socket
import struct


def send_msg(sock: socket.socket, msg: bytearray) -> None:
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


def recv_msg(sock: socket.socket) -> bytearray:
    tamanho = recvall(sock, 4)
    if not tamanho:
        return None
    tamanho = struct.unpack('>I', tamanho)[0]
   
    return recvall(sock, tamanho)


def recvall(sock: socket.socket, n: int) -> bytearray:
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n-len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
