# Sistem Kasir CLI (Point of Sale) - Penerapan SOLID & Dependency Injection

Proyek ini adalah simulasi aplikasi Point of Sale (POS) sederhana berbasis Command Line Interface (CLI). Aplikasi ini dibangun untuk mendemonstrasikan penerapan **Arsitektur Berlapis (Layered Architecture)** dan prinsip **Dependency Injection (DI)** dalam Pemrograman Berorientasi Objek.

## Arsitektur Proyek
Aplikasi ini memisahkan kode menjadi komponen-komponen yang berdiri sendiri (Decoupled Components) sesuai prinsip *Single Responsibility Principle*:

1.  **Models (`models.py`)**: Struktur data dasar (`Product`, `CartItem`).
2.  **Repository (`repositories.py`)**: Lapisan akses data (Simulasi Database Produk).
3.  **Services (`services.py`)**: Logika bisnis (Keranjang Belanja) dan Interface Pembayaran.
4.  **Orchestrator (`main_app.py`)**: Aplikasi utama yang merakit semua komponen menggunakan teknik *Dependency Injection*.

## Fitur Utama
* **Browsing Produk**: Melihat daftar produk beserta harga.
* **Shopping Cart**: Menambahkan barang ke keranjang dengan kuantitas tertentu.
* **Checkout System**: Menghitung total belanja.
* **Logging System**: Menggunakan library `logging` python untuk mencatat aktivitas sistem (bukan `print` biasa).
* **Flexible Payment (Challenge Completed)**: Mendukung pembayaran via:
    * 💵 Cash (Tunai)
    * 💳 Debit Card (Implementasi Challenge Mandiri)

## 🚀 Cara Menjalankan
Pastikan Python 3.x sudah terinstall di komputer Anda.

1.  Clone repository ini atau download filenya.
2.  Buka terminal di folder proyek.
3.  Jalankan perintah berikut:
    ```bash
    python main_app.py
    ```

## Jawaban Tugas Mandiri (Challenge)
Pada tugas mandiri, saya telah menerapkan **Open/Closed Principle** dengan cara:
1.  Membuat class `DebitCardPayment` di `services.py` yang mengimplementasikan `IPaymentProcessor`.
2.  Melakukan *Injection* class `DebitCardPayment` ke dalam `PosApp` melalui file `main_app.py` tanpa mengubah kode logika inti di dalam class `PosApp`.

---