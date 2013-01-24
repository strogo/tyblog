import MySQLdb


class Entry:
    def __init__(self):
        self.title = ''
        self.html = ''
        self.markdown = ''
        self.time = ''
        self.catagory = ''
        self.tag =''


def ConnectDatabase():
    conn = MySQLdb.connect('localhost', 'root', 'helloworld','python')
    return conn

conn = ConnectDatabase()
cursor = conn.cursor()

def isDBConnecting():
    global cursor
    try:
        cursor.execute('show tables;')
        return True
    except:
        return False


def NewPost(entry):
    global conn, cursor
    if isDBConnecting() is False:
        conn = ConnectDatabase()
        cursor = conn.cursor()
    sql = "insert into post (title, html, markdown,  catagory, tag)" \
          "values ('%s', '%s', '%s', '%s', '%s')" % \
          (entry.title, entry.html, entry.markdown, entry.catagory, entry.tag)
    cursor.execute(sql)
    conn.commit()
            
def getRecentPosts():
    global conn, cursor
    if isDBConnecting() is False:
        conn = ConnectDatabase()
        cursor = conn.cursor()
    cursor.execute('select * from post ;')
    results = cursor.fetchall()
    print results
    entries = []
    entry = Entry()
    for result in results:
        entry.title = result[1]
        entry.html = result[2]
        entry.markdown = result[3]
        entry.time = '2012-12-12'
        entry.catagory = result[5]
        entry.tag = result[6]
        entries.append(entry)
    return entries
    
        

if __name__ == '__main__':
    entry = Entry
    entry.title = 'first blood'
    entry.html = '<h1>FB</h1><br><p>hahahaha</p>'
    entry.markdown = 'hi i am markdown'
    entry.catagory = 'haha'
    entry.tag = 'a|b'
    NewPost(entry)
    entries = getRecentPosts()
    conn.commit()
    conn.close()

