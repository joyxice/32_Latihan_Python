import matematika as mtk
import bangun_ruang as br
import sqlite3
import os

def register():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')

    print('========= REGISTER =========')
    username = str(input('Masukkan username: '))
    password = str(input('Masukkan password: '))
    cursor.execute('INSERT INTO user(username, password) VALUES(?, ?)', (username, password))
    print('registrasi berhasil!')
    conn.commit()
    conn.close()

def login():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print('========= LOGIN =========')

    username = str(input('Masukkan username: '))
    password = str(input('Masukkan password: '))

    cursor.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
    status = cursor.fetchone()
    conn.close()

    if status:
        return True
    else:
        print('username atau password salah!')
        return False

def program():
    while True:

        pilihan = [
        'cek bilangan prima',
        'akar bilangan',
        'cek ganjil genap',
        'hitung luas kubus',
        'hitung diagonal segi empat'
        ]

        print('====== OPERASI MATEMATIKA DAN BANGUN RUANG ======\n')
        for i in range(len(pilihan)):
            print(f'{i+1}. {pilihan[i]}')
        konfirmasi = int(input('\nmasukkan pilihan: '))
        print('')
        if konfirmasi == 1:
            print(f'====== {pilihan[konfirmasi-1]} ======')
            angka = int(input('masukkan angka: '))
            print(f'angka {angka} adalah bilangan prima') if mtk.prima(angka) else print(f'angka {angka} bukanlah bilangan prima')

        elif konfirmasi == 2:
            print(f'===== {pilihan[konfirmasi-1]} ======')
            angka = int(input('masukkan angka: '))
            print(mtk.akar(angka))

        elif konfirmasi == 3:
            print(f'====== {pilihan[konfirmasi-1]} ======')
            angka = int(input('masukkan angka: '))
            print(f'angka {angka} adalah bilangan genap') if mtk.ganjil_genap(angka) else print(f'ankga {angka} adalah bilangan ganjil')

        elif konfirmasi == 4:
            print(f'====== {pilihan[konfirmasi-1]} ======')
            alas = int(input('masukkan alas: '))
            tinggi = int(input('masukkan tinggi: '))
            print(br.luas_kubus(alas, tinggi))

        elif konfirmasi == 5:
            print(f'====== {pilihan[konfirmasi-1]} ======')
            sisi1 = int(input('masukkan sisi pertama: '))
            sisi2 = int(input('masukkan sisi kedua: '))
            print(br.diagonal_segiempat(sisi1, sisi2))

        else:
            print('masukkan pilihan yang benar!\n')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('>>> PILIH MENU <<<\n')

    pilihan = [
        'login',
        'register'
    ]

    for i in range(len(pilihan)):
        print(f'{i+1}. {pilihan[i]}')

    print('')

    choice = int(input('Masukkan pilihan: '))
    if choice == 1:
        log = login()
    elif choice == 2:
        register()
    else:
        main()

    if log:
        program()

if __name__ == '__main__':
    main()