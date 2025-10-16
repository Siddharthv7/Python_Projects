from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = b'myscreatkey'
data = b'HELLO WORLD!'

cipher = Blowfish.new(key, Blowfish.MODE_ECB)

padded_data = pad(data, Blowfish.block_size)

encrypted = cipher.encrypt(padded_data)
print("Encrypted: ", encrypted.hex())

decrypted = cipher.decrypt(encrypted)

orignal_data = unpad(decrypted, Blowfish.block_size)
print("Decrypted: ", orignal_data.decode())