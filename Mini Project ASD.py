class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class SistemPemesanan:
    def __init__(self):
        self.menu = {
            1: Menu("Nasi Goreng", 15000),
            2: Menu("Mie Goreng", 12000),
            3: Menu("Ayam Goreng", 20000),
            4: Menu("Soto Ayam", 18000),
            5: Menu("Es Teh", 5000)
        }
        self.pesanan = {}

    def tampilkan_menu(self):
        print("Menu Makanan:")
        for key, item in self.menu.items():
            print(f"{key}. {item.nama}: Rp{item.harga}")

    def pesan_makanan(self, nomor_menu, jumlah):
        if nomor_menu in self.menu:
            if nomor_menu in self.pesanan:
                self.pesanan[nomor_menu] += jumlah
            else:
                self.pesanan[nomor_menu] = jumlah
            print(f"{jumlah} {self.menu[nomor_menu].nama} berhasil ditambahkan ke pesanan.")
        else:
            print("Menu tidak tersedia.")

    def hapus_pesanan(self, nomor_menu, jumlah):
        if nomor_menu in self.pesanan:
            if self.pesanan[nomor_menu] >= jumlah:
                self.pesanan[nomor_menu] -= jumlah
                print(f"{jumlah} {self.menu[nomor_menu].nama} berhasil dihapus dari pesanan.")
            else:
                print("Jumlah pesanan tidak mencukupi.")
        else:
            print("Menu tidak ditemukan dalam pesanan.")

    def tampilkan_pesanan(self):
        if self.pesanan:
            print("Pesanan Anda:")
            total_harga = 0
            for nomor_menu, jumlah in self.pesanan.items():
                menu = self.menu[nomor_menu]
                subtotal = menu.harga * jumlah
                total_harga += subtotal
                print(f"{menu.nama}: {jumlah} x Rp{menu.harga} = Rp{subtotal}")
            print(f"Total: Rp{total_harga}")
        else:
            print("Pesanan Anda kosong.")


# Program Utama
sistem_pemesanan = SistemPemesanan()

while True:
    print("\nPilih menu:")
    print("1. Tampilkan Menu")
    print("2. Pesan Makanan")
    print("3. Hapus Pesanan")
    print("4. Tampilkan Pesanan")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        sistem_pemesanan.tampilkan_menu()
    elif pilihan == '2':
        nomor_menu = int(input("Masukkan nomor menu: "))
        jumlah = int(input("Masukkan jumlah: "))
        sistem_pemesanan.pesan_makanan(nomor_menu, jumlah)
    elif pilihan == '3':
        nomor_menu = int(input("Masukkan nomor menu: "))
        jumlah = int(input("Masukkan jumlah: "))
        sistem_pemesanan.hapus_pesanan(nomor_menu, jumlah)
    elif pilihan == '4':
        sistem_pemesanan.tampilkan_pesanan()
    elif pilihan == '5':
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")