import sys

def push(k):
    stack.append(k)

def size():
    return len(stack)

def empty():
    if size() == 0:
        return 1
    return 0
    
def pop():
    if empty() == 1:
        return -1
    return stack.pop()

def top():
    if empty() == 1:
        return -1
    return stack[-1]    

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    c = sys.stdin.readline().split()

    if c[0] == "push":
        push(int(c[1]))
    elif c[0] == "size":
        print(size())
    elif c[0] == "empty":
        print(empty())
    elif c[0] == "top":
        print(top())
    elif c[0] == "pop":
        print(pop())