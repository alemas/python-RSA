import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('bits', metavar='bits', type=int,
                    help='The number of bits to be used')
args = parser.parse_args()

# Pequeno Teorema de Fermat
def is_prime(p):
    if (p < 2):
        return False

    for _ in range(0, 2):
        a = randint(2, p-2)
        if (pow(a, p-1, p) != 1):
            return False
        return True

def generate_prime(bits):
    pb_key = 0
    pv_key = 0

    while (not is_prime(pb_key)):                
        pb_key = randint(2**(bits-1), 2**bits)

    while (not is_prime(pv_key) or pv_key == pb_key):
        pv_key = randint(2**(bits-1), 2**bits)

    print("Public key:\n" + str(pb_key) + "\n\nPrivate key:\n" + str(pv_key))

generate_prime(args.bits)