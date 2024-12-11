import csv
import sys
import os

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 40
garis = "=" * 40

def tambah_pengadaan() :
    print("")
    print("")
    print("Program Tambah Data Pengadaan Barang".center(40))
    print("Tahun 2024".upper().center(40))
    print(baris.center(40))
    print("Gaikindo".upper().center(40))
    print("Masukkan Data Barang dibawah ini!".center(40))
    print("")

    data_pengadaan = []
    file_path = 'data_pengadaan.csv'

    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    data_pengadaan.append(row)

    nama_barang = input("Nama Barang/Jasa : ").strip()
    jumlah = int(input("Jumlah : "))
    barang_ditemukan = False
    harga_satuan = None

    for row in data_pengadaan:
        if row[0].lower() == nama_barang.lower():
            barang_ditemukan = True
            harga_satuan = int(row[2])
            print(f"Harga Satuan untuk '{nama_barang}' adalah: {harga_satuan}")
            break

    if not barang_ditemukan:
        harga_satuan = int(input("Harga Satuan : "))

    total_harga = jumlah * harga_satuan
    
    barang_diupdate = False
    for row in data_pengadaan:
        if row[0].lower() == nama_barang.lower() and int(row[2]) == harga_satuan:
            row[1] = str(int(row[1]) + jumlah)
            row[3] = str(int(row[1]) * harga_satuan)
            barang_diupdate = True
            break
    
    if not barang_diupdate:
        data_pengadaan.append([nama_barang, str(jumlah), str(harga_satuan), str(total_harga)])

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_pengadaan)
    
    print("Data Pengadaan Barang Berhasil Ditambahkan!")

    def jalankan_modul(file_name):
        with open(file_name) as f:
            kode = f.read()
        exec(kode)
    
    print("")
    kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
    if kembali == "y" or kembali == "Y" :
        jalankan_modul("Dashboard.py")
    elif kembali == "t" or kembali == "T" :
        quit("Baiklah, Sampai Jumpa Lagi!")
    else :
        quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")

tambah_pengadaan()