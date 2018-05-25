import listings
import xattr


def test_DocID():
    listings.setDocID(id = b"test", name='test.file')
    assert xattr.getxattr('Downloaded/test.file', 'user.docid') == b"test"
