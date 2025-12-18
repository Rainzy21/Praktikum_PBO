from abc import ABC, abstractmethod

# Parent Class abstrak
class Notifikasi(ABC):
    @abstractmethod
    def kirim(self, pesan):
        raise NotImplementedError("Method kirim() harus diimplementasikan di class turunan")

# Child Class: Email
class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")

# Child Class: SMS
class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")

# Child Class: PushNotif
class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

# Bagian utama program
if __name__ == "__main__":
    # Membuat list objek dari setiap kanal
    daftar_notif = [
        Email(),
        SMS(),
        PushNotif()
    ]

    # Pesan yang akan dikirim
    pesan = "Diskon Spesial! Hanya untuk Anda!"

    # Loop polymorphism
    for notif in daftar_notif:
        notif.kirim(pesan)