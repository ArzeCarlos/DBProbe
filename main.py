import pymysql
import pymysql.cursors
def obtener_conexion():
    connection = pymysql.connect(host='localhost',
                             user='carlos',
                             password='Carlos123#',
                             database='1')
    with connection.cursor() as cursor:
    # Create a new record
       sql = "INSERT INTO `DevicesData` (`value`, `Datatype`) VALUES ('1', 'prueba')"
       cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `DevicesData`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)


if __name__ == '__main__':
    obtener_conexion()
