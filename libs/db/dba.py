import _sqlite3

def getConn(dbpath):
    #conn=_sqlite3.connect("/Users/Demian/Desktop/pythonproject/abc.db")
    conn=_sqlite3.connect(dbpath)
    return conn
