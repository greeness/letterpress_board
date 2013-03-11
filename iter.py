import time

import sys
import logging
from pprint import pprint
from collections import defaultdict
from itertools import combinations
from dictionary import Dictionary
from scores import Board

logging.basicConfig(format='%(message)s',level=logging.DEBUG)
logger = logging.getLogger('letterpress')
class Bot : 
    
    def __init__(self, letters):
        self.dic = Dictionary('resource/anadict.txt')
        logger.info("Dictionary loaded: %d anagrams, %d words.", 
                     len(self.dic.Anagrams), self.dic.n_words)    
        self.max_word_len = 18
        self.big_board = Board(letters)
    
    def find_words(self, letters, required=[], disabled=set()):
        letters = ''.join(sorted(letters))
        target_words = set()
        for word_length in range(self.max_word_len, 2, -1):
            for combination in combinations(letters, word_length):
                if not required:
                    word = ''.join(combination)
                else:
                    word = ''.join(sorted(''.join(combination) + required))
                if word in self.dic.Anagrams:
                    for w in self.dic.Anagrams[word]:
                        target_words.add(w)
                        if len(target_words) > 5:
                            return sorted(list(target_words))
    
    def is_valid(self, word, disabled_words):
        for w in disabled_words:
            if w.startswith(word):
                return False
        return True
    
    def first_move(self):
        subletters = self.big_board.GetFirstMoveLetters()
        return self.find_words(subletters)
        
if __name__ == "__main__":
    
    letters = ''.join([letter.lower() for letter in sys.argv[1] if letter.isalpha()])
    logger.info("board letters %s", letters)
    bot = Bot(letters)
    
    words = bot.first_move()
    
    """if len(sys.argv) == 2:
        words = bot.find_words(letters)
    elif len(sys.argv) == 3:
        words = bot.find_words(letters, sys.argv[2])
    else:
        print 'usage: %s $board ($required)'
        exit()"""
    
    
    words_by_len = defaultdict(list)
    for w in words:
        words_by_len[len(w)].append(w)

    for length in words_by_len:
        for word in words_by_len[length]:
            print "Len-%2d, %s" % (length, word)

    
