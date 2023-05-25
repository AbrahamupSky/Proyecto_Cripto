import mysql.connector
from os import system as sys
from time import sleep
from cryptography.fernet import Fernet

# Establecer la conexión
cnx = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='cutdb'
)

# Crear un cursor para ejecutar consultas
cursor = cnx.cursor()

while True:
  print("Selecciona una opción:")
  print("1. Consulta 1: Obtener nombres de usuarios ordenados alfabéticamente")
  print("2. Consulta 2: Obtener conteo de usuarios por rol")
  print("3. Consulta 3: Obtener nombres de usuarios con un rol específico")
  print("4. Consulta 4: Obtener nombres de usuarios que contienen una letra, nombre o apellido")
  print("5. Encriptar texto y guardarlo en un archivo")
  print("6. Desencriptar texto desde un archivo")
  print("7. Salir")

  string = ''
  option = input("Ingresa el número de opción: ")

  if option == "1":
    query1 = "SELECT fullName FROM users ORDER BY fullName ASC"
    cursor.execute(query1)

    # Obtener los resultados
    results = cursor.fetchall()

    # Imprimir los resultados
    for row in results:
      string += row[0] + '\n'

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    encrypted_text = cipher_suite.encrypt(string.encode())

    file_path = "query1.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)
    
    print("La clave de encriptación es:", encryption_key.decode())

  elif option == "2":
    query2 = "SELECT COUNT(*), role FROM users GROUP BY role"
    cursor.execute(query2)

    # Obtener los resultados
    results = cursor.fetchall()

    # Imprimir los resultados
    for row in results:
      string += f'numero de personas con este rol {row[1]}: {row[0]} \n'

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    encrypted_text = cipher_suite.encrypt(string.encode())

    file_path = "query1.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)
    
    print("La clave de encriptación es:", encryption_key.decode())
    
  elif option == "3":
    role = int(input("¿Por qué rol quieres agrupar los registros?\nR= "))
    query3 = f"SELECT fullName FROM users WHERE role={role}"
    cursor.execute(query3)

    # Obtener los resultados
    results = cursor.fetchall()

    string = f'personas con rol {role}: \n'

    # Imprimir los resultados
    for row in results:
      string += f'{row[0]} \n'

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    encrypted_text = cipher_suite.encrypt(string.encode())

    file_path = "query1.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)
    
    print("La clave de encriptación es:", encryption_key.decode())
    
  elif option == "4":
    c = input("Ingresa una letra, nombre o apellido:\nR=")
    query4 = f"SELECT fullName FROM users WHERE fullName LIKE '%{c}%' "
    cursor.execute(query4)

    # Obtener los resultados
    results = cursor.fetchall()

    string = f'personas cuyo nombre contiene: {c} \n'

    # Imprimir los resultados
    for row in results:
      string += row[0] + '\n'

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    encrypted_text = cipher_suite.encrypt(string.encode())

    file_path = "query1.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)
    
    print("La clave de encriptación es:", encryption_key.decode())
    
  elif option == "5":
    text = input("Ingresa el texto a encriptar: ")

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    encrypted_text = cipher_suite.encrypt(text.encode())

    file_path = "encrypted_text.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)

    file_path1 = 'key.txt'
    with open(file_path1, 'wb') as file:
      file.write(encryption_key)

    print("El texto se ha encriptado y guardado correctamente en el archivo 'encrypted_text.txt'.")
    print("La clave de encriptación es:", encryption_key.decode())

  elif option == "6":
    file_path = input("Ingresa la ruta del archivo encriptado: ")

    with open(file_path, 'rb') as file:
      encrypted_text = file.read()

    encryption_key = input("Ingresa la clave de encriptación: ")

    try:
      cipher_suite = Fernet(encryption_key.encode())

      decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

      decrypted_file_path = "decrypted_text.txt"
      with open(decrypted_file_path, 'w') as file:
        file.write(decrypted_text)

      print("El texto se ha desencriptado y guardado correctamente en el archivo 'decrypted_text.txt'.")

    except:
      print("Error: La clave de encriptación no es válida.")

  elif option == "7":
    break


  else:
    print("Opción inválida. Por favor, selecciona una opción válida.")

  input("\n\nPresiona Enter para continuar...")
  sys("cls")
  
# Cerrar el cursor y la conexión
cursor.close()
cnx.close()
