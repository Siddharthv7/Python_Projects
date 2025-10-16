import hashlib

# Take input from user
data = input("Enter a message: ")
data_changed = input("Enter a slightly changed message: ")

# Compute MD5 hashes
hash1 = hashlib.md5(data.encode()).hexdigest()
hash2 = hashlib.md5(data_changed.encode()).hexdigest()

# Show results
print("\nOriginal message hash:", hash1)
print("Changed message hash: ", hash2)

# Verify integrity
if hash1 == hash2:
    print("\nData is intact!")
else:
    print("\nData has been altered!")
