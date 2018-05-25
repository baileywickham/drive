# drive
The goal of this is to provide a cli interface for downloading,editing, and uploading documents to Google Drive. It uses the PyDrive wrapper.

## Requirements
Built with python 3.8, the dev branch. May lead to compatibility problems.

## Use Case
None, but it was fun to make. I want to use it to edit my essays with vim.
## Installing
#### Clone the repo. 
``` git clone https://github.com/baileywickham/drive.git ```

#### Install dependencies
``` pipenv install ```

#### Get a client_secret.json from the Google API console.
This is important for the Google API

#### Run it
``` 
pipenv shell

python3 get.py
```

## TODO
Fix the Upload function

Add a diff checker to get changes and auto upload when changed on disk

Do something about formats.

Figure out how to access the decorator list without violating scope issues.

WRITE UNIT TESTS
