from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import listings

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

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

# force keyword args out of laziness
def downloadDocument(*, request):
    for id in request:
        fileToWrite = drive.CreateFile({'id' : id})
        fileToWrite.FetchMetadata()
        fileToWrite.GetContentFile('./Downloaded/' + fileToWrite['title'])

# is this even good practice any more? Is there a better standard? Probably.
def main():
    getList()

if __name__ == '__main__':
    main()
