import time
from collections import defaultdict
from itertools import combinations, combinations_with_replacement

def load_anagrams():
    anagrams = defaultdict(list)
    with open('resource/anadict.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            anagrams[words[0]] = words[1:]
    return anagrams

def find_words(board, anagrams, max_length=16):
    board = ''.join(sorted(board))
    target_words = []
    for word_length in range(2, len(board) + 1):
        for combination in combinations(board, word_length):
            word = ''.join(combination)
            if word in anagrams:
                target_words += anagrams[word]
    return target_words

def is_valid(board):
    return True
    
def iterall(anagrams):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print len(letters)
    N = 25
    
    tnow = time.time()
    for i, board in enumerate(combinations_with_replacement(letters, N)):
        board = ''.join(board)
        if not is_valid(board): continue
        num_solution = len(find_words(board, anagrams))
        if num_solution >= 10:
            print board, num_solution
        if i%100 == 0: 
            print i, (time.time() -tnow)
            tnow = time.time()
            
if __name__ == "__main__":
    anagrams = load_anagrams()
    print len(anagrams)
    print find_words("asdwtribnowplf", anagrams)
    iterall(anagrams)
