# 2-Level Rail Fence Cipher

def railfence_encrypt(text):
    # remove spaces for simplicity
    text = text.replace(" ", "")
    rail1, rail2 = "", ""
    # zig-zag writing
    for i, ch in enumerate(text):
        if i % 2 == 0:
            rail1 += ch
        else:
            rail2 += ch
    return rail1 + rail2


def railfence_decrypt(cipher):
    # split into two rails
    mid = (len(cipher) + 1) // 2
    rail1 = cipher[:mid]
    rail2 = cipher[mid:]
    result = ""
    # interleave chars back
    for i in range(len(cipher)):
        if i % 2 == 0:
            result += rail1[i // 2]
        else:
            result += rail2[i // 2]
    return result


# ---------------- Demo ----------------
if __name__ == "__main__":
    msg = "HELLO WORLD"
    enc = railfence_encrypt(msg)
    dec = railfence_decrypt(enc)

    print("Original :", msg)
    print("Encrypted:", enc)
    print("Decrypted:", dec)
