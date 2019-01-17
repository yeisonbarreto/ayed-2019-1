import json


# TODO Complete!!
def reverse(list):
    if len(list)==1:
        return list
    else:
        return list[-1]+reverse(list[:-1])


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
