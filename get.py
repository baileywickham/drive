from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import listings

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#TODO add upload function, add check diff func. 
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
    optionList = {'Download' : getList(),
            'Edit' : pass,
            'Upload' : pass}

    optionList[showOptions()]

# is this even good practice any more? Is there a better standard? Probably.
def main():
    getList()

# this is for modules, will not run unless it's being run on it's own.
if __name__ == '__main__':
    main()
