from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

def getList():
    fileList = drive.ListFile({'q' : "mimeType = 'application/vnd.google-apps.document'"}).GetList()

    docs = {}

    for i in fileList:
        docs.update({ i['title'] : i['id']})
        # str literal, needs > 3.6
        # print(f"the name is {f.title}")
        # print('title: %s, id: %s, type: %s'  % (i['title'], i['id'], i['mimeType']))
    print(docs)


# Should docs be global or should I pass it in?
def downloadDocument(id):
    fileToWrite = drive.CreateFile({'id' : id})
    fileToWrite.GetContentFile()
    with open('Downloaded/', 'w') as localFile:
        localFile.write(fileToWrite)

def main():
    getList()

if __name__ == '__main__':
    main()
