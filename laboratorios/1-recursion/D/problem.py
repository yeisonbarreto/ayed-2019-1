import json


# TODO Complete!
def compute_ways(n):
    return 0


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            actual = compute_ways(n)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | expected: {expected}, actual: {actual}'
        print('OK!')
