from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement
from pprint import pprint
from copy import deepcopy
import json


N = 5*5
def load_anagrams():
    anagrams = {}
    #anagrams_lookup = defaultdict(list)
    bags = []
    with open('resource/anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            if len(words[0]) > N: continue
            anagrams[words[0]] = len(words[1:])
            #anagrams_lookup[words[0]] = words[1:]
            bags.append(Counter(words[0]))
            #print '-'*100
            #print anagrams_lookup[words[0]]
            #print anagrams[words[0]]
    return bags, anagrams

def merge(bags, anagrams):
    mcount = 0
    sorted_bags = sorted(bags, key=lambda b: sum(b.values()))
    for b1 in sorted_bags:
        shorter_key= ''.join(sorted(b1.elements()))
        for b2 in sorted_bags:
            # skip itself
            if b1 == b2: continue
            # deepcopy required otherwise bags get modified
            b = deepcopy(b2)
            # get a diff
            b.subtract(b1)
            if all([v>=0 for v in b.values()]):
                longer_key = ''.join(sorted(b2.elements()))
                # merging the count              
                anagrams[longer_key] += anagrams[shorter_key]
                
        del anagrams[shorter_key]
        mcount += 1        
        print "shorter key %26s, unprocessed anagrams %6d, %.3f done" % \
            (shorter_key, len(anagrams), mcount*100./len(bags))
                
    json.dump(anagrams, open('resource/merged_anagrams_short.json', 'w+'), indent=2)    
    print 'done'   
                
        
if __name__ == '__main__':
    bags, anagrams = load_anagrams()
    #bb = sorted(bags, key=lambda b: sum(b.values()))[:50]
    #pprint(bb)
    merge(bags, anagrams)
