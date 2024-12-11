import csv
import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 105
garis = "=" * 105

def terima_barang():
    print("\n\n")
    print("Penerimaan Barang Atau Jasa".center(105))
    print("Tahun 2024".upper().center(105))
    print(baris.center(105))
    print("Gaikindo".upper().center(105))
    print("")

    file_pesanan = 'pesanan_pembelian.csv'
    file_pengadaan = 'data_pengadaan.csv'

    try:
        with open(file_pesanan, mode='r') as file:
            reader = csv.reader(file)
            pesanan_list = list(reader)

        if len(pesanan_list) <= 1:
            print("Belum ada pesanan pembelian untuk diterima.")
            return

        print(f"{'No':<5}{'Nama Barang/Jasa':<40}{'Jumlah':<10}{'Harga Satuan':<20}{'Total Harga':<20}{'Status':<15}")
        print(garis.center(105))

        for i, row in enumerate(pesanan_list[1:], start=1):
            print(f"{i:<5}{row[0]:<40}{row[1]:<10}{row[2]:<20}{row[3]:<20}{row[4]:<15}")

        pilihan = input("\nMasukkan nomor pesanan yang diterima (pisahkan dengan koma jika lebih dari satu): ")
        nomor_diterima = [int(n.strip()) for n in pilihan.split(",")]

        if any(n <= 0 or n >= len(pesanan_list) for n in nomor_diterima):
            print("Nomor pesanan tidak valid.")
            return

        diterima_list = []
        tidak_diterima_list = []

        for i, row in enumerate(pesanan_list[1:], start=1):
            if i in nomor_diterima:
                row[4] = "Diterima"
                diterima_list.append(row)
            else:
                tidak_diterima_list.append(row)

        with open(file_pesanan, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pesanan_list[0])
            writer.writerows(diterima_list)

        if tidak_diterima_list:
            with open(file_pengadaan, mode='a', newline='') as file:
                writer = csv.writer(file)
                for row in tidak_diterima_list:
                    writer.writerow(row[:-1])

        print("\nPesanan yang dipilih telah diperbarui menjadi 'Diterima'.")
        print("Pesanan yang tidak dipilih dikembalikan ke daftar pengadaan.\n")

    except FileNotFoundError:
        print("File pesanan pembelian tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Pastikan hanya memasukkan angka sesuai nomor pesanan.")

    def jalankan_modul(file_name):
        with open(file_name) as f:
            kode = f.read()
        exec(kode)

    kembali = input("Ingin Kembali Ke Menu Utama? [y,t]: ")
    if kembali.lower() == "y":
        jalankan_modul("Dashboard.py")
    elif kembali.lower() == "t":
        quit("Baiklah, Sampai Jumpa Lagi!")
    else:
        quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")

terima_barang()
