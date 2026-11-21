def hitung(nilai1, nilai2):
    selisih = nilai1 - nilai2
    if selisih < 0:
        return -selisih
    return selisih

def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    hasil = hitung(a, c) + hitung(b, d)
    print(mutlak(hasil))

if __name__ == "__main__":
    main()