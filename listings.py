# I think this will be depricated.
import readchar
from inquirer import Checkbox, prompt
testList = ['opion 1', 'option 2', 'third option', 'forth']
answerList = [1,0,0,1]
lenList = [0 for i in range(len(testList))] 
# there has to be a better way to do this.
lenList[0] = 1

def outputList(testList):
    while True:
        for idex, litem in enumerate(testList):
            print(litem, " : (" + str(int(lenList[idex])) + ")" ) 

        key = readchar.readkey()
        if key == readchar.key.UP or key == 'w':
            lenList[idex + 1] = 1
            lenList[idex] = 0
            idex = idex + 1
        if key == readchar.key.DOWN or key == 's':
            lenList[idex - 1] = 1
            lenList[idex] = 0
            idex = idex + 1
        if key == readchar.key.CTRL_C:
            raise KeyboardInterrupt()
        print("idex =", idex)
        print("this is the current list: ", lenList)

c = [Checkbox('interests', message="interest check", choices=testList, default=answerList)]
print(prompt(c))
