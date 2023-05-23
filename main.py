import pymysql
import pymysql.cursors
def obtener_conexion():
    connection = pymysql.connect(host='localhost',
                             user='carlos',
                             password='Carlos123#',
                             database='1')
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `DevicesData`"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)


if __name__ == '__main__':
    obtener_conexion()
