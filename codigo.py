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
        print(f'Datos de consulta {datos}')
        #sql="INSERT INTO libro (Titulo,Numero,Paginas,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        #sql="INSERT INTO libro (Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES ('%s','%d','%d','%s','%s','%s','%s','%d','%d','%d','%d')" % (titulo,numero,paginas,fecha,isbn,imagen,link,pais,editorial,cantidad_pedidas,estado)
        sql="INSERT INTO libro (Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(f'sql {sql}')
        #print("ingresando datos")
        cursor.execute(sql, datos)
        connect.commit()
          
        #cursor.close()
        connect.close()

    def consulta(self, datos):
        connect=self.abrir()
        cursor=connect.cursor()
        sql="select idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado FROM libro WHERE idLibro=%s"
        print(f'sql consulta {sql}')
        cursor.execute(sql, datos)
        print(f'datos {datos}')
        #cursor.close()
        connect.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        connect=self.abrir()
        cursor=connect.cursor()
        sql="SELECT idLibro,Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado FROM libro"
        print(f'sql {sql}')
        cursor.execute(sql)

        #cursor.close()
        connect.close()
        return cursor.fetchall()
        
    def baja(self, datos):
        connect=self.abrir()
        cursor=connect.cursor()
        sql="delete from libro where idlibro=%s"
        print(f'sql {sql}')
        cursor.execute(sql, datos)
        connect.commit()

        #cursor.close()
        connect.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        connect = self.abrir()
        #creo el puntero
        cursor=connect.cursor()
        print(f'Datos de consulta UPDATE {datos}')
        sql="UPDATE libro SET Titulo=%s,Numero=%s,Paginas=%s,FechaPublicacion=%s,ISBN=%s,LinkImagen=%s,LinkDescarga=%s,Pais_idPais=%s,Editorial_idEditorial=%s,CantidadVecesPedidas=%s,Estado=%s where idLibro=%s"
        #sql="UPDATE `libro` SET `Titulo`=[value-2],`Numero`=[value-3],`Paginas`=[value-4],`FechaPublicacion`=[value-5],`ISBN`=[value-6],`LinkImagen`=[value-7],`LinkDescarga`=[value-8],`Pais_idPais`=[value-9],`Editorial_idEditorial`=[value-10],`CantidadVecesPedidas`=[value-11],`Estado`=[value-12] WHERE `Titulo`=[value-2]"
        #print(f'Datos de consulta UPDATE 68 {datos}')
        
        print(f'sql 69 {sql}')
        cursor.execute(sql, datos)
        connect.commit()
          
        #cursor.close()
        connect.close()
        #print(f'cursor 62 {cursor.rowcount}')
        return cursor.rowcount # retornamos la cantidad de filas modificadas