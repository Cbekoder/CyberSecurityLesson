def encryption(alphabet, a, b, text):
    alphabet_dict = {char: idx for idx, char in enumerate(alphabet)}
    ciphertext = ""

    for char in text:
        if char in alphabet:
            char_idx = alphabet_dict[char]
            ciphertext_idx = (a * char_idx + b) % len(alphabet)
            ciphertext += alphabet[ciphertext_idx]
        else:
            ciphertext += char

    return ciphertext
def decryption(alphabet, a, b, ciphertext):
    alphabet_dict = {char: idx for idx, char in enumerate(alphabet)}
    plaintext = ""

    for char in ciphertext:
        if char in alphabet:
            char_idx = alphabet_dict[char]
            plaintext_idx = (pow(a, -1, len(alphabet)) * (char_idx - b)) % len(alphabet)
            plaintext += alphabet[plaintext_idx]
        else:
            plaintext += char

    return plaintext

def main():
    print("Affine Cipher shifrlash va deshifrlash")
    k = int(input("""Amaliyot turini tanlash:
    1: Shifrlash
    2: Deshifrlash
(1/2)>>>"""))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}:. "
    if k ==1:
        plainText = input("Shifrlash uchun matn: ")
        keya = int(input("'a'-kalitni kiriting: "))
        keyb = int(input("'b'-kalitni kiriting: "))
        print(f"Shifrlangan matn: {encryption(alphabet, keya, keyb, plainText)}")
    elif k ==2:
        ctext = input("Deshifrlash uchun matn: ")
        keya = int(input("'a'-kalitni kiriting: "))
        keyb = int(input("'b'-kalitni kiriting: "))
        print(f"Deshifrlangan matn: {decryption(alphabet, keya, keyb, ctext)}")

    else:
        print("Noto'g'ri kiritma!")
        main()
    if input("\n\nYana amaliyotni bajarish uchun istalgan belgini kiriting,\n aks holda shunchaki 'Enter' tugmasini bosing:"):
        main()
main()