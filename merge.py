from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement
from pprint import pprint
from copy import deepcopy
import json


N = 5*5
def load_anagrams():
    anagrams = defaultdict(list)
    bags = []
    with open('resource/anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            if len(words[0]) > N: continue
            anagrams[words[0]] = words[1:]
            bags.append(Counter(words[0]))
    
    return bags, anagrams

def merge(bags, anagrams):
    mcount = 0
    for b1 in bags:
        longer_key= ''.join(sorted(b1.elements()))
        print longer_key
        for b2 in bags:
            if b1 == b2: continue
            b = deepcopy(b1)
            b.subtract(b2)
            if all([v>=0 for v in b.values()]):
                bags.remove(b2)
                key = ''.join(sorted(b2.elements()))
                
                anagrams[longer_key].extend(anagrams[key])
                del anagrams[key]
                mcount += 1
                print longer_key, len(bags), mcount, len(anagrams[longer_key])
                
    json.dump(anagrams, open('resource/merged_anagrams.json', 'w+'), indent=2)    
    print 'done'   
                
        
if __name__ == '__main__':
    bags, anagrams = load_anagrams()
    merge(bags, anagrams)
