from abc import ABC, abstractmethod
import logging
from models import Product, CartItem
from typing import List

LOGGER = logging.getLogger('SERVICES')

# --- INTERFACE PEMBAYARAN (Diperlukan untuk DIP/OCP) ---
class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass

# --- IMPLEMENTASI 1: TUNAI ---
class CashPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        LOGGER.info(f"Menerima TUNAI sejumlah: Rp{amount:,.0f}")
        return True

# --- IMPLEMENTASI 2: DEBIT CARD (JAWABAN LATIHAN MANDIRI) ---
class DebitCardPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        # Simulasi logika kartu debit
        LOGGER.info("System: Menghubungkan ke Gateway Bank...")
        LOGGER.info(f"Bank: Memproses pemotongan saldo sebesar Rp{amount:,.0f}")
        LOGGER.info("Bank: Transaksi APPROVED.")
        return True

# --- SERVICE KERANJANG BELANJA ---
class ShoppingCart:
    """Mengelola item, kuantitas, dan total harga pesanan (SRP)."""
    
    def __init__(self):
        self._items: dict[str, CartItem] = {}

    def add_item(self, product: Product, quantity: int = 1):
        if product.id in self._items:
            self._items[product.id].quantity += quantity
        else:
            self._items[product.id] = CartItem(product=product, quantity=quantity)
        
        LOGGER.info(f"Added {quantity}x {product.name} to cart.")

    def get_items(self) -> List[CartItem]:
        return list(self._items.values())

    @property
    def total_price(self) -> float:
        return sum(item.subtotal for item in self._items.values())