def encryption(text, key, harflar):
    res = []
    for i in text:
        g = key
        if i.islower():
            g += harflar.index(i.upper())
            res.append(harflar[g%26].lower())
        elif i.isupper():
            g += harflar.index(i)
            res.append(harflar[g%26])
        else:
            res.append(i)
    return "".join(map(str, res))

def decryption(cipher, key, harflar):
    res = []
    for i in cipher:
        g = 0
        if i.islower():
            g = harflar.index(i.upper()) - key
            res.append(harflar[(26+g) % 26].lower())
        elif i.isupper():
            g = harflar.index(i) -key
            res.append(harflar[(26+g) % 26])
        else:
            res.append(i)
    return "".join(map(str, res))
def main():
    print("Ceasar Cipher shifrlash va deshifrlash")
    k = int(input("""Amaliyot turini tanlash:
    1: Shifrlash
    2: Deshifrlash
(1/2)>>>"""))
    harflar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    if k ==1:
        plainText = input("Shifrlash uchun matn: ")
        key = int(input("Kalit sonni kiriting: "))
        print(f"Shifrlangan matn: {encryption(plainText, key, harflar)}")
    elif k ==2:
        ctext = input("Deshifrlash uchun matn: ")
        key = int(input("Kalit sonni kiriting: "))
        print(f"Deshifrlangan matn: {decryption(ctext, key, harflar)}")
    else:
        print("Noto'g'ri kiritma!")
        main()
    if input("\n\nYana amaliyotni bajarish uchun istalgan belgini kiriting,\n aks holda shunchaki 'Enter' tugmasini bosing:"):
        main()
main()