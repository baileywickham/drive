# I think this will be depricated.
import os
import xattr
from inquirer import Checkbox, prompt, List

def getDownloadedFiles():
    idList = [xattr.getxattr(os.path.join('Downloaded', file), 'user.docid') for file in os.listdir('./Downloaded')] 
    # generator because it should only be compared once. 
    yield idList 

def outputList(fileList):
    # dl = [ id for id in getDownloadedFiles()] 

    c = [Checkbox('docs', message='List of Google Docs:', choices=[x['title'] for x in fileList]) ]
    # need to impliment already downloaded check, then return a clean
    # prompt list
    # Genorator is no longer optimized
    responses = prompt(c)['docs']
    return [file['id'] for file in fileList if file['title'] in responses and file['id'] not in getDownloadedFiles()]

def setDocID(*, id, name):
    xattr.setxattr(os.path.join('Downloaded', name), 'user.docid', id)

def showOptions():
    c = [List('options', message='Welcome to Drive', choices=['Download', 'Edit', 'Upload'])]
    return prompt(c)['options']

