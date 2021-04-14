# Fuzzer
Simple fuzzer for stack based buffer overflows - written for OSCP prep
usage: fuzzer.py [-h] target ip target port command

Simple fuzzer for stack based buffer overflows.

positional arguments:
  target ip    Target host ip running the vulnerable app
  target port  Target port
  command      Command of the vulnerable app. Dont forget space if needed. "TRUN "

optional arguments:
  -h, --help   show this help message and exit

example: python3 fuzzer.py 10.10.111.82 1337 "OVERFLOW1 "


![alt text][logo]

[logo]: https://github.com/fluxcapa/Fuzzer/blob/main/fuzzer.gif "fuzzer.py"
