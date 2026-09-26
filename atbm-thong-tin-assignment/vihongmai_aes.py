import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Tạo khóa 128-bit (16 bytes) ngẫu nhiên
key = os.urandom(16)
iv = os.urandom(16)
plaintext = "Bài tập Mã hóa AES - Môn An toàn bảo mật thông tin"

# Quy trình Mã hóa (Encryption)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Quy trình Giải mã (Decryption)
decryptor = cipher.decryptor()
padded_plain = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
decrypted_text = (unpadder.update(padded_plain) + unpadder.finalize()).decode('utf-8')

print("--- KẾT QUẢ MÃ HÓA AES ---")
print("Bản rõ ban đầu :", plaintext)
print("Khóa AES (Hex) :", key.hex())
print("Bản mã (Hex)   :", ciphertext.hex())
print("Sau khi giải mã:", decrypted_text)
