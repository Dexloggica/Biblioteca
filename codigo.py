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
        sql="select Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado from libro where titulo=%s"
        print(f'sql {sql}')
        cursor.execute(sql, datos)

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
        sql="delete from libro where Titulo=%s"
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
        #sql="UPDATE libro SET (Titulo=%s,Numero=%d,Paginas=%d,FechaPublicacion=%s,ISBN=%s,LinkImagen=%s,LinkDescarga=%s,Pais_idPais=%d,Editorial_idEditorial=%d,CantidadVecesPedidas=%d,Estado=%d) where (Titulo=%s)"
        sql="UPDATE libro SET Titulo=%s,Numero=%s,Paginas=%s,FechaPublicacion=%s,ISBN=%s,LinkImagen=%s,LinkDescarga=%s,Pais_idPais=%s,Editorial_idEditorial=%s,CantidadVecesPedidas=%s,Estado=%s where Titulo=%s"
        #sql = "UPDATE libro SET (Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE Titulo=%s"
        #sql= "UPDATE libro SET Titulo,Numero,Paginas,FechaPublicacion,ISBN,LinkImagen,LinkDescarga,Pais_idPais,Editorial_idEditorial,CantidadVecesPedidas,Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE Titulo=%s"
        #sql="UPDATE libro SET Titulo={0},Numero={1},Paginas={2},FechaPublicacion={3},ISBN={4},LinkImagen={5},LinkDescarga={6},Pais_idPais={7},Editorial_idEditorial={8},CantidadVecesPedidas={9},Estado={10} WHERE Titulo={0}".format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[0])
        #sql = "UPDATE libro SET Titulo={0},Numero={1},Paginas={2},FechaPublicacion={3},ISBN={4},LinkImagen={5},LinkDescarga={6},Pais_idPais={7},Editorial_idEditorial={8},CantidadVecesPedidas={9},Estado={10} WHERE Titulo={0}"
        print(f'sql 67 {sql}')
        print(f'Datos de consulta UPDATE 68 {datos}')
        cursor.execute(sql, datos)
        connect.commit()
          
        #cursor.close()
        connect.close()
        #print(f'cursor 62 {cursor.rowcount}')
        return cursor.rowcount # retornamos la cantidad de filas modificadas