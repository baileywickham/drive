from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q' : 'type=document'}).GetList()
for i in fileList:
    # str literal, needs > 3.6
    # print(f"the name is {f.title}")
    print('title: %s, id: %s' % (i['title'], i['id']))
