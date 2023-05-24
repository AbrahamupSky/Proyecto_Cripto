import secrets
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def upload_file(file_path):
    """Uploads a file to the server and encrypts it.

    Args:
        file_path: The path to the file to upload.

    Returns:
        A tuple of the encrypted file path and the encryption key.
    """

    # Open the file in binary mode.
    with open(file_path, "rb") as f:
        file_data = f.read()

    # Generate a random encryption key.
    encryption_key = secrets.token_bytes(32)  # 32 bytes = 256 bits

    # Encrypt the file data.
    encrypted_file_data = encrypt(file_data, encryption_key)

    # Print the encrypted data.
    print("Encrypted data:", encrypted_file_data)

    # Save the encrypted file data to a file.
    encrypted_file_path = "encrypted_file.dat"
    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_file_data)

    # Return the encrypted file path and the encryption key.
    return encrypted_file_path, encryption_key


def encrypt(data, encryption_key):
    """Encrypts data using the encryption key.

    Args:
        data: The data to encrypt.
        encryption_key: The encryption key.

    Returns:
        The encrypted data.
    """
    # Generate a random initialization vector (IV)
    iv = secrets.token_bytes(16)  # 16 bytes = 128 bits

    # Create a cipher using AES encryption in CBC mode
    cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Pad the data to match the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Perform the encryption
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Return the IV concatenated with the encrypted data
    return iv + encrypted_data
