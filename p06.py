import _sqlite3
from libs.db.dba import getConn

class Db:
    conn=getConn('/Users/Demian/Desktop/pythonproject/phone.db')
    cur=conn.cursor()
    def createtable(self):
        Db.cur.execute('create table tell(name text, no text)')

    def insert(self):
        self.name=input('Name ? = ')
        self.no=input('Phone Number ? = ')
        self.sql='Insert into Tell values(?,?)'
        Db.cur.execute(self.sql, (self.name, self.no))

    def select(self):
        self.sql='select * from tell'
        Db.cur.execute(self.sql)
        rs=Db.cur.fetchall()
        print('***** Date Print*****')
        for k, v in rs:
            print(k,v)

    def delete(self):
        self.name=input('Name ? = ')
        self.sql='delete from tell where name=?'
        Db.cur.execute(self.sql, (self.name,))
        print('{} is deleted',(self.name,))

    def update(self):
        self.name=input('Name ? = ')
        self.no=input('Phone Number ? =')
        self.sql='update tell set no=? where name=?'
        Db.cur.execute(self.sql, (self.no, self.name))

def main():
    d=Db()
    while True:
        n=input('a.Create Table, 1. Insert, 2. Select, 3, Delete, 4. Update, 0.Close : ')
        if n=='a':
            d.createtable()
        if n=='1':
            d.insert()
        if n=='2':
            d.select()
        if n=='3':
            d.delete()
        if n=='4':
            d.update()
        if n=='0':
            d.conn.commit()
            d.conn.close()
            break
    print('Program terminates')


if __name__ == '__main__':
    main()

