import json


# TODO Complete!
def hanoi(n, origen, auxiliar, destino):
    if n > 0: 
        hanoi(n-1, origen, destino, auxiliar)
        print ("Se mueve de torre", origen, 'a torre', destino)
        hanoi(n-1, auxiliar, origen, destino)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            origen='A'
            auxiliar='B'
            destino='C'
            hanoi(n, origen, auxiliar, destino)
        print('OK!')
