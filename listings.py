# I think this will be depricated.
import os
import xattr
from inquirer import Checkbox, prompt

def getDownloadedFiles():
    idList = [xattr.getxattr(file, 'user.docid') for file in os.listdir('./Downloaded')] 
    # generator because it should only be compared once. 
    yield idList 

def outputList(fileList):
    # dl = [ id for id in getDownloadedFiles()] 

    c = [Checkbox('docs', message='List of Google Docs:', choices=[x['title'] for x in fileList]) ]
    # need to impliment already downloaded check, then return a clean
    # prompt list
    return prompt(c)['docs']
    
