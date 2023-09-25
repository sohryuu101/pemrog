import csv
import string


# Ini enkripsi dan dekripsi password
def SULAP(text, key, characters=string.ascii_lowercase, decrypt=False, shift_type="right"):
    if key < 0:
        print("K tidak valid (tidak boleh negatif)")
        return None
    n = len(characters)
    if decrypt == True:
        key = n - key
    if shift_type == "left":
        key = -key
    rumus_sulap = str.maketrans(characters, characters[key:] + characters[:key])
    tersulap = text.translate(rumus_sulap)
    return tersulap


# Tahap Pemilihan Login atau Register
Mainkan_Musik = False  # ini nanti jadi command buat jalanin sqlnya
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
                Opsi_Salah_Login = "Undefined"
                with open('user.csv', mode='r') as file:
                    csvFile = csv.reader(file)
                    for lines in csvFile:
                        dekripsi = SULAP(lines[1], 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                         decrypt=True, shift_type="left")
                        if Nama in lines[0] and dekripsi == Password:
                            Login = True  # Berhasil Login
                            print("Anda berhasil masuk!")
                            Mainkan_Musik = True
                            # Nanti disini bakal dimulai perkodingan semua - muanya, tenang aja ini full satu kodingan bisa dijadiin fungsi kok

                            # Pemberhentian loop
                            mainloop = False
                            Login = "Undefined"
                            Mau_Login = "Undefined"
                            Status_Akun = "Undefined"

                    if Login == False:
                        Salah_login += 1
                        print(f"Username atau Password yang anda masukan salah! ({Salah_login}/3)")
                        # Salah Login 3 kali, dikasih opsi mau daftar atau exit aja
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
                enkripsi = SULAP(Password, 3, characters=(string.ascii_lowercase + string.ascii_uppercase),
                                 decrypt=False, shift_type="left")
                Register_Berhasil = True
                Akun_Baru = [Nama, enkripsi]
                with open('user.csv', 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(Akun_Baru)
                    print("Akun berhasil terdaftar!")

                    # Pemberhentian Loop
                    Register_Berhasil = True
                    Status_Akun = "Undefined"
                    Ngulang = False
                    First_Time = False

