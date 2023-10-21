def keylist(key, n):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    res = []
    for i in range(n):
        res.append(letters.index(key[i%len(key)].upper()))
    return res

def encryption(text, key):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    n = len(text)-text.count(" ")
    keys = keylist(key, n)
    kn = 0
    res = ""
    for word in text.split():
        for i in range(len(word)):

            if word[i].islower():
                keys[kn] += letters.index(word[i].upper())
                res+=letters[keys[kn] % 26].lower()
                kn += 1
            elif word[i].isupper():
                keys[kn] += letters.index(word[i])
                res+=letters[keys[kn] % 26]
                kn += 1
            else:
                res+=word[i]
        res += " "
    res = res[:-1]
    return res
def decryption(cipher, key):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    n = len(cipher) - cipher.count(" ")
    keys = keylist(key, n)
    kn = 0
    res = ""
    for word in cipher.split():
        for i in range(len(word)):
            g = 0
            if word[i].islower():
                g = letters.index(word[i].upper()) - keys[kn]
                res += letters[(26+g) % 26].lower()
                kn += 1
            elif word[i].isupper():
                g = letters.index(word[i]) - keys[kn]
                res += letters[(26+g) % 26]
                kn += 1
            else:
                res += word[i]
        res += " "
    res = res[:-1]
    return res
def main():
    print("Viginere Cipher shifrlash va deshifrlash")
    k = int(input("""Amaliyot turini tanlash:
    1: Shifrlash
    2: Deshifrlash
(1/2)>>>"""))
    if k ==1:
        plainText = input("Shifrlash uchun matn: ")
        key = input("Kalit so'zni kiriting: ")
        print(f"Shifrlangan matn: {encryption(plainText, key)}")
    elif k ==2:
        ctext = input("Deshifrlash uchun matn: ")
        key = input("Kalit so'zni kiriting: ")
        print(f"Deshifrlangan matn: {decryption(ctext, key)}")
    else:
        print("Noto'g'ri kiritma!")
        main()
    if input("\n\nYana amaliyotni bajarish uchun istalgan belgini kiriting,\n aks holda shunchaki 'Enter' tugmasini bosing:"):
        main()
main()




