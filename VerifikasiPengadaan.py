import csv
import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 86
garis = "=" * 86

def verifikasi_pengadaan():
    print("\n\n")
    print("Verifikasi Dan Persetujuan Pengadaan Barang".center(86))
    print("Tahun 2024".upper().center(86))
    print(baris.center(86))
    print("Gaikindo".upper().center(86))
    print("")

    try:
        
        with open('data_pengadaan.csv', mode='r') as file:
            reader = csv.reader(file)
            pengadaan_list = list(reader)

        if not pengadaan_list:
            print("Belum Ada Data Pengadaan Untuk Diverifikasi!")
            return

        print(f"{'No':<5}{'Nama Barang/Jasa':<40}{'Jumlah':<10}{'Harga Satuan':<20}{'Total Harga':<20}")
        print(garis.center(86))
        for i, row in enumerate(pengadaan_list, start=1):
            nama_barang, jumlah, harga_satuan, total_harga = row
            print(f"{i:<5}{nama_barang:<40}{jumlah:<10}{harga_satuan:<20}{total_harga:<20}")

        pilihan = input("\nMasukkan nomor barang yang ingin disetujui (pisahkan dengan koma jika lebih dari satu): ")
        nomor_dipilih = [int(n.strip()) for n in pilihan.split(",")]

        if any(n <= 0 or n > len(pengadaan_list) for n in nomor_dipilih):
            print("Nomor barang tidak valid.")
            return

        disetujui_list = []
        sisa_pengadaan_list = []

        for i, row in enumerate(pengadaan_list, start=1):
            if i in nomor_dipilih:
                nama_barang, jumlah, harga_satuan, total_harga = row
                jumlah_awal = int(jumlah)
                jumlah_setujui = int(input(f"Masukkan jumlah yang disetujui untuk '{nama_barang}' (maks {jumlah_awal}): "))

                if jumlah_setujui <= 0 or jumlah_setujui > jumlah_awal:
                    print(f"Jumlah yang dimasukkan tidak valid untuk '{nama_barang}'.")
                    sisa_pengadaan_list.append(row)
                else:
                    
                    disetujui_list.append([nama_barang, jumlah_setujui, harga_satuan, int(harga_satuan) * jumlah_setujui, "Disetujui"])

                    sisa_jumlah = jumlah_awal - jumlah_setujui
                    if sisa_jumlah > 0:
                        sisa_pengadaan_list.append([nama_barang, sisa_jumlah, harga_satuan, int(harga_satuan) * sisa_jumlah])
            else:
                sisa_pengadaan_list.append(row)

        if disetujui_list:
            with open('pesanan_pembelian.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nama Barang/Jasa", "Jumlah", "Harga Satuan", "Total Harga", "Status"])
                writer.writerows(disetujui_list)

            print("\nBarang yang dipilih telah disetujui dan dicatat sebagai Pesanan Pembelian (PO).")

        with open('data_pengadaan.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(sisa_pengadaan_list)

        print("\nData pengadaan telah diperbarui.")

    except FileNotFoundError:
        print("File Data Pengadaan Tidak Ditemukan!")
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

verifikasi_pengadaan()
