import sqlite3 
conn = sqlite3.connect('mydb.db')

# Cursor 객체 생성 
c = conn.cursor()

# 학번을 검색해서 정보 출력
num = ('20201234',)
c.execute('SELECT * FROM student WHERE num = ?', num)
print(c.fetchone())

#  접속한 db 닫기
conn.close()

# CREATE TABLE "users" (
# 	"id"	VARCHAR(50),
# 	"pw"	VARCHAR(50),
# 	"name"	VARCHAR(50),
# 	PRIMARY KEY("id")
# );