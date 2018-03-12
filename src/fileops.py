import sys
# text = sys.stdin.read()
# words = text.split()
# wordscount = len(words)
# print("wordscount:",wordscount)

with open("exam.txt") as text:
    while True:
        line = text.readline()
        if not line:break
        print("line:",line)

class bird(object):
    def __init__(self):
        super(bird, self).__init__()