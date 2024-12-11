import csv
import sys
from datetime import datetime

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 105
garis = "=" * 105

def bayar_vendor():
    print("\n\n")
    print("Pembayaran Ke Vendor".center(105))
    print("Tahun 2024".upper().center(105))
    print(baris.center(105))
    print("Gaikindo".upper().center(105))
    print("")

    try:
        with open('pesanan_pembelian.csv', mode='r') as file:
            reader = csv.reader(file)
            pesanan_list = list(reader)

        if len(pesanan_list) <= 1:
            print("Belum ada pesanan yang dapat dibayar.")
            return

        print(f"{'No':<5}{'Nama Barang/Jasa':<40}{'Jumlah':<10}{'Harga Satuan':<20}{'Total Harga':<20}{'Status':<15}")
        print(garis.center(105))
        for i, row in enumerate(pesanan_list[1:], start=1):
            print(f"{i:<5}{row[0]:<40}{row[1]:<10}{row[2]:<20}{row[3]:<20}{row[4]:<15}")

        pilihan = input("\nMasukkan nomor pesanan yang akan dibayar (pisahkan dengan koma jika lebih dari satu): ")
        nomor_dipilih = [int(n.strip()) for n in pilihan.split(",")]

        transaksi_berhasil = []
        for no_pesanan in nomor_dipilih:
            if 1 <= no_pesanan < len(pesanan_list):
                if pesanan_list[no_pesanan][4] == "Diterima":
                    pesanan_list[no_pesanan][4] = "Dibayar"
                    transaksi_berhasil.append(pesanan_list[no_pesanan])
                else:
                    print(f"Pesanan nomor {no_pesanan} belum diterima, tidak dapat diproses untuk pembayaran.")
            else:
                print(f"Nomor pesanan {no_pesanan} tidak valid.")

        with open('pesanan_pembelian.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(pesanan_list)

        if transaksi_berhasil:
            with open('history_transaksi.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nama Barang/Jasa", "Jumlah", "Harga Satuan", "Total Harga", "Status", "Tanggal Pembayaran"])
                tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for transaksi in transaksi_berhasil:
                    writer.writerow(transaksi + [tanggal])

            print("\nPembayaran telah dilakukan ke vendor dan dicatat dalam riwayat transaksi.")

    except FileNotFoundError:
        print("File pesanan pembelian tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan hanya memasukkan angka yang benar.")

    def jalankan_modul(file_name):
        with open(file_name) as f:
            kode = f.read()
        exec(kode)

    kembali = input("\nIngin Kembali Ke Menu Utama? [y,t]: ")
    if kembali.lower() == "y":
        jalankan_modul("Dashboard.py")
    elif kembali.lower() == "t":
        quit("Baiklah, Sampai Jumpa Lagi!")
    else:
        quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")

bayar_vendor()
