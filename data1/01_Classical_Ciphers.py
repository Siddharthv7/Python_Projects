def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(test, k):
    return caesar_encrypt(test, -k)

def rot13(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.upper() else ord('a')
            result += chr((ord(ch) - base + 13) % 26 +base)
        else:
            result += ch
    return result

def rot13(text):
    return caesar_encrypt(text, 13)

def atbash(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.upper() else ord('a')
            result += chr(base +(25 -(ord(ch) - base)))
        else:
            result += ch
    return result

if __name__ == "__main__":
    msg = "HELLO"
    
    c_enc = caesar_encrypt(msg, 3)
    c_dec = caesar_decrypt(c_enc, 3)
    
    r_enc = rot13(msg)
    r_dec = rot13(r_enc)
    
    a_enc = atbash(msg)
    a_dec = atbash(a_enc)
    
print("Orignal: ", msg)
print("Caesar: ", c_enc, "->", c_dec)
print("Rot13: ", r_enc, "->", r_dec)
print("Atbash: ", a_enc, "->", a_dec) 