def cek_ganjil(n):
    if n % 2 != 0:
        return True
    else:
        return False

def main():
    n = int(input("Masukkan bilangan: "))
    
    for i in range(n + 1):
        if cek_ganjil(i):
            print(i ** 2)

if __name__ == "__main__":
    main()