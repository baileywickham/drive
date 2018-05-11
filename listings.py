import readchar
testList = ['opion 1', 'option 2', 'third option', 'forth']

lenList = [0 for i in range(len(testList))] 
# there has to be a better way to do this.
lenList[0] = 1

def outputList(testList):
    while True:
        for idex, litem in enumerate(testList):
           print(litem, " : (" + str(int(lenList[idex])) + ")" ) 
        if readchar.readkey() == readchar.key.UP:
            print("up arrow")

outputList(testList)
