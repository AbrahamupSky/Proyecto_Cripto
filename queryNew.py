import mysql.connector
from os import system as sys
from time import sleep

# Import the routes module.
import routes

# Import the encryption function.
from cryptography.fernet import Fernet

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
  "5. Encriptar texto y guardarlo en un archivo",
  "6. Desencriptar texto desde un archivo",
  "7. Salir"
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
    # Get the text from the user.
    text = input("Ingresa el texto a encriptar: ")

    # Generate an encryption key.
    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)

    # Encrypt the text.
    encrypted_text = cipher_suite.encrypt(text.encode())

    # Save the encrypted text to a file.
    file_path = "encrypted_text.txt"
    with open(file_path, 'wb') as file:
      file.write(encrypted_text)

    print("El texto se ha encriptado y guardado correctamente en el archivo 'encrypted_text.txt'.")
    print("La clave de encriptación es:", encryption_key.decode())

  elif option == "6":
      # Get the encrypted file path from the user.
      file_path = input("Ingresa la ruta del archivo encriptado: ")

      # Read the encrypted text from the file.
      with open(file_path, 'rb') as file:
          encrypted_text = file.read()

      # Get the encryption key from the user.
      encryption_key = input("Ingresa la clave de encriptación: ")

      try:
          # Create a cipher suite with the provided encryption key.
          cipher_suite = Fernet(encryption_key.encode())

          # Decrypt the text.
          decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

          # Save the decrypted text to a file.
          decrypted_file_path = "decrypted_text.txt"
          with open(decrypted_file_path, 'w') as file:
              file.write(decrypted_text)

          print("El texto se ha desencriptado y guardado correctamente en el archivo 'decrypted_text.txt'.")

      except:
          print("Error: La clave de encriptación no es válida.")

  elif option == "7":
    # Salir del programa
    break

  else:
    print("Opción inválida. Por favor, selecciona una opción válida.")
    
    # Obtener los resultados
    results = cursor.fetchall()

    # Imprimir los resultados
    for row in results:
        print(row)
    input("\n\nPresiona Enter para continuar...")
    sys("cls")

    input("\n\nPresiona Enter para continuar...")
    sys("cls")

cursor.close()
cnx.close()