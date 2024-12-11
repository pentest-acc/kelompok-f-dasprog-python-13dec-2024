import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 40
garis = "=" * 40

print("")
print("")
print("Sistem Pengadaan Barang Dan Jasa Gaikindo".upper().center(40))
print(garis.center(40))
print("| No  |  Menu")
print(garis.center(40))
nomor = ["| 1  ",
         "| 2  ",
         "| 3  ",
         "| 4  ",
         "| 5  ",
         "| 6  ",
         "| 7  ",
         "| 8  ",
         ]

menu = ["|  Tambah Data Pengadaan",
        "|  Lihat Daftar Pengadaan",
        "|  Verifikasi Data Pengadaan",
        "|  Lihat Daftar Pemesanan Pembelian",
        "|  Penerimaan Barang",
        "|  Pembayaran Ke Vendor",
        "|  Tentang Kami",
        "|  keluar",]

for angka, daftar in zip(nomor, menu) :
  print(angka, daftar)
print(garis.center(40))
print("")

def jalankan_modul(file_name):
    with open(file_name) as f:
        kode = f.read()
    exec(kode)
    
def jalankan_modul1(file_name1):
    with open(file_name1) as f1:
        kode1 = f1.read()
    exec(kode1, globals())


pilih = input("Pilih Menu (1-8) : ")

if pilih == "1" :
   jalankan_modul1("TambahDataPengadaan.py")
elif pilih == "2" :
   jalankan_modul1("DaftarPengadaan.py")
elif pilih == "3" :
   jalankan_modul1("VerifikasiPengadaan.py")
elif pilih == "4" :
   jalankan_modul1("LihatPO.py")
elif pilih == "5" :
   jalankan_modul1("PenerimaanBarang.py")
elif pilih == "6" :
   jalankan_modul1("PembayaranVendor.py")
elif pilih == "7" :
   jalankan_modul("Team.py")
elif pilih == "8" :
   quit("Anda Keluar Dari Menu Utama, Program Dihentinkan!")
else :
   quit("Anda Menginput Pilihan Angka Yang Tidak Tersedia, Program Dihentikan!")