import random, string, itertools, time
from tqdm import tqdm

alphabet = string.printable[:95]
charlength = 3
passw = 'slm'
startTime = int(time.time())
numpw = 0


def generaterandpw(charlength):
    outStr = ''
    while len(outStr) < charlength:
        outStr += random.choice(alphabet)
    return outStr

def bruteforce(PwToBrute,pwAlphabet):
    estimatedTime = int((alphabet.index(PwToBrute[0]) / len(alphabet)) * (len(alphabet) ** charlength))
    global numpw
    pwTuple = tuple(PwToBrute)
    charList = [[x for x in alphabet]] * len(PwToBrute)
    args = [char for char in charList]
    for combination in tqdm(itertools.product(*args),total = estimatedTime):
        numpw += 1
        if combination == pwTuple:
            return combination

    
if __name__=="__main__":
    randpw = generaterandpw(charlength)
    print(f"attemting to brute {randpw}")
    result = bruteforce(randpw,alphabet)
    endTime = int(time.time())
    print(f"bruteforced password {result} in {endTime - startTime} seconds, with a total of {numpw} attempts" )