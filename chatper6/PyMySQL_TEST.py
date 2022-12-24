import pymysql
conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = '계정비번', db='mysql')
cur = conn.cursor()
cur.execute("Use scraping")
cur.execute("select * from pages where id = 1")
print(cur.fetchone())
cur.close()
conn.close()