import pymysql

class Libros:

    #conecto a la base de datos
    def abrir(self):
        connection = pymysql.connect(host='localhost',user='root',password='', db='20181020_version1')
        return connection
        

    def alta(self, datos):
        connect = self.abrir()
        #creo el puntero
        cursor=connect.cursor()
        #realizar consulta sql
        print("entrando a consulta")
        #sql="INSERT INTO libro (Titulo,Numero,Paginas,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        sql="INSERT INTO libro (Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,fecha,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        try:
            print("try")
            cursor.execute(sql)
            #cerrar puntero
            connect.commit()
        except:
            print("except")
            #en el caso de error
            connect.rollback()
        cursor.close()
        connect.close()


    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Titulo from libro where nombre=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone = self.abrir()
        cursor=cone.cursor()
        sql="SELECT idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado FROM libro"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
        
    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas