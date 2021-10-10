import pymysql.cursors

# MariaDB
conn = pymysql.connect(
    host='192.168.11.9',
    port=3307,
    db='ShinkanBot',
    user='admin',
    password='admin',
    cursorclass=pymysql.cursors.DictCursor)

def select(sql, params=None):
    cur = conn.cursor()
    if params is not None:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    return cur

# def insert(sql, params=None, doCommit=True):
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if params is not None:
#         cur.execute(sql, params)
#     else:
#         cur.execute(sql)
    
#     if doCommit:
#         conn.commit()

# def update(sql, params=None, doCommit=True):
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if params is not None:
#         cur.execute(sql, params)
#     else:
#         cur.execute(sql)
    
#     if doCommit:
#         conn.commit()

# def delete(sql, params=None, doCommit=True):
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     if params is not None:
#         cur.execute(sql, params)
#     else:
#         cur.execute(sql)
    
#     if doCommit:
#         conn.commit()

# def commit():
#     conn.commit()
