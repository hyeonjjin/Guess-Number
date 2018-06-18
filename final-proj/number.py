import random

class Number:

    def __init__(self):
        self.secret = 0
        self.trials = 0

    def newGame(self, max1):
        self.secret = random.randint(1,max1)
        self.trials = 0

    def guess(self, userGuess):
        self.trials += 1
        num=0
        h="Nothing"
        if(int(userGuess)<self.secret):
            h="Greater"
        elif (int(userGuess) > self.secret):
            h="Smaller"
        else:
            h="Correct"
        return h

    def getGuessCount(self):
        return self.trials


if __name__ == '__main__':
    s = Number()
    max1 = int(input("max = "))
    while(max1<100):
        print("max is greater than 100")
        max1=int(input("max = "))

    s.newGame(max1)
    ss="Nothing"
    while (ss!="Correct"):
        inputString = input("Your guess: ")
        while (int(inputString)<1) | (int(inputString)>max1):
            print("Input between 1 and %d !" %max1)
            inputString = input("Your guess: ")
        ss=s.guess(inputString)
        print(ss)

    guessCount = s.getGuessCount()
    print("SUCCESS in %d trials" % guessCount)
