from models.kontak import Kontak

if __name__ == "__main__":
    daftar_kontak = []

    kontak1 = Kontak("Hervino", "08123456789")
    kontak2 = Kontak("Islami", "082233445566")
    kontak3 = Kontak("Fasha", "083312345678")

    daftar_kontak.extend([kontak1, kontak2, kontak3])

    for kontak in daftar_kontak:
        kontak.tampilkan_info()
