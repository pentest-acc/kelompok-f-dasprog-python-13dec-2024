import sys

if __name__ == "__main__":
    print("Anda Tidak Bisa Menjalankan Program Ini Secara Langsung, Harus Melalui ProgramUtama.py Terlebih Dahulu!")
    sys.exit()

baris = "-" * 40
garis = "=" * 40

print("")
print("")
print("Program Pengadaan Barang".upper().center(40))
print("Admin Gaikindo".center(40))
print(garis.center(40))

print("Login Form".upper().center(40))
user = input("Username  : ")
pw   = input("Password  : ")
if user== "gaikindo-kelompok-f" and pw== "ilham,zaid&stephen-_-" :
  print("")
  print(baris.center(40))
  print("")
  print("Login Berhasil,")
  menu = input("Apakah Anda Ingin Masuk Menu Utama ? [y,t] : ")
  if menu=="y" or menu=="Y" :
    import Dashboard
  elif menu == "t" or menu == "T" :
    quit("Baiklah, Sampai Jumpa Lagi!")
  else :
    quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")
else :
  quit("Maaf Username/Password Yang Anda Masukkan Salah!")