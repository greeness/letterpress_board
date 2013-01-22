import json
from collections import defaultdict, Counter
#from pprint import pprint
from itertools import  combinations_with_replacement
import copy

N = 25
letters = "abcdefghijklmnopqrstuvwxyz"

def load_anagrams():
    anagrams = defaultdict(list)
    with open('resource/anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            if len(words[0]) > N: continue
            anagrams[words[0]] = words[1:]
    return anagrams

def create_link():
    
    anagrams = load_anagrams()
    
    links = defaultdict(list)
    
    sorted_anagrams = sorted(anagrams.iteritems(), key=lambda (k,v):len(k))
    
    zeros = 0
    for i,(k,v) in enumerate(sorted_anagrams):
        bag = Counter(k)
        #print i,k, v
        
        # one edit distance
        filters = list(letters)
        for char in letters:
            new_bag = bag+Counter(char)
            new_anagram = ''.join(sorted(new_bag.elements()))
            if new_anagram in anagrams:
                #print new_anagram, '->', anagrams[new_anagram]
                links[k].append(new_anagram)
                filters.remove(char)
        
        comb_length = 2
        max_comb_length = min(5, 25-len(k))
        while comb_length <= max_comb_length and len(filters) >= comb_length:
            print'-- max comb %d, trying comb-length %d, filters %s' % (max_comb_length, comb_length,''.join(filters))
            # try two edit distance
            for c in combinations_with_replacement(filters, comb_length):
                new_bag = bag + Counter(c)
                new_anagram = ''.join(sorted(new_bag.elements()))
                if new_anagram in anagrams:
                    #print new_anagram, '->', anagrams[new_anagram]
                    links[k].append(new_anagram)
                    for letter in c:
                        if letter in filters:
                            filters.remove(letter)
                            
            comb_length += 1
        
        print i,k, len(links), len(links[k]), zeros
    #for k,v in links.iteritems():
    #    print k,v 
    
    json.dump(links, open('resource/links.json', 'w+'), indent=2)
    json.dump(links, open('resource/reverse_links.json', 'w+'), indent=2)
        
create_link()
