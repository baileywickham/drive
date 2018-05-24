from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import listings #TODO figure out when I should split files, and not put all of this in one.

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#TODO add upload function, add check diff func. 
@dictionary('Download')
def getList():
    # sharedWithMe = false returns a 404 error. This is an api problem.
    fileList = drive.ListFile({'q' : "mimeType = 'application/vnd.google-apps.document'", 'maxResults' : 10}).GetList()

    #No idea when this would fail but it looks good.
    assert fileList is not None

    # str literal, needs > 3.6
    # print(f"the name is {f.title}")
    # passes full list for later metadata support
    request = listings.outputList(fileList)
    downloadDocument(request=request) 

@dictionary('Upload')
def upload():
    lc = input("enter the file location:")
    newFile = drive.CreateFile({"title" : lc.split("/")[len(lc.split("/")) - 1]})
    newFile.setContentFile(lc)
    newFile.Upload()
    # We are going to hope upload can autodetermine mimeType, otherwise
    # I'll have to use an ugly Dict.


# force keyword args out of laziness, eventually I'll add more args.
def downloadDocument(*, request):
    # Downloads doc from ids returned.
    # TODO show progress. use readable format.
    for id in request:
        fileToWrite = drive.CreateFile({'id' : id})
        fileToWrite.FetchMetadata()
        fileToWrite.GetContentFile('./Downloaded/' + fileToWrite['title'] + '.pdf',
                mimetype='application/pdf')
        listings.setDocID(id=id, name=fileToWrite['title'])


def options():
    # this will list the options, including download, open, and upload
    option = listings.showOptions()

"""
so... the logic here is that a. I want to use decorators, and b. I want to make it easy to 
add to the option lists. I am not sure that this is the right place to use decorators, 
but I like the idea and it is good practice. I am fairly sure it should motify the function
in some way to make it a propper use. also I need to access the list somehow
"""
def dictionary(func, listName):
    optionList.append(listName : func.__name__)
    return func


# is this even good practice any more? Is there a better standard? Probably.
def main():
    getList()


# this is for modules, will not run unless it's being run on it's own.
if __name__ == '__main__':
    main()
