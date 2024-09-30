from parkir_database import Database
from datetime import datetime

class AplikasiParkir:
    def __init__(self):
        self.db = Database()

    def mulai_parkir(self, nama, jenis_kendaraan):
        waktu_mulai = datetime.now()
        self.db.tambah_catatan_parkir(nama, jenis_kendaraan, waktu_mulai)
        print(f"Parkir dimulai untuk {nama} dengan jenis kendaraan {jenis_kendaraan} pada {waktu_mulai}")

    def akhiri_parkir(self, nama):
        waktu_akhir = datetime.now()
        catatan_parkir = self.db.akhiri_catatan_parkir(nama, waktu_akhir)
        if catatan_parkir:
            durasi = (catatan_parkir['waktu_akhir'] - catatan_parkir['waktu_mulai']).total_seconds() / 3600
            tarif = 5.0 
            biaya = durasi * tarif
            self.db.perbarui_biaya_parkir(nama, biaya)
            print(f"Parkir diakhiri untuk {nama} pada {waktu_akhir}")
            print(f"Total durasi: {durasi:.2f} jam, Biaya: Rp{biaya:.2f}")
        else:
            print("Tidak ditemukan catatan parkir aktif untuk pengguna tersebut.")

    def hitung_biaya(self, nama):
        catatan_parkir = self.db.dapatkan_catatan_parkir(nama)
        if catatan_parkir['waktu_akhir']:
            print(f"Biaya parkir untuk {nama} adalah Rp{catatan_parkir['biaya']:.2f}")
        else:
            print("Catatan parkir tidak ditemukan atau parkir belum diakhiri.")

    def menu_utama(self):
        while True:
            print("\nMenu Sistem Parkir")
            print("1. Mulai Parkir")
            print("2. Akhiri Parkir")
            print("3. Hitung Biaya")
            print("4. Keluar")
            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                nama = input("Masukkan nama Anda: ")
                jenis_kendaraan = input("Masukkan jenis kendaraan: ")
                self.mulai_parkir(nama, jenis_kendaraan)
            elif pilihan == '2':
                nama = input("Masukkan nama Anda: ")
                self.akhiri_parkir(nama)
            elif pilihan == '3':
                nama = input("Masukkan nama Anda: ")
                self.hitung_biaya(nama)
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app = AplikasiParkir()
    app.menu_utama()
