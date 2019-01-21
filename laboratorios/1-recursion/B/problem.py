import json


# TODO Complete!
def arrange(array, orden):
    if len(array) == 0:
        return orden
    else:
        if array[0]%2 == 0:
            orden.insert(len(orden)//2,array[0])
        else:
            orden.append(array[0])
        return arrange(array[1:],orden)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers, [])
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
