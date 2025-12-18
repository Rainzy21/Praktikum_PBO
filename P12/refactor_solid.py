from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass
    
class INotificationService(ABC):
    @abstractmethod
    def send(self, order: Order):
        pass
    
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Kartu Kredit.")
        return True
    
class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Mengirim email konfirmasi ke {order.customer_name}.")
        
class CheckoutService:
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        self.payment_processor = payment_processor
        self.notifier = notifier
        
    def run_checkout(self, order: Order):
        print(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")
        payment_success = self.payment_processor.process(order)
        
        if payment_success:
            order.status = "paid"
            self.notifier.send(order)
            print("Checkout Sukses. Status pesanan: PAID.")
            return True
        else:
            print("Pembayaran gagal. Transaksi dibatalkan.")
            return False

# --- Main Program ---
andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

cc_processor = CreditCardProcessor()
checkout_cc = CheckoutService(payment_processor=cc_processor, notifier=email_service)
print("--- Skenario 1: Credit Card ---")
checkout_cc.run_checkout(andi_order)

class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Qris.")
        return True
    
budi_order = Order("Budi", 100000)
qris_processor = QrisProcessor()

checkout_qris = CheckoutService(payment_processor=qris_processor, notifier=email_service)
print("\n--- Skenario 2: Pembuktian OCP (QRIS) ---")
checkout_qris.run_checkout(budi_order)