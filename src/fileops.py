import sys

# text = sys.stdin.read()
# words = text.split()
# wordscount = len(words)
# print("wordscount:",wordscount)

with open("exam.txt") as text:
    while True:
        line = text.readline()
        if not line: break
        print("line:", line)


class bird(object):
    def __init__(self):
        super(bird, self).__init__()


# 1-100质数
a = [x for x in range(1, 101) if x % 2 != 0]
print(a)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%d\t' % (j, i, j * i), end='')
    print('\n')
