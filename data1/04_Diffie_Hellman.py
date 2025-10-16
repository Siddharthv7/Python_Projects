p = 23
g = 5

a = 6
A = pow(g, a, p)
print("ALice public key: ", A)

b = 15
B = pow(g, b, p)
print("BOb public key: ", B) 

shared_key_Alice = pow(B, a, p)
shared_key_Bob = pow(A, b, p)

print("Shared key computed by Alice: ", shared_key_Alice)
print("Shared key computer by Bob: ", shared_key_Bob)
