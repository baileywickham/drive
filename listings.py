# I think this will be depricated.
import os
import xattr
import readchar
from inquirer import Checkbox, prompt

# there has to be a better way to do this.
# turns out there is and it has half the number of lines.
def getDownloadedFiles():
    idList = [xattr.getxattr(file, 'user.docid') for file in os.listdir('./Downloaded')] 
    # generator because it should only be compared once. 
    yield idList 

def outputList(nameList, idList):
    dl = [ id for id in getDownloadedFiles() if id in [x for x in idList]] 
        
    c = [Checkbox('documents', message='List of Google Docs:', choices=nameList)]
    prompt(c)
