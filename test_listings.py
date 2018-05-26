import listings
import xattr
import get
import os

def test_DocID():
    listings.setDocID(id = b"test", name='test.file')
    assert xattr.getxattr('Downloaded/test.file', 'user.docid') == b"test"
    xattr.removexattr('Downloaded/test.file', 'user.docid')

def test_Download():
    get.downloadDocument(request='todo')
    assert os.path.exists('Downloaded/todo.pdf')
    os.remove('Downloaded/todo.pdf')
