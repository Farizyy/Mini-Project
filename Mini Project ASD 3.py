class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Menambahkan atribut prev untuk mengakses node sebelumnya

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current  # Menyimpan node sebelumnya

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node tidak ada.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node  # Menyimpan node sebelumnya dari new_node

    def delete_node(self, key):
        current = self.head

        if current is not None and current.data.name == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return

        prev = None
        while current is not None and current.data.name != key:
            prev = current
            current = current.next

        if current is None:
            print("Menu tidak ditemukan.")
            return

        prev.next = current.next
        if current.next:
            current.next.prev = prev
        current = None
        print(f"Menu '{key}' berhasil dihapus.")

    def delete_menu(self, menu_name):
        if self.head is None:
            print("Linked list kosong.")
            return

        # Jika menu yang ingin dihapus ada di head
        if self.head.data.name == menu_name:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            print(f"Menu '{menu_name}' berhasil dihapus.")
            return

        # Cari menu yang ingin dihapus
        current = self.head
        while current and current.data.name != menu_name:
            current = current.next

        # Jika menu ditemukan
        if current:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            print(f"Menu '{menu_name}' berhasil dihapus.")
        else:
            print(f"Menu '{menu_name}' tidak ditemukan.")

    def quick_sort(self, key='name', order='asc'):
        # Menggunakan algoritma Quick Sort untuk sorting
        def partition(start, end):
            pivot_value = end.data.price if key == 'price' else end.data.name
            i = start.prev

            current = start
            while current != end:
                j = current.next
                current_value = current.data.price if key == 'price' else current.data.name
                if (order == 'asc' and current_value <= pivot_value) or (order == 'desc' and current_value >= pivot_value):
                    i = start if i is None else i.next
                    i.data, current.data = current.data, i.data
                current = j

            i = start if i is None else i.next
            i.data, end.data = end.data, i.data
            return i
        

        def quick_sort_util(start, end):
            if end is not None and start is not None and start != end and start != end.next:
                pivot = partition(start, end)
                quick_sort_util(start, pivot.prev)
                quick_sort_util(pivot.next, end)

        quick_sort_util(self.head, self.get_tail())

    def get_tail(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current

class OrderSystem:
    def __init__(self):
        self.menu_list = LinkedList()
        self.orders = {}

        # Menambahkan menu ke linked list
        self.menu_list.append(Menu("Nasi Goreng", 15000))
        self.menu_list.append(Menu("Mie Goreng", 12000))
        self.menu_list.append(Menu("Ayam Goreng", 20000))
        self.menu_list.append(Menu("Soto Ayam", 18000))
        self.menu_list.append(Menu("Es Teh", 5000))

    def show_menu(self):
        print("Menu Makanan:")
        current = self.menu_list.head
        while current:
            print(f"{current.data.name}: Rp{current.data.price}")
            current = current.next

    def place_order(self, menu_name, quantity):
        current = self.menu_list.head
        found = False
        while current:
            if current.data.name.lower() == menu_name.lower():
                found = True
                if current.data.name in self.orders:
                    self.orders[current.data.name] += quantity
                else:
                    self.orders[current.data.name] = quantity
                print(f"{quantity} {current.data.name} berhasil ditambahkan ke pesanan.")
                break
            current = current.next
        if not found:
            print("Menu tidak tersedia.")

    def remove_order(self, menu_name, quantity):
        if menu_name in self.orders:
            if self.orders[menu_name] >= quantity:
                self.orders[menu_name] -= quantity
                print(f"{quantity} {menu_name} berhasil dihapus dari pesanan.")
            else:
                print("Jumlah pesanan tidak mencukupi.")
        else:
            print("Menu tidak ditemukan dalam pesanan.")

    def add_menu_at_beginning(self, name, price):
        new_menu = Menu(name, price)
        self.menu_list.prepend(new_menu)
        print(f"Menu '{name}' berhasil ditambahkan di awal.")

    def add_menu_at_end(self, name, price):
        new_menu = Menu(name, price)
        self.menu_list.append(new_menu)
        print(f"Menu '{name}' berhasil ditambahkan di akhir.")

    def add_menu_after(self, prev_menu_name, name, price):
        current = self.menu_list.head
        while current:
            if current.data.name.lower() == prev_menu_name.lower():
                new_menu = Menu(name, price)
                self.menu_list.insert_after(current, new_menu)
                print(f"Menu '{name}' berhasil ditambahkan setelah '{prev_menu_name}'.")
                return
            current = current.next
        print(f"Menu '{prev_menu_name}' tidak ditemukan.")

    def show_order(self):
        print("Pesanan Anda:")
        for menu_name, quantity in self.orders.items():
            print(f"{menu_name}: {quantity}")

    def delete_menu(self, menu_name):
        self.menu_list.delete_menu(menu_name)

    def main_loop(self):
        while True:
            print("\nPilih menu:")
            print("1. Tampilkan Menu")
            print("2. Pesan Makanan")
            print("3. Hapus Pesanan")
            print("4. Tampilkan Pesanan")
            print("5. Tambah Makanan")
            print("6. Hapus Makanan")
            print("7. Keluar")
            print("8. Sorting")

            choice = input("Masukkan pilihan: ")

            if choice == '1':
                self.show_menu()
            elif choice == '2':
                menu_name = input("Masukkan nama menu: ")
                quantity = input("Masukkan jumlah: ")
                if quantity.isdigit():  # Memeriksa apakah input hanya terdiri dari angka
                    self.place_order(menu_name, int(quantity))
                else:
                    print("Jumlah harus berupa angka.")
            elif choice == '3':
                menu_name = input("Masukkan nama menu: ")
                quantity = input("Masukkan jumlah: ")
                if quantity.isdigit():
                    self.remove_order(menu_name, int(quantity))
                else:
                    print("Jumlah harus berupa angka.")
            elif choice == '4':
                self.show_order()
            elif choice == '5':
                new_name = input("Masukkan nama makanan baru: ")
                price_input = input("Masukkan harga makanan baru: ")
                if price_input.isdigit():
                    new_price = int(price_input)
                    print("Pilihan: ")
                    print("1. Tambah di Awal")
                    print("2. Tambah di Akhir")
                    print("3. Tambah di Tengah")
                    option = input("Masukkan pilihan: ")
                    if option == '1':
                        self.add_menu_at_beginning(new_name, new_price)
                    elif option == '2':
                        self.add_menu_at_end(new_name, new_price)
                    elif option == '3':
                        prev_menu = input("Masukkan nama menu setelah menu baru: ")
                        self.add_menu_after(prev_menu, new_name, new_price)
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print("Harga harus berupa angka.")
            elif choice == '6':
                menu_name = input("Masukkan nama makanan yang ingin dihapus: ")
                self.delete_menu(menu_name)
            elif choice == '7':
                print("Terima kasih telah menggunakan layanan kami.")
                break
            elif choice == '8':
                print("Pilihan Sorting: ")
                print("1. Nama Menu Ascending")
                print("2. Nama Menu Descending")
                print("3. Harga Menu Ascending")
                print("4. Harga Menu Descending")
                sort_option = input("Masukkan pilihan sorting: ")

                if sort_option == '1':
                    self.menu_list.quick_sort(key='name', order='asc')
                    print("Menu berhasil diurutkan berdasarkan nama secara ascending.")
                elif sort_option == '2':
                    self.menu_list.quick_sort(key='name', order='desc')
                    print("Menu berhasil diurutkan berdasarkan nama secara descending.")
                elif sort_option == '3':
                    self.menu_list.quick_sort(key='price', order='asc')
                    print("Menu berhasil diurutkan berdasarkan harga secara ascending.")
                elif sort_option == '4':
                    self.menu_list.quick_sort(key='price', order='desc')
                    print("Menu berhasil diurutkan berdasarkan harga secara descending.")
                else:
                    print("Pilihan sorting tidak valid.")
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    order_system = OrderSystem()
    order_system.main_loop()
