def main():
    jalan = 'y'
    while True:
        if jalan == 'y' or jalan == 'Y':
            x = int(input('Masukkan angka: '))
            print(f'bilangan {x} adalah genap') if x % 2 == 0 else print(f'bilangan {x} adalah ganjil')
        else:
            break
        jalan = str(input('Lanjut? (y/n): '))

if __name__ == '__main__':
    main()