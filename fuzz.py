#!/usr/bin/python
# Quick Fuzzer with arguments

import sys, socket, argparse
from time import sleep

parser=argparse.ArgumentParser(
        description='''Simple fuzzer for stack based buffer overflows.''',
        epilog='''example: python3 fuzz.py 10.10.111.82 1337 "OVERFLOW1 "''')
parser.add_argument('target ip', help='Target host ip running the vulnerable app')
parser.add_argument('target port', help='Target port')
parser.add_argument('command', help='Command of the vulnerable app. Dont forget space if needed. "TRUN "')
args = parser.parse_args()

buffer = "A" * 100
target = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]

print("target: " + target + " port: " + str(port) + " command: " + command)
while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target,port))
            print("Sending " + command + " plus " + str(len(buffer)) + " A's")
            s.send((command.encode() + buffer.encode()))
            s.close
            sleep(1)
            buffer = buffer + "A" * 100
            print(s.recv(4096).decode())
        except:
            print("Fuzzing crashed or reached timeout (3sec) at %s bytes" % str(len(buffer) - 100))
            sys.exit()
