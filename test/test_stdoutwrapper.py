from cligui import stdoutwrapper

def test_stdoutwrapper():
    print('should not be in buffer')
    w = stdoutwrapper.Wrapper()
    print('Should show up')
    assert w.getvalue() == 'Should show up\n'
