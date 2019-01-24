def bbin(a,num,index):
    global n 
    if len(a) == 1:
        return 0
    else:
        for i in a:
            if i == num:
                index.append(n)
            n+=1
            if n == len(a) and index == []:
                return -1
        return index
            
def main():
    global n
    n=0
    num = 6
    a = [1,2,3,4,5,5,5,5,5,5,6,6,6,6,6,7,7]
    index = []
    print(bbin(a,num,index))

main()
