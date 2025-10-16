import hashlib

# Take input from user
data = input("Enter original message: ")
data_changed = input("Enter slightly changed message: ")

# Compute SHA-256 hashes
hash1 = hashlib.sha256(data.encode()).hexdigest()
hash2 = hashlib.sha256(data_changed.encode()).hexdigest()

# Display results
print("\nOriginal message hash:", hash1)
print("Changed message hash:  ", hash2)

# Verify integrity
if hash1 == hash2:
    print("\nData is intact!")
else:
    print("\nData has been altered!")
