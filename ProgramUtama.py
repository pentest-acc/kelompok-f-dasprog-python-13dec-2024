garis = "=" * 40

print("")
print("Selamat Datang".upper().center(40))
print("Gaikindo Bekasi Utara".center(40))
print(garis.center(40))
print("")
login = input("Apakah Anda Ingin Login ? [y,t] : ")
if login == "y" or login == "Y" :
   import LoginForm
elif login == "t" or login == "T" :
   quit("Baiklah, Sampai Jumpa Lagi!")
else :
   quit("Anda Menginput Tidak Sesuai Pilihan Huruf Yang Tersedia, Program Dihentikan!")