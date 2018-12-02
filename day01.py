with open('data/input01.txt') as f:
    data = [int(line) for line in f]


print(sum(data))


def all_frq(data):
    frequency = 0

    while True:
        for datum in data:
            yield frequency
            frequency += datum


def first_repeat_frequency(data):
    seen = set()

    for frequency in all_frq(data):
        if frequency in seen:
            return frequency
        else:
            seen.add(frequency)

assert first_repeat_frequency([1, -1]) == 0
assert first_repeat_frequency([3, 3, 4, -2, -4]) == 10
assert first_repeat_frequency([-6, 3, 8, 5, -6]) == 5
assert first_repeat_frequency([7, 7, -2, -7, -4]) == 14

print(first_repeat_frequency(data))