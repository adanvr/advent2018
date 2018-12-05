with open('data/input05.txt') as f:
    data = f.read().replace('\n','')
#My implementation

def chem_rdx_og(data):
    redox_done = True
    while redox_done:
        redox_done = False
        for i in range(1, len(data)):
            chem1 = data[i-1]
            chem2 = data[i]
            #print(list(zip(chem1,chem2)))
            if chem1.lower() == chem2.lower() and chem1 != chem2:
                data = data[:i-1] + data[i+1:]
                print(list(zip(data[:i-1],data[i+1:])))
                redox_done = True
                break
    return data
    
# Much faster implementation
def chem_reduction(data):
    chemicals = list(data)
    idxs = [i for i in range(len(chemicals))]
    removed = set()

    def next_index(prev_index):
        for idx in range(prev_index + 1, len(chemicals)):
            if idx not in removed:
                return idx
        return len(chemicals)

    reduction_done = True
    while reduction_done:
        reduction_done = False

        lo = next_index(-1)
        hi = next_index(lo)

        while hi < len(chemicals):
            chem1 = chemicals[lo]
            chem2 = chemicals[hi]
            if chem1.lower() == chem2.lower() and chem1 != chem2:
                removed.add(lo)
                removed.add(hi)
                lo = next_index(hi)
                hi = next_index(lo)
                reduction_done = True
            else:
                lo = hi
                hi = next_index(lo)
    return "".join(chem for i, chem in enumerate(chemicals) if i not in removed)

assert chem_reduction('aA') == '' 
assert chem_reduction('abBA') == ''
assert chem_reduction('abAB') == 'abAB'
assert chem_reduction('aabAAB') == 'aabAAB'


test_str = 'dabAcCaCBAcCcaDA'
assert chem_reduction(test_str) == 'dabCBAcaDA'

print(len(chem_reduction(data)))

chars = {c.lower() for c in data}

best_poly = {}

for c in chars:
    print(c)
    polymer_no_c = data.replace(c, "").replace(c.upper(), "")
    best_poly[c] = len(chem_reduction(polymer_no_c))

print(best_poly)
best_key = min(best_poly, key=lambda c: best_poly[c])
print(best_key)