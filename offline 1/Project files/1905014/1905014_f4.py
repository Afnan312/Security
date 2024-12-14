import socket
import importlib
import random
from time import sleep
import pickle
import numpy as np

functions = importlib.import_module("1905014_f5")

find_mod = getattr(functions, 'find_mod')
point_multiplication = getattr(functions, 'point_multiplication')
key_expansion = getattr(functions, 'key_expansion')
convert_key = getattr(functions, 'convert_key')
decrypt = getattr(functions, 'decrypt')

rc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
rc.connect((host, port))
print("Connected to Alice")

prime = rc.recv(1024)
a = rc.recv(1024)
b = rc.recv(1024)
Gx = rc.recv(1024)
Gy = rc.recv(1024)
R1 = rc.recv(1024)

prime_ = pickle.loads(prime)

a_ = pickle.loads(a)

b_ = pickle.loads(b)

Gx_ = pickle.loads(Gx)

Gy_ = pickle.loads(Gy)

R1_ = pickle.loads(R1)

G = [Gx_, Gy_]

kb = random.getrandbits(128)
limit = prime_ + 1 - 2 * prime_ ** 0.5
while kb >= limit or len(str(bin(kb)[2:])) < 128:
    kb = random.getrandbits(128)

A = find_mod(point_multiplication(kb, G, prime_, a_), prime_)

A_s = pickle.dumps(A)

rc.send(A_s)
sleep(0.2)

shared = point_multiplication(kb, R1_, prime_, a_)
shared_key = shared[0] % prime_

shared_key = convert_key(shared_key)

message = rc.recv(1024).decode()
if message == "Ready":
    print("Alice is ready to send the ciphertext")
    all_keys = key_expansion(shared_key)
    rc.send('Ready'.encode())

    iv = rc.recv(1024).decode()

    encrypted = rc.recv(1024)
    received_data = pickle.loads(encrypted)

    decrypted = decrypt(received_data, iv, all_keys)

    ascii_decrypt = ''
    for e_block in decrypted:
        e_block = np.transpose(e_block)
        for row in e_block:
            for char in row:
                if char == '00':
                    continue
                ascii_decrypt += (chr(int(char, 16)))
    print("Deciphered Text:")
    print("In ASCII:")
    print(ascii_decrypt)
    print("")
rc.close()
