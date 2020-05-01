import random

class verbiageGenerator:
    def __init__(self):
        self.nouns = open ('./lib/words/nouns.txt', 'r').readlines()
        self.verbs = open ('./lib/words/verbs.txt', 'r').readlines()
        self.adjectives = open ('./lib/words/adjectives.txt', 'r').readlines()

    def getVerb(self, startsWith=None):
        return random.choice(self.verbs)

    def getNoun(self, startsWith=None):
        return random.choice(self.nouns)

    def getAdjective(self, startsWith=None):

        return random.choice(self.adjectives)

    