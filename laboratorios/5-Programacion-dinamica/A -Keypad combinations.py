from collections import defaultdict
from sys import stdin
from itertools import combinations

def is_valid(i, j):
        if 0 <= i <= 3 and 0 <= j <= 2 and keys[i][j] != '*' and keys[i][j] != '#':
            return True
keys = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     ['*', 0, '#'],
            ]
row = [0, -1, 0, 1]
col = [-1, 0, 1, 0]


def fill_keypad_map():
    
        # TODO Complete (is movement valid in the keypad?)
    keypad_map = defaultdict(list)
    for i in range(4):
        for j in range(3):
            for k in range(4):
                r = i + row[k]
                c = j + col[k]
                if is_valid(i, j) and is_valid(r, c):
                    keypad_map[keys[i][j]].append(keys[r][c])
    return keypad_map

def keypad(n):
 keypad = fill_keypad_map()
 print(keypad)
 combinaciones = []
 for i3 in keys:
     for i in i3:
         if i != "*" and i != "#":
             print(i,keypad[i])
             pc = list(combinations(keypad[i]+[i],n))
             combinaciones+=pc
 return combinaciones
 
 


def main():
    n = int(stdin.readline().strip())
    resultados = {}
    if n in resultados.keys():
        print(resultados[n])
    else:
        count = keypad(n)
        print(count)
        resultados[n] = len(count)
        print(f'Combinations: {resultados[n]}')




main()
