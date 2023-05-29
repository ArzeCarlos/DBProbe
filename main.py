import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Carlos123#',
                             database='1')

with connection:  
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM devices"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
