from config import config
import psycopg2
import psycopg2.extras

params = config()

conn = psycopg2.connect(**params)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute(
    'CREATE TABLE user (user_id SERIAL PRIMARY KEY NOT NULL, nick_name VARCHAR(20) NOT NULL)')

# print(cur.fetchone())


cur.close()
conn.close()
