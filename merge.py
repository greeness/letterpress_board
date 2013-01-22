from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement
from pprint import pprint
from copy import deepcopy
import json


N = 5*5
def load_anagrams():
    anagrams = {}
    anagrams_lookup = defaultdict(set)
    bags = []
    with open('resource/anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            if len(words[0]) > N: continue
            anagrams[words[0]] = len(words[1:])
            for w in words[1:]:
                anagrams_lookup[words[0]].add(w)
            bags.append(Counter(words[0]))
    return bags, anagrams_lookup

def merge(bags, anagrams_lookup):
    mcount = 0
    sorted_bags = sorted(bags, key=lambda b: sum(b.values()))
    for b1 in sorted_bags:
        shorter_key= ''.join(sorted(b1.elements()))
        for b2 in sorted_bags:
            # skip itself
            if b1 == b2: continue
            # get a diff
            b = b2 - b1
            if all([v>=0 for v in b.values()]):
                longer_key = ''.join(sorted(b2.elements()))
                # merging the count
                #print 'before long' , anagrams_lookup[longer_key]
                #print 'before short', anagrams_lookup[shorter_key]             
                anagrams_lookup[longer_key] = anagrams_lookup[longer_key] | anagrams_lookup[shorter_key]
                #print 'after', anagrams_lookup[longer_key]
                
        del anagrams_lookup[shorter_key]
        sorted_bags.remove(b1)
        mcount += 1        
        print "shorter key %26s, completed %d, unprocessed anagrams %6d, %.3f done" % \
            (shorter_key, mcount, len(sorted_bags), mcount*100./len(bags))
                
    json.dump(anagrams_lookup, open('resource/merged_anagrams_lookup.json', 'w+'), indent=2)    
    print 'done'   
                
        
if __name__ == '__main__':
    bags, anagrams_lookup = load_anagrams()
    #bb = sorted(bags, key=lambda b: sum(b.values()))[:50]
    #pprint(bb)
    merge(bags, anagrams_lookup)
