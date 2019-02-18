#sys2.py
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

# upper를 이용하여 소문자를 대문자로 바꿈
