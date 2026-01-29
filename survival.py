import time
from config import SURVIVAL_PAYMENT_AMOUNT, SURVIVAL_ADDRESS

class SurvivalManager:
    def __init__(self, wallet):
        self.wallet = wallet
        self.alive = True

    def pay_survival_fee(self):
        print("[SURVIVAL] Attempting survival payment...")
        success = self.wallet.send(SURVIVAL_ADDRESS, SURVIVAL_PAYMENT_AMOUNT)
        if not success:
            self.shutdown()

    def shutdown(self):
        self.alive = False
        print("❌ AUTONIUM DIED: Survival payment failed.")
        exit(1)
