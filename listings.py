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

def outputList(fileList):
    # dl = [ id for id in getDownloadedFiles()] 

    c = [Checkbox('docs', message='List of Google Docs:', choices=[x['title'] for x in fileList]) ]
    # need to impliment already downloaded check, then return a clean
    # prompt list
    return prompt(c)
    
