'''
Utility class for interacting with ChatGPT API
'''
from db_util import DbUtil

db_util: DbUtil = DbUtil()
db_util.connect()
data = db_util.query('manufacturers')
print(data)
db_util.disconnect()
