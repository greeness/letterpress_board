from collections import defaultdict


def load_dict(dictfile='resource/enable2k.txt'):
    anagram = defaultdict(list)
    for word in file(dictfile):
        word = word.strip()
        key = ''.join(sorted(word))
        anagram[key].append(word)
        
    print len(anagram)
    anagram_dictionary = sorted([' '.join([key] + value) for key, value in anagram.items()])
    with open('resource/anadict.txt', 'w') as file_handle:
        file_handle.write('\n'.join(anagram_dictionary))
        
if __name__ == '__main__':
    load_dict()
        