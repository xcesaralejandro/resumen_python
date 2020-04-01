import sqlite3
import pprint
# .connect() Crea la base de datos si no existe
# OBS: recordar que sqlite es publica ya que no tiene usuarios de db

conexion = sqlite3.connect("firstdb")

# Para trabajar con la db necesitamos un cursor
cursordb = conexion.cursor()




# CREAR TABLAS
# OBS: Las ''' te permitirán crear saltos de linea en los strings y pasarte las tabulaciones por el orto.
create_table_emails_sql = '''create table if not exists emails(
                                id integer primary key autoincrement, 
                                email varchar(255), 
                                name varchar(255), 
                                lastname varchar(255)
                            )'''
cursordb.execute(create_table_emails_sql)




# INSERTAR UN REGISTRO
insert_record_sql = "insert into emails(email,name,lastname) values('usuario0@usuario0.cl','usuario','cero')"
cursordb.execute(insert_record_sql)




# INSERTAR VARIOS REGISTROS
usuarios = (
    ('usuario1@usuario1.cl','usuario','uno'),
    ('usuario2@usuario2.cl','usuario','dos'),
    ('usuario3@usuario3.cl','usuario','tres'),
)
insert_records_sql = "insert into emails(email,name,lastname) values(?,?,?)"
cursordb.executemany(insert_records_sql, usuarios)




# CONSULTAR REGISTROS
select_emails_sql = "select * from emails"
cursordb.execute(select_emails_sql)
records = cursordb.fetchall() 
pprint.pprint(records)
#luego de ejecutar una acción que MANIPULE LOS DATOS de la db hay que hacer un commit
conexion.commit()
conexion.close()


# UPDATE Y DELETE
# Estos metodos se ejecutan con la función .execute() pasando el sql respectivo.