import psycopg2
conn = psycopg2.connect(database='dvdrental',user='postgres',password=admin)
cur = conn.cursor()
cur.execute('SELECT * FROM payment')
cur.fetchall(2)
