# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Given a list of words, determine whether the words can be chained to form a circle. 
# A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

# For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can 
# form the following circle: chair --> racket --> touch --> height --> tunic --> chair.

#############################################################################
# Credit goes to https://github.com/mission-peace                           #
# I gave up and just ported their Java code to python to learn how it works #
#############################################################################

class WordCircle():
    def __init__(self, startingArray):
        self.startingArray = startingArray
        self.finalArr = [startingArray[0]]
        self.used = [False] * len(startingArray)
        self.firstChar = startingArray[0][0]

    def getFinalArray(self):
        self.finalArr.append(self.finalArr[0])
        return self.finalArr

    def findCircle(self):
        if len(self.startingArray) == len(self.finalArr):
            str = self.finalArr[len(self.finalArr) - 1]
            if self.startingArray[0][0] == str[len(str) - 1]:
                return True
            return False
        
        str = self.finalArr[len(self.finalArr) - 1]
        lastChar = str[len(str) - 1]
        for i in range(1, len(self.startingArray)):
            if self.used[i]:
                continue
            if lastChar == self.startingArray[i][0]:
                self.used[i] = True
                self.finalArr.append(self.startingArray[i])
                r = self.findCircle()
                if r:
                    return True
                self.used[i] = False
                del self.finalArr[len(self.finalArr) - 1]


if __name__ == "__main__":
    # input = ["geeks", "king", "seeks", "sing", "gik", "kin"]
    # input = ["king","gik","geeks", "seeks", "sing"]
    input = ["chair", "height", "racket", "touch", "tunic"]
    circle = WordCircle(input)
    result = circle.findCircle()

    if not result:
        print("No chain")
    else:
        print(", ".join(circle.getFinalArray()))