from Crypto.Util import number as pr
import random
import datetime


def legendre_symbol(s1, s2):
    ls = pow(s1, int((s2 - 1) // 2), s2)
    return -1 if ls == (s2 - 1) else ls


# def get_y_in_curve(x_point, a_given, b_given, p):
#     y2 = (x_point ** 3 + a_given * x_point + b_given) % p
#     y_int = modular_sqrt(y2, p)
#     if y_int and ((y_int * y_int) % p) == (y2 % p):
#         return y_int
#     return None


def generate_parameters(p):
    a_given = random.randrange(0, p - 1)
    b_given = random.randrange(0, p - 1)
    val = (4 * (a_given ** 3) + 27 * (b_given ** 2)) % p
    while val == 0:
        a_given = random.randrange(0, p - 1)
        b_given = random.randrange(0, p - 1)
        val = (4 * (a_given ** 3) + 27 * (b_given ** 2)) % p
    print(f'a={a_given} b={b_given}')
    return a_given, b_given


def gen_coords(p, a_given, b_given):
    while True:
        x_point = random.randint(1, p - 1)
        y2 = (x_point ** 3 + a_given * x_point + b_given) % prime

        if legendre_symbol(y2, prime) == 1:
            y_point = pow(y2, (p+1) // 4, p)
            return x_point, y_point


def point_addition(P, Q, coeff_a, p):
    if P[0] == Q[0] and P[1] == Q[1]:
        s = (3 * P[0] ** 2 + coeff_a) * pow(2 * P[1], -1, p)
    else:
        s = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p)
    x_point = (s ** 2 - P[0] - Q[0]) % p
    y_point = (s * (P[0] - x_point) - P[1]) % p
    return x_point, y_point


def point_multiplication(mul, P, p, coeff_a):
    val = bin(mul)[3:]
    Q = P
    for bit in val:
        Q = point_addition(Q, Q, coeff_a, p)
        if bit == '1':
            Q = point_addition(P, Q, coeff_a, p)
    return Q


def find_mod(Q, p):
    x_coo = Q[0] % p
    y_coo = Q[1] % p
    return x_coo, y_coo


def check_val(val1, val2):
    if val1 == val2:
        return True
    return False


f = open("output.txt", "w")
f.write("\tComputation time for (in msec)\n")
f.write("  k\tA\tB\tShared key R\n")
for i in 128, 196, 256:
    # i=256
    prime = pr.getPrime(i)
    print(f'prime- {prime}')
    trial = 0
    total_a = 0
    total_b = 0
    total_r = 0
    limit = prime + 1 - 2 * prime ** 0.5
    a, b = generate_parameters(prime)
    # a=2
    # b=2
    while trial < 5:
        # x, y = generate_coordinates(prime, a, b)
        x, y = gen_coords(prime, a, b)

        G = [x, y]
        ka = random.getrandbits(i)
        while ka >= limit or len(str(bin(ka)[2:])) < i:
            ka = random.getrandbits(i)
        # print(f'ka= {ka} len= {len(str(bin(ka)[2:]))}')
        kb = random.getrandbits(i)
        while kb >= limit or len(str(bin(kb)[2:])) < i:
            kb = random.getrandbits(i)
        # print(f'kb= {kb} len= {len(str(bin(kb)[2:]))}')

        start_a = datetime.datetime.now()
        A = find_mod(point_multiplication(ka, G, prime, a), prime)
        end_a = datetime.datetime.now()
        time_diff_a = (end_a - start_a)
        execution_time_a = time_diff_a.total_seconds() * 1000

        start_b = datetime.datetime.now()
        B = find_mod(point_multiplication(kb, G, prime, a), prime)
        end_b = datetime.datetime.now()
        time_diff_b = (end_b - start_b)
        execution_time_b = time_diff_b.total_seconds() * 1000

        R1 = point_multiplication(ka, B, prime, a)
        R2 = point_multiplication(kb, A, prime, a)
        R1p = R1[0] % prime
        R2p = R2[0] % prime
        # if R1p == R2p:
        #     print("ok")

        start_r = datetime.datetime.now()
        R = find_mod(point_multiplication(ka * kb, G, prime, a), prime)
        end_r = datetime.datetime.now()
        time_diff_r = (end_r - start_r)
        execution_time_r = time_diff_r.total_seconds() * 1000
        trial += 1
        total_a += execution_time_a
        total_b += execution_time_b
        total_r += execution_time_r

    avg_a = total_a / 5
    avg_b = total_b / 5
    avg_r = total_r / 5
    avg_a = "{:.5f}".format(avg_a)
    avg_b = "{:.5f}".format(avg_b)
    avg_r = "{:.5f}".format(avg_r)
    print(f'average times: {avg_a} {avg_b} {avg_r}')
    print("")
    f.write(str(i)+"\t"+str(avg_a)+"\t"+str(avg_b)+"\t"+str(avg_r)+"\n")
    f.flush()
f.close()
