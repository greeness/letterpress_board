from collections import defaultdict
import matplotlib.pyplot as plt
from pprint import pprint
import math
from Levenshtein import distance
import json

class Dictionary:
    def __init__(self, anagram_file_name):
        self.n_words = 0
        self.Anagrams = self.load_anagrams(anagram_file_name)
        self.index_anagrams()
        print 'anagram counts %d, word counts %d' % (len(self.Anagrams), self.n_words)
        
        
    def load_anagrams(self, anagram_file_name):
        anagrams = defaultdict(list)
        
        with open(anagram_file_name, 'r') as file_handle:
            #try:
                for line in file_handle:
                    words = line.split()
                    anagrams[words[0]] = words[1:]
                    self.n_words += len(words) - 1
            #except:
            #    raise Exception('unhandled anagrams')

        return anagrams
    
    def get_edit_distance(self, a1, a2):
        return distance(a1, a2)
    
    def load_connections(self):
        self.conn = json.load(open('resource/conn.json'))
        self.Index= json.load(open('resource/anagram_idx.json'))
        print 'conn graph loaded'
        
    def construct_connection(self):
        self.conn = defaultdict(list)
        for length in range(2, 26):
            group1 = self.anagram_len[length]
            # iterate every anagram in group1
            for seq, a1 in enumerate(group1):
                n_conn = 0
                idx1 = self.Index[a1]
                for length_candidate in range(length, length+2):
                    group2 = self.anagram_len[length_candidate]
                    for a2 in group2:
                        if a1 == a2: continue
                        n_diff= self.get_edit_distance(a1, a2)
                        if n_diff > 1: continue
                        self.connect(idx1, self.Index[a2])
                        n_conn += 1
                if seq % 100 == 0: 
                    print 'len-%2d-%5d, connect %d:%s to %d' \
                        %(length, seq, idx1, a1, n_conn)
                            
        #import json
        #json.dump(self.conn, open('resource/conn.json', 'w'), indent=2)
        #json.dump(self.Index, open('resource/anagram_idx.json', 'w'), indent=2)                  
        
    def group_anagram_by_len(self):
        self.anagram_len = defaultdict(list)
        for anagram in self.Anagrams:
            if len(anagram) > 25: continue
            self.anagram_len[len(anagram)].append(anagram)
        for length in range(25):
            print '%2d, %5d' % (length, len(self.anagram_len[length]))
    
    def index_anagrams(self):
        self.Index = defaultdict(int)
        self.RevIndex = defaultdict(str)
        for i, anagram in enumerate(self.Anagrams):
            self.Index[anagram] = i
            self.RevIndex[i] = anagram
            
    def connect(self, idx1, idx2):
        self.conn[idx1].append(idx2)
        self.conn[idx2].append(idx1)
        
    def profile(self):
        anagram_len = []
        for anagram in self.Anagrams:
            anagram_len.append(len(anagram))
        plt.hist(anagram_len, bins=27, normed=False)
        plt.xlabel("Word Length")
        plt.ylabel("Word Count")
        plt.show()
    
    
    
if __name__ == '__main__':
    dic = Dictionary('resource/anadict.txt')
    #dic.profile()
    dic.group_anagram_by_len()
    dic.load_connections()
    print len(dic.conn)
    """
    for anagram in dic.Anagrams:
        key = str(dic.Index[anagram])
        if key not in dic.conn: continue
        
        for neighbor in dic.conn[key]:
            print "%s -> %s, %d " % (anagram, dic.RevIndex[neighbor], neighbor) 
    """
    #dic.construct_connection()