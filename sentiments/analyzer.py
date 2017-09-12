# 這個analyzer.py是一個module,裡面有一個叫Analyzer的class, class裡面有一個method叫analyze, 而__init__是初始化Analyzer這個class的method

import nltk

class Analyzer(): # In here is our definition of the Analyzer class, which has two methods, __init__ and analyze
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positive_words = set() # 創一個set空間給self.positive_words
        self.negative_words = set()

        file = open(positives, "r") # open the file whichs address is the variable "positives"
        for line in file:
            if line.startswith(";") == False: # 若該行開頭沒有";"符號的話,才執行下面的動作
                self.positive_words.add(line.rstrip("\n")) # access the set called positive_words, and add to it the line I've encountered after stripping off the trailing new line
        file.close()

        file = open(negatives, "r") # open the file whichs address is the variable "negatives"
        for line in file:
            if line.startswith(";") == False:
                self.negative_words.add(line.rstrip("\n"))
        file.close()


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text) # 把text裡的內容拆開成一個一個的單字,存到tokens這個list裡
        sum = 0
        for word in tokens:
            if word.lower() in self.positive_words:
                sum += 1
            elif word.lower() in self.negative_words:
                sum -= 1
            else:
                sum += 0
        return sum
