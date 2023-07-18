# your code goes here!

class Anagram:   
    
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matched_list = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                matched_list.append(word)
        return matched_list
