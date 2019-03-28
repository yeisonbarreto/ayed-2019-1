from sys import stdin
def IsReverse(text,n):
    new = []
    for i in range(n):
        new.append(text.pop())
    p = ''.join(new)
    return p
def main():
    text = [str(i) for i in stdin.readline().strip()]
    print(IsReverse(text,len(text)))
main()
