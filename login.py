import csv

# Tahap Pemilihan Login atau Register
Ngulang = False
mainloop = True
while mainloop == True:
    if Ngulang == False:
        Status_Akun = input("Apakah anda sudah mempunyai akun? (Sudah/Belum) ")
    if Status_Akun != "Sudah" and Status_Akun != "sudah" and Status_Akun != "Belum" and Status_Akun != "belum":
        while Status_Akun != "Sudah" and Status_Akun != "sudah" and Status_Akun != "Belum" and Status_Akun != "belum":
            print("Masukkan perintah yang diminta! (Sudah/Belum) ")
            Status_Akun = input("Apakah anda sudah mempunyai akun? (Sudah/Belum) ")
    if Status_Akun == "Sudah" or Status_Akun == "sudah":
        Mau_Login = True
        Salah_login = 0
        if Mau_Login == True:
            Login = False
            while Login == False and Mau_Login == True:
                Nama = input("Masukkan username: ")
                Password = input("Masukkan password: ")
                Opsi_Salah_Login = "Belum Terdefinisi"
                with open('user.csv', mode='r') as file:
                    csvFile = csv.reader(file)
                    for lines in csvFile:
                        if Nama in lines[0] and Password in lines[1]:
                            Login = True  # Berhasil Login
                            print("Anda berhasil masuk!")
                            # Nanti disini bakal dimulai perkodingan semua - muanya, tenang aja ini full satu kodingan bisa dijadiin fungsi kok

                    if Login != True:
                        print("Username atau Password yang anda masukan salah!")
                        # Salah Login 3 kali, dikasih opsi mau daftar atau exit aja
                        Salah_login += 1
                        if Salah_login == 3:  # Salah Login 3 Kali
                            while Opsi_Salah_Login != "Ya" and Opsi_Salah_Login != "ya" and Opsi_Salah_Login != "Tidak" and Opsi_Salah_Login != "tidak":
                                Opsi_Salah_Login = input(
                                    "Anda telah mencapai batas maksimum login! Periksa kembali Username dan Password anda! Atau anda ingin membuat akun baru? (Ya/Tidak)")

                                # Mau buat akun baru
                                if Opsi_Salah_Login == "Ya" or Opsi_Salah_Login == "ya":
                                    Status_Akun = "Belum"
                                    Mau_Login = False
                                    Ngulang = True

                                # Gamau buat akun baru
                                elif Opsi_Salah_Login == "Tidak" or Opsi_Salah_Login == "tidak":
                                    print("Selamat Tinggal!")

                                    # Pemberhentian loop
                                    mainloop = False
                                    Login = 0
                                    Mau_Login = 0
                                    break

                                # Wrong input
                                else:
                                    print("Masukkan perintah yang diminta! (Ya/Tidak)")
                            break

                            # Register
    elif Status_Akun == "Belum" or Status_Akun == "belum":
        Mau_Login = False
        Register_Berhasil = False
        Nama_Sama = False

        # Register dimulai
        while Register_Berhasil == False:
            print("Buat akun baru!")
            Nama = input("Masukkan username baru: ")
            Password = input("Masukkan password baru: ")
            with open('user.csv', mode='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    if Nama in lines[0]:
                        Nama_Sama = True

            # Nama Sudah Terdaftar
            if Nama_Sama == True:
                Register_Berhasil = False
                Nama_Sama = False
                print("Username sudah digunakan")

            # Register Berhasil
            else:
                Register_Berhasil = True
                Akun_Baru = [Nama, Password]
                with open('user.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(Akun_Baru)
                    print("Akun berhasil terdaftar!")
                    Register_Berhasil = True
                    Status_Akun = 0
                    Ngulang = False
