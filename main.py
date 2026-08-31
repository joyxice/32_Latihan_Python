import matematika as mtk
import bangun_ruang as br

def main():

    def prima(angka):
        print(f'angka {angka} adalah bilangan prima') if mtk.prima(angka) else print(f'angka {angka} bukanlah bilangan prima')

    def akar(angka):
        print(mtk.akar(angka))

    def ganjil_genap(angka):
        print(f'angka {angka} adalah bilangan genap') if mtk.ganjil_genap(angka) else print(f'ankga {angka} adalah bilangan ganjil')

    def luas_kubus(alas, tinggi):
        print(br.luas_kubus(alas, tinggi))

    def diagonal_segiempat(sisi1, sisi2):
        print(br.diagonal_segiempat(sisi1, sisi2))

    pilihan = ['cek bilangan prima', 'akar bilangan', 'cek ganjil genap', 'hitung luas kubus', 'hitung diagonal segi empat']

    print('====== OPERASI MATEMATIKA DAN BANGUN RUANG ======\n')
    for i in range(len(pilihan)):
        print(f'{i+1}. {pilihan[i]}')
    konfirmasi = int(input('\nmasukkan pilihan: '))
    print('')
    if konfirmasi == 1:
        print(f'====== {pilihan[konfirmasi-1]} ======')
        angka = int(input('masukkan angka: '))
        print(prima(angka))
    elif konfirmasi == 2:
        print(f'===== {pilihan[konfirmasi-1]} ======')
        angka = int(input('masukkan angka: '))
        akar(angka)
    elif konfirmasi == 3:
        print(f'====== {pilihan[konfirmasi-1]} ======')
        angka = int(input('masukkan angka: '))
        ganjil_genap(angka)
    elif konfirmasi == 4:
        print(f'====== {pilihan[konfirmasi-1]} ======')
        alas = int(input('masukkan alas: '))
        tinggi = int(input('masukkan tinggi: '))
        luas_kubus(alas, tinggi)
    elif konfirmasi == 5:
        print(f'====== {pilihan[konfirmasi-1]} ======')
        sisi1 = int(input('masukkan sisi pertama: '))
        sisi2 = int(input('masukkan sisi kedua: '))
        diagonal_segiempat(sisi1, sisi2)
    else:
        print('masukkan pilihan yang benar!\n')
    
if __name__ == '__main__':
    main()