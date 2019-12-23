from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from Conexion import Conexion

app=Flask(__name__)
app.secret_key='mysecretkey'

try:
  cx=Conexion('remotemysql.com','ZFhrcj5iN5','UeaWxigh5H','ZFhrcj5iN5')
  #Ingresar Datos
  #sql="Insert into Persona(nombres,apellidos)values('Wendy','German')"
  #cx.ejecutar_sentencia(sql)
  #Consultar datos
  sql="Select id, nombres, apellidos from Persona"
  cursor=cx.ejecutar_sentencia(sql)
  datos=cursor.fetchall()
  for data in datos:
    print(data[0])
    print(data[1])
    print(data[2])

  
  cx.commit()
except Exception as e:
  cx.rollback()
  print(e)
finally:
  cx.cerrar_conexion()

@app.route('/')
def index():
  #Para mostrar los datos
  try:
    cx=Conexion('remotemysql.com','ZFhrcj5iN5','UeaWxigh5H','ZFhrcj5iN5')
    sql="Select id, nombres, apellidos from Persona"
    cursor=cx.ejecutar_sentencia(sql)
    datos=cursor.fetchall()
    cx.commit()
  except Exception as e:
    cx.rollback()
    print(e)
  finally:
    cx.cerrar_conexion()
  return render_template('index.html',contacts=datos)

@app.route('/add_contact',methods=['POST'])
def add_contact():
  #Para añadir los datos
  if request.method=='POST':
    nombres=request.form['nombres']
    apellidos=request.form['apellidos']
    #para comprobar que me recibe
    #print(nombres)
    #print(apellidos)
    #Aqui le doy datos a mysql
    try:
      cx=Conexion('remotemysql.com','ZFhrcj5iN5','UeaWxigh5H','ZFhrcj5iN5')
    #Ingresar Datos
      sql="INSERT INTO Persona(nombres,apellidos) values(\"%s\",\"%s\")"%(nombres,apellidos)
      cx.ejecutar_sentencia(sql)
      cx.commit()
      flash('Agregado')
    except Exception as e:
      cx.rollback()
      print(e)
    finally:
      cx.cerrar_conexion()
    #####################################
    
    return redirect(url_for('index'))

app.run(host='0.0.0.0',port=8080, debug=True)



"""
db = pymysql.connect(
      host='remotemysql.com',
      user='ZFhrcj5iN5',
      password='UeaWxigh5H',
      db='ZFhrcj5iN5'
    )
print(db)
cursor=db.cursor()

sql="Insert into Persona(nombres,apellidos)values('Dorival','Pichamba')"
cursor.execute(sql)
db.commit()

sql="Select id, nombres, apellidos from Persona"
cursor.execute(sql)
datos=cursor.fetchall()

for data in datos:
  print(data[0])
  print(data[1])
  print(data[2])
"""





