from collections import Counter

with open('data/input02.txt') as f:
    data = [list(line.strip('\n')) for line in f]

def count_letters(word_str):
    '''
    Function that will create a dictionary of count of letters in box_id
    '''
    return dict(Counter(word_str))

assert count_letters('aabbcc') == {'a':2, 'b':2, 'c':2}
assert count_letters('ddff') == {'d':2, 'f':2}

def count_doubles(data_dict):
    if len({k: v for k, v in data_dict.items() if v == 2}) > 0:
        return 1
    else: 
        return 0

assert count_doubles({'a':2, 'b':2, 'c':2}) == 1

def count_triples(data_dict):
    if len({k: v for k, v in data_dict.items() if v == 3}) > 0:
        return 1
    else: 
        return 0

assert count_triples({'a':2, 'b':2, 'c':2}) == 0

data_dict = [count_letters(datum) for datum in data]


def check_sum(data_dict):
    doubles = sum([count_doubles(datum) for datum in data_dict])
    triples = sum([count_triples(datum) for datum in data_dict])
    print(doubles * triples)

check_sum(data_dict)

