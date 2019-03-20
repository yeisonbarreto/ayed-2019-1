from sys import stdin
def spikes(runway,speed,index):
    if index >= len(runway) or index < 0 or speed < 0 or not runway[index]:
        return False

    if speed == 0:
        return True

    for i in [speed,speed - 1,speed + 1]:
        if spikes(runway,i,index + i):
            return True
        
    return False
        
if __name__ == '__main__':
    runway = [False, True, True, False, False, True, True, True, True, False, True]
    speed = 5
    index = 1
    print(spikes(runway,speed,index))



