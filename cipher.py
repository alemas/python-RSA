import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pb_key', metavar='public-key', type=int, help='Key to be used when ciphering the message')
parser.add_argument('msg', metavar='message', type=int, help='Message to be ciphered')
args = parser.parse_args()

def cipher():
    pb_key = args.pb_key
    msg = args.msg
    

cipher()



