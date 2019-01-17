import json


# TODO Complete!
vowels = ['a','e','i','o','u','A','E','I','O','U']
def has_more_vowels(text):
    text = list(text)
    cont = 0
    for i in range(len(text)):
        for j in range(len(vowels)):
            if text[i] == vowels[j]:
                cont += 1
    rest = len(text) - cont
    if cont <= rest:
        return False
    else:
        return True


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
