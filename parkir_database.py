class Database:
    def __init__(self):
        self.catatan_parkir = {}

    def tambah_catatan_parkir(self, nama, jenis_kendaraan, waktu_mulai):
        self.catatan_parkir[nama] = {
            'jenis_kendaraan': jenis_kendaraan,
            'waktu_mulai': waktu_mulai,
            'waktu_akhir': None,
            'biaya': None
        }

    def akhiri_catatan_parkir(self, nama, waktu_akhir):
        if nama in self.catatan_parkir and self.catatan_parkir[nama]['waktu_akhir'] is None:
            self.catatan_parkir[nama]['waktu_akhir'] = waktu_akhir
            return self.catatan_parkir[nama]
        return None

    def perbarui_biaya_parkir(self, nama, biaya):
        if nama in self.catatan_parkir:
            self.catatan_parkir[nama]['biaya'] = biaya

    def dapatkan_catatan_parkir(self, nama):
        return self.catatan_parkir.get(nama, None)
