import csv
import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 86
garis = "=" * 86

def lihat_daftar():
    print("\n")
    print("Daftar Pengadaan Barang".center(86))
    print("Tahun 2024".upper().center(86))
    print(baris.center(86))
    print("Gaikindo".upper().center(86))
    print("")

    file_path = 'data_pengadaan.csv'
    total_anggaran = 0
    data_pengadaan = []

    def jalankan_modul(file_name):
        with open(file_name) as f:
            kode = f.read()
        exec(kode)

    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data_pengadaan = list(reader)
        
        if not data_pengadaan:
            print("Belum Ada Data Pengadaan!")
            print("")
            kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
            if kembali == "y" or kembali == "Y" :
                jalankan_modul("Dashboard.py")
            elif kembali == "t" or kembali == "T" :
                quit("Baiklah, Sampai Jumpa Lagi!")
            else :
                quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")
            return

        print(f"{'No.':<5}{'Nama Barang/Jasa':<40}{'Jumlah':<10}{'Harga Satuan':<20}{'Total Harga':<20}")
        print(garis.center(86))
        for i, row in enumerate(data_pengadaan, start=1):
            nama_barang, jumlah, harga_satuan, total_harga = row
            print(f"{i:<5}{nama_barang:<40}{jumlah:<10}{harga_satuan:<20}{total_harga:<20}")
            total_anggaran += float(total_harga)

        print(baris.center(86))
        print(f"Total Anggaran : Rp. {total_anggaran:.2f}\n")

    except FileNotFoundError:
        print("Belum Ada Data Pengadaan!")
        return

    def hapus_barang():
        try:
            pilihan = input("Masukkan Nomor Barang Yang Ingin Dihapus (Pisahkan Dengan Koma Jika Lebih Dari Satu) : ")
            nomor_hapus = [int(n.strip()) for n in pilihan.split(",")]

            if any(n <= 0 or n > len(data_pengadaan) for n in nomor_hapus):
                print("Nomor Yang Dimasukkan Tidak Valid!")
                return

            konfirmasi = input("Apakah Anda Yakin Ingin Menghapus Barang Ini? [y,t] : ")
            if konfirmasi.lower() != "y":
                print("Penghapusan Dibatalkan")
                print("")
                kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
                if kembali == "y" or kembali == "Y":
                    jalankan_modul("Dashboard.py")
                elif kembali == "t" or kembali == "T":
                    quit("Baiklah, Sampai Jumpa Lagi!")
                else:
                    quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")
                return

            for i in sorted(nomor_hapus, reverse=True):
                data_pengadaan.pop(i - 1)

            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_pengadaan)

            print("Barang Berhasil Dihapus!")
            print("")
            kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
            if kembali == "y" or kembali == "Y":
                jalankan_modul("Dashboard.py")
            elif kembali == "t" or kembali == "T":
                quit("Baiklah, Sampai Jumpa Lagi!")
            else:
                quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")

        except ValueError:
            print("Input Tidak Valid! Pastikan Anda Hanya Memasukkan Angka Sesuai Dengan Barang Yang Tersedia!")

    hapus = input("Ingin Menghapus Barang Dari Daftar ? [y,t] : ")
    if hapus == "y" or hapus == "Y":
        hapus_barang()
    elif hapus == "t" or hapus == "T":
        print("")
        kembali = input("Ingin Kembali Ke Menu Utama ? [y,t] : ")
        if kembali == "y" or kembali == "Y":
            jalankan_modul("Dashboard.py")
        elif kembali == "t" or kembali == "T":
            quit("Baiklah, Sampai Jumpa Lagi!")
        else:
            quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")
    else:
        quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")

lihat_daftar()
