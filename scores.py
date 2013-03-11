from collections import defaultdict
from pprint import pprint

class Board: 
    def __init__(self, letters):
        """ Using a string of length 25 to represent a board
            e.g.,
            "VBBNFBDBVJMLSNDVXNAETVIOR", which corresponds to
            VBBNF
            BDBVJ
            MLSND
            VXNAE
            TVIOR
        """    
        self.letters = letters.lower()
           
        self.size = 5
        self.n = self.size**2
        self.colors  = ""
        self.BuildLocation() 
        self.score = {'w': 0.5, 'b': 0., 'r': 0., 
                        'c': 0.,  'p': 1.}   

    def BuildLocation(self):
        self.map = defaultdict(list)
        for idx, letter in enumerate(self.letters):
            self.map[letter].append(idx)
            
    def SetColor(self, colors):
        """
            'w' -> white
            'b' -> blue
            'r' -> red
            'c' -> cyan, light blue
            'p' -> pink, light red
        """
        self.colors = colors
    
    def IsWhite(self, idx):
        return self.colors[idx] == 'w'
    
    def IsLightRed(self, idx):
        return self.colors[idx] == 'p'
    
    def GetIndexScore(self, idx):
        return self.IsLightRed(idx) * self.score['p'] + \
            self.IsWhite(idx) * self.score['w']

    def GetMaxWordScore(self, word):
        word = word.lower()
        score = 0.0
        location_used = set()
        for letter in word:
            best_letter_score = 0.
            best_location = None
            for idx in self.map[letter]:
                if idx in location_used: continue
                letter_score = self.GetIndexScore(idx)
                if best_letter_score < letter_score:
                    best_letter_score = letter_score
                    best_location = idx
            score += best_letter_score
            location_used.add(best_location)
            print letter, best_location, best_letter_score
        return score

    def GetFirstMoveLetters(self):
        pos = [0,1,2,3,4,5,6,8,9,10,14,15,16,18,19,20,21,22,23,24]
        return ''.join([self.letters[idx] for idx in pos])
            

if __name__ == '__main__':
    bb =  Board("VBBNFBDBVJMLSNDVXNAETVIOR")
    bb.SetColor("wwcpprrrrrrrwwwwwwwwwwwww")
    pprint (bb.map)
    print bb.GetIndexScore(5)
    print bb.GetMaxWordScore("beadnn")
    