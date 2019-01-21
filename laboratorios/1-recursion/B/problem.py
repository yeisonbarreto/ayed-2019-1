import json


# TODO Complete!
def arrange(array, par, impar):
    if len(array) == 0:
        return par+impar
    else:
        if array[0]%2 == 0:
            par.append(array[0])
        else:
            impar.append(array[0])
        return arrange(array[1:], par, impar)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers, [] ,[])
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
