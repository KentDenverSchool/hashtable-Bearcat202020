
class HashTable:

    def __init__(self, size):
        self.arr = [None] * size

    def put(self, key, value):
        hashedKey = myHash(key)
        self.arr[hashedKey] = value

    def remove(self, key):
        hashedKey = myHash(key)
        self.arr[hashedKey] = None

    def get(self, key):
        hashedKey = myHash(key)
        return self.arr[hashedKey]

    def hashCode(self, key):
        return myHash(key)

    def contains(self, key):
        hashedKey = myHash(key)
        return self.arr[hashedKey] != None


'''
Question 1:
    -a large prime number is better because it is less likely to create patterns when you mod numbers that are factors of the number you are modding by

    i.e.
        6%12 == 6
        12%12 == 0
        18%12 == 6
        24%12 == 0

    whereas a prime number like 11 creates less patterns
        6%11 == 6
        12%11 == 1
        18%11 == 7
        24%11 == 2 ...

Question 2:
    -summing characters is a bad way to hash because it ignores the order of the letters in the string
    -"hello" will be give the same hashed key as "elloh"

Question 3:
    -looking at the Java way of hashing, I think it works like one-way encryption
    -after snooping some more, i found this comment that says the method calculates the hashcode like this
        -s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
    -i believe n is the index of each character in the string





'''

def myHash(obj):
    hash = int(obj, 36) * 3803
    strHash = str(hash)
    bigPrime = 7949
    otherBigPrime = 4801
    num = 0

    for i in range(len(strHash)):
        if(i%3 == 0):
            num += int(strHash[i]) * otherBigPrime % bigPrime * i
        elif (i%3 == 1):
            num -= int(strHash[i]) * otherBigPrime % bigPrime * i
        else:
            num *= int(strHash[i]) * otherBigPrime % bigPrime * i


    return int(abs(num)) % 7963


if __name__ == "__main__":
    #check other doc for testing
    testArr = []
    i = 0
    firstLetter = 65
    secondLetter = 65
    thirdLetter = 65
    num = 0
    amountOfIterations = 1000
    while i < amountOfIterations:
        if thirdLetter >= 90:
            thirdLetter = 65
            secondLetter += 1
        elif secondLetter >= 90:
            secondLetter = 65
            firstLetter += 1
        else:
            thirdLetter += 1

        testStr = chr(firstLetter) + chr(secondLetter) + chr(thirdLetter)

        if myHash(testStr) in testArr:
            num += 1
        testArr.append(myHash(testStr))
        i+=1
    print("percent of collisions is:", num/amountOfIterations * 100, "%")
