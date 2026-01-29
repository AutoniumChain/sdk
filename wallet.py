class Wallet:
    def __init__(self, private_key: str):
        self.private_key = private_key
        self.balance = 1.0  # mock balance

    def get_balance(self):
        return self.balance

    def send(self, to: str, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            print(f"[WALLET] Sent {amount} to {to}")
            return True
        else:
            print("[WALLET] Insufficient balance")
            return False
