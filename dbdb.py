import sqlite3

def dbcon(): 
    return sqlite3.connect('mydb.db')

def create_table(): 
    try:
        query = '''
            CREATE TABLE "user" (
            	"id"	VARCHAR(50),
            	"pw"	VARCHAR(50),
            	"name"	VARCHAR(50),
            	PRIMARY KEY("id")
            ); 
            '''
        db = dbcon() 
        c = db.cursor() 
        c.execute(query) 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close()

def insert_data(num, name): 
    try: 
        db = dbcon()
        c = db.cursor() 
        setdata = (num, name) 
        c.execute("INSERT INTO student VALUES (?, ?)", setdata) 
        db.commit() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close()

def select_all(): 
    ret = list() 
    try: 
        db = dbcon() 
        c = db.cursor() 
        c.execute('SELECT * FROM student') 
        ret = c.fetchall() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret

def select_num(num): 
    ret = () 
    try: 
        db = dbcon() 
        c = db.cursor() 
        setdata = (num,) 
        c.execute('SELECT * FROM student WHERE num = ?', setdata) 
        ret = c.fetchone() 
    except Exception as e: 
        print('db error:', e) 
    finally: 
        db.close() 
        return ret

# create_table()
# insert_data('20201236', '디비')
# ret = select_num('20201236')
# print(ret)
create_table()