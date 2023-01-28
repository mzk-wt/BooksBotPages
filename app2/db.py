# import pymysql.cursors

# # MariaDB
# conn = pymysql.connect(
#     host='192.168.11.9',
#     port=3307,
#     db='ShinkanBot',
#     user='admin',
#     password='admin',
#     cursorclass=pymysql.cursors.DictCursor)

# def select(sql, params=None):
#     cur = conn.cursor()
#     if params is not None:
#         cur.execute(sql, params)
#     else:
#         cur.execute(sql)
#     return cur

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./bookscurationbot-firebase-adminsdk-dchn5-1db2ecb1c6.json')
firebase_admin.initialize_app(cred)

def get(collectionName, wheres, order):
    db = firestore.client()

    query = db.collection(collectionName)

    for where in wheres:
        query = query.where(where['column'], where['ope'], where['condition'])

    if order:
        query = query.order_by(order)
    
    return query.get()


