import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-"*40
garis = "="*40

print("")
print("")
print("Program Pengadaan Barang".upper().center(40))
print("Admin Gaikindo".center(40))
print("Tahun 2024".center(40))
print(garis.center(40))
print("")
print("Kelompok F".center(40))
print("")
anggota = ["Ketua     : ",
           "Anggota   : ",
           "Anggota   : ",]

nama = ["Stephen Baldwin",
        "Muhammad Zaid Dhiyaulhaq",
        "Ilham Maulana",]

nim = ["(15241024)",
       "(15240021)",
       "(15241002)",]

for jabatan, identitas, nomor in zip(anggota,nama,nim) :
    print(jabatan,identitas,nomor)

print("")
kelompok = ["1) Nama     :",
            "   Nim      :",
            "   Kelas    :",
            "   Prodi    :",
            "   Jabatan  :",
            "   Tugas    :",
            "           ",
            "2) Nama     :",
            "   Nim      :",
            "   Kelas    :",
            "   Prodi    :",
            "   Jabatan  :",
            "   Tugas    :",
            "           ",
            "3) Nama     :",
            "   Nim      :",
            "   Kelas    :",
            "   Prodi    :",
            "   Jabatan  :",
            "   Tugas    :",]

kelompok_data = ["Stephen Baldwin",
                 "15241024       ",
                 "15.1C.05       ",
                 "Informatika    ",
                 "Ketua          ",
                 "Memperbaiki Program dan Membuat PowerPoint",
                 "               ",
                 "Muhammad Zaid Dhiyaulhaq",
                 "15240021       ",
                 "15.1C.05       ",
                 "Informatika    ",
                 "Anggota        ",
                 "Membuat Proposal",
                 "               ",
                 "Ilham Maulana  ",
                 "19241002       ",
                 "15.1C.05       ",
                 "Informatika    ",
                 "Anggota        ",
                 "Membuat Program",]

def jalankan_modul1(file_name):
    with open(file_name) as f:
        kode = f.read()
    exec(kode)

team = input("Ingin Tampilkan Data Kelompok ? [y,t] : ")
print("")
if team == "y" or team == "Y" :
   for kelompok, data in zip(kelompok, kelompok_data) :
       print(kelompok, data)
elif team == "t" or team == "T" :
    jalankan_modul1("Dashboard.py")
else :
    quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")
print("")
kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
if kembali == "y" or kembali == "Y" :
    jalankan_modul1("Dashboard.py")
elif kembali == "t" or kembali == "T" :
    quit("Baiklah, Sampai Jumpa Lagi!")
else :
    quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")