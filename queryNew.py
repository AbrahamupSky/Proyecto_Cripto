import mysql.connector
from os import system as sys
from time import sleep

# Import the upload_file and download_file modules.
import upload_file

# Import the routes module.
import routes

# Establish the connection to the database.
cnx = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='cutdb'
)

# Create a cursor to execute queries.
cursor = cnx.cursor()

# Create a menu of options.
options = [
  "1. Consulta 1: Obtener nombres de usuarios ordenados alfabéticamente",
  "2. Consulta 2: Obtener conteo de usuarios por rol",
  "3. Consulta 3: Obtener nombres de usuarios con un rol específico",
  "4. Consulta 4: Obtener nombres de usuarios que contienen una letra, nombre o apellido",
  "5. Subir archivo",
  "6. Salir"
]

while True:
  print("Selecciona una opción:")
  for option in options:
    print(option)

  option = input("Ingresa el número de opción: ")

  if option == "1":
    query1 = "SELECT fullName FROM users ORDER BY fullName ASC"
    cursor.execute(query1)
  elif option == "2":
    query2 = "SELECT COUNT(*), role FROM users GROUP BY role"
    cursor.execute(query2)
    
  elif option == "3":
    role = int(input("¿Por qué rol quieres agrupar los registros?\nR= "))
    query3 = f"SELECT fullName FROM users WHERE role={role}"
    cursor.execute(query3)
    
  elif option == "4":
    c = input("Ingresa una letra, nombre o apellido:\nR=")
    query4 = f"SELECT fullName FROM users WHERE fullName LIKE '%{c}%' "
    cursor.execute(query4)
    
  elif option == "5":
    # Get the file path from the user.
    file_path = input("Ingresa la ruta del archivo: ")

    # Upload the file to the server and encrypt it.
    encrypted_file_path, encryption_key = upload_file.upload_file(file_path)

    # Print the encrypted file path and the encryption key.
    print("El archivo se ha subido y encriptado correctamente.")
    print("La ruta del archivo encriptado es:", encrypted_file_path)
    print("La clave de encriptación es:", encryption_key)
    
  elif option == "6":
    # Salir del programa
    break
  
  else:
    print("Opción inválida. Por favor, selecciona una opción válida.")

  # Obtener los resultados
  # results = cursor.fetchall()

  # Imprimir los resultados
  # for row in results:
    # print(row)
