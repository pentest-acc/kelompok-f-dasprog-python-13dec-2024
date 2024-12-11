import csv
import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 100
garis = "=" * 100

def lihat_po():
    print("")
    print("")
    print("Daftar Pemesanan Pembelian (PO)".center(100))
    print("Tahun 2024".upper().center(100))
    print(baris.center(100))
    print("Gaikindo".upper().center(100))
    print("")
    
    try:
        with open('pesanan_pembelian.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            print(f"{'Nama Barang/Jasa':<40}{'Jumlah':<10}{'Harga Satuan':<20}{'Total Harga':<20}{'Status':<15}")
            print(garis.center(100))
            for row in reader:
                nama_barang, jumlah, harga_satuan, total_harga, status = row
                print(f"{nama_barang:<40}{jumlah:<10}{harga_satuan:<20}{total_harga:<20}{status:<15}")
    except FileNotFoundError:
        print("Belum Ada Pesanan Pembelian (PO) Yang Dibuat")

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

lihat_po()