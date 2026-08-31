import matematika as mtk
import bangun_ruang as br


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