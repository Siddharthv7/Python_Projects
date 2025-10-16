p, q = 61, 53
n, phi = p*q, (p-1)*(q-1)

e = 17
d = next(x for x in range(1, phi) if (e*x) % phi == 1)

print("Public key (e, n): ", (e, n))
print("private key (d, n): ", (d, n))

msg = "Hello RSA!"

encrypted = [pow(ord(c), e, n) for c in msg]
print("encrypted:" , encrypted)

decrypted = ''.join([chr(pow(c, d, n)) for c in encrypted])
print("Decryptedd: ", decrypted)