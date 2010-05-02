from config import *
import MySQLdb as mysql

conn = mysql.connect(host = DB_HOST, user = DB_USERNAME, passwd = DB_PASSWORD, db = DB_NAME)
sql_query= 'select ID, post_content from wp_posts'
c = conn.cursor()
c.execute(sql_query)
result = c.fetchall()

sql_update = 'update wp_posts set post_content = \'%s\' where ID = %d'

for r in result:
    novo_valor = r[1].replace('http://www.franciscosouza.net', 'http://www.franciscosouza.com.br')
    id = r[0]
    c.execute(sql_update % (conn.escape_string(novo_valor), id))
    conn.commit()
    print id

