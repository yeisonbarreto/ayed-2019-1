from sys import stdin
        
def maxWeight (array, w_1, w_2):
    W1 = 0
    W2 = 0
    for i in range(len(array)):
        
        if w_1 >= array [i]:
            W1 = array [i] + w_1 - array [i]
            
        if w_2 >= array [i]:
            W2 = array [i] + w_2 - array [i]
            
    return W1 + W2
        
def main():
    
    array = eval(stdin.readline().strip())
    W1 = int(stdin.readline().strip())
    W2 = int(stdin.readline().strip())
    print(maxWeight (array, W1, W2))
    
main()
