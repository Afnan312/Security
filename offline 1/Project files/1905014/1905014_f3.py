import socket
import importlib
import random
from time import sleep
import pickle

functions = importlib.import_module("1905014_f5")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)

client, addr = s.accept()
print("Connected to Bob")

get_val = getattr(functions, 'get_params')

encrypt = getattr(functions, 'encrypt')
get_iv = getattr(functions, 'get_iv')
key_expansion = getattr(functions, 'key_expansion')
convert_key = getattr(functions, 'convert_key')

find_mod = getattr(functions, 'find_mod')
point_multiplication = getattr(functions, 'point_multiplication')

prime, x, y, a, b = get_val()
G = [x, y]

ka = random.getrandbits(128)
limit = prime + 1 - 2 * prime ** 0.5
while ka >= limit or len(str(bin(ka)[2:])) < 128:
    ka = random.getrandbits(128)

A = find_mod(point_multiplication(ka, G, prime, a), prime)


prime_b = pickle.dumps(prime)
a_b = pickle.dumps(a)
b_b = pickle.dumps(b)

x_b = pickle.dumps(x)
y_b = pickle.dumps(y)

A_s = pickle.dumps(A)

client.send(prime_b)
sleep(0.2)
client.send(a_b)
sleep(0.2)
client.send(b_b)
sleep(0.2)
client.send(x_b)
sleep(0.2)
client.send(y_b)
sleep(0.2)
client.send(A_s)
sleep(0.2)

R1_s = client.recv(1024)

R = pickle.loads(R1_s)

shared = point_multiplication(ka, R, prime, a)
shared_key = shared[0] % prime

shared_key = convert_key(shared_key)

client.send('Ready'.encode())
sleep(0.2)

message = client.recv(1024).decode()
if message == "Ready":
    print("Bob is ready to receive the ciphertext")
    all_keys = key_expansion(shared_key)
    iv = get_iv()
    client.send(iv.encode())
    sleep(0.1)

    print("Plaintext:")
    plaintext = input("In ASCII:")
    if len(plaintext) % 16 != 0:
        padding = 16 - len(plaintext) % 16
        plaintext = plaintext + " " * padding

    text_blocks = []
    for i in range(0, len(plaintext), 16):
        text_blocks.append(plaintext[i:i + 16])

    encrypted = encrypt(text_blocks, iv, all_keys)

    encrypt_s = pickle.dumps(encrypted)

    client.send(encrypt_s)
    sleep(1)
