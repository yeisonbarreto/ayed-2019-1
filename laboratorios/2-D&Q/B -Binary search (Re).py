def bbin(a,num,index):
    if len(a) == 1:
        if a[0] == num:
            return index
        else:
            return -1
    else:
        mid = len(a)//2
        if a[mid] > num:
            return bbin(a[:mid],num,index)
        else:
            index += mid
            return bbin(a[mid:],num,index)

num = 7
a = [1,2,3,4,5,6,7]
index = 0
