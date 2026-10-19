class Kendaraan:
    def __init__(self, Tahun_Produksi, Nama_Merek, Nama_Model, Kategori_Bodi):
        self.tahun_produksi = Tahun_Produksi
        self.nama_merek = Nama_Merek
        self.nama_model = Nama_Model
        self.kategori_bodi = Kategori_Bodi

    def display_info(self):
        print(f"{self.tahun_produksi} {self.nama_merek} {self.nama_model}. berjenis bodi mobil {self.kategori_bodi} ")

input_tahun_produksi = int(input("masukkan tahun produksi merek anda: "))
input_merek = input("Masukkan Nama Merek Anda: ").lower()
input_model_merek = input("Masukkan nama Model mobil anda: ").lower()
input_jenis_bodi = input("Masukkan jenis model mobil anda: ").lower()

user_input = Kendaraan(input_tahun_produksi, input_merek, input_model_merek, input_jenis_bodi)
user_input.display_info()