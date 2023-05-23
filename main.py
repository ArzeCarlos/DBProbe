import pymysql
def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Carlos123#',
                                db='1')

if __name__ == '__main__':
    obtener_conexion()