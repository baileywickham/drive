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
    # listings.outputList([x['title'] for x in fileList]) 
    # passes full list for later metadata support
    request = listings.outputList(fileList)
    print(type(fileList))
    idRequests = [ fileList['title'].get(x) for x in request.values()]
 

# force keyword args out of laziness
def downloadDocument(*, request, fileList):
    fileToWrite = drive.CreateFile()
    fileToWrite.GetContentFile()
    with open('Downloaded/', 'w') as localFile:
        localFile.write(fileToWrite)


def main():
    getList()

if __name__ == '__main__':
    main()
