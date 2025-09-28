print ("Nama    : Ananta Hanif Fidzya Pratama")
print ("Kelas   : Sistem Informasi A'25")
print ("NIM     : 2509116023")
print ("Tugas   : Mini Project 2")

inventaris = [
    ["krimer", 10, "pcs"],
    ["skm", 60, "kaleng"],
    ["susu uht", 20, "dus"],
    ["kopi", 25, "pack"],
    ["evaporasi", 10, "dus" ],
    ["es batu", 50, "pack"]
]

def menu_boss():
    while True:
        print("=== Inventaris Stok Gudang ===")
        print("1. Lihat Stok ")
        print("2. Tambah Stok")
        print("3. Ubah Stok")
        print("4. Hapus Stok")
        print("5. Keluar")
        menu = input("Pilih menu (1-5): ").strip()

        if menu == "1":
            print("Daftar Stok Opname Bahan:")
            for i, item in enumerate(inventaris):
                print(i+1 , item[0] ,"- stok:", item[1] , item[2])

        elif menu == "2":
            try:
                nama = input("Nama Stok Bahan: ").lower()
                stok = int(input("Jumlah stok bahan?: "))
                jenis = input("Jenis stok bahan?: ")
                inventaris.append([nama, stok, jenis])
                print("Stok berhasil ditambahkan.")
            except ValueError:
                print("Jumlah harus angka!")

        elif menu == "3":
            for i, item in enumerate(inventaris):
                print(i+1 , item[0] ,"- stok:", item[1] , item[2])
            try:
                idx = int(input("Pilih bahan stok yang mau diubah: ")) - 1
                if 0 <= idx < len(inventaris):
                    nama_baru = input("Nama bahan yang mau di ubah?: ").lower()
                    stok_baru = int(input("Berapa stok bahan?: "))
                    jenis_baru = input("Jenis kemasannya?: ")
                    inventaris[idx][0] = nama_baru
                    inventaris[idx][1] = stok_baru
                    inventaris[idx][2] = jenis_baru
                    print("Stok berhasil diubah.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus angka!")

        elif menu == "4":
            for i, item in enumerate(inventaris):
                print(i+1 , item[0] ,"- stok:", item[1] , item[2])
            try:
                idx = int(input("Pilih bahan stok yang mau dihapus: ")) - 1
                if 0 <= idx < len(inventaris):
                    inventaris.pop(idx)
                    print("Stok berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus angka!")

        elif menu == "5":
            print("Keluar dari program.")
            break
        else:
            print("Menu tidak ditemukan.")

def menu_crew():
    while True:
        print("=== Inventaris Stok Gudang ===")
        print("1. Lihat Stok")
        print("2. Keluar")
        menu = input("Pilih menu (1-2): ").strip()

        if menu == "1":
            print("Daftar Stok Opname Bahan:")
            for i, item in enumerate(inventaris):
                print(i+1 , item[0] ,"- stok:", item[1] , item[2])
        elif menu == "2":
            print("Keluar dari program.")
            break
        else:
            print("Menu tidak ditemukan.")

def main():
    print("=== Sistem Login ===")
    print("1. Boss")
    print("2. Crew")
    role = input("Siapa Kamu? (boss/crew): ").strip().lower()

    if role == "boss":
        menu_boss()
    elif role == "crew":
        menu_crew()
    else:
        print("Role tidak dikenal, keluar program.")

main()
