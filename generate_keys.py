import argparse
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('bits', metavar='bits', type=int,
                    help='The number of bits to be used')
args = parser.parse_args()

def gcd(a, b):
    if (b == 0):
       return a 
    else:
       return gcd(b, a % b)

# Pequeno Teorema de Fermat
def is_prime(p):
    if (p < 2):
        return False

    # for _ in range(0, 2):
        # a = randint(2, p-2)
    a = 2
    if (pow(a, p-1, p) != 1):
        return False
    return True

def generate_prime(bits):
    p = 0
    q = 0

    while (not is_prime(p)):                
        p = randint(2**(bits-1), 2**bits)

    while (not is_prime(q) or q == p):
        q = randint(2**(bits-1), 2**bits)

    modulo = p * q


    print("Public key:\n" + str(p) + "\n\nPrivate key:\n" + str(q))

generate_prime(args.bits)