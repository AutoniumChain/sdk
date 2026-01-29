import time
from wallet import Wallet
from strategy import StrategyEngine
from survival import SurvivalManager
from config import SURVIVAL_PAYMENT_INTERVAL

def main():
    wallet = Wallet(private_key="DEV_PRIVATE_KEY")
    strategy = StrategyEngine()
    survival = SurvivalManager(wallet)

    print("🔥 Autonium started. Survival mode ON.")

    last_payment = time.time()

    while survival.alive:
        # Run strategy
        strategy.run(wallet)

        # Check survival payment timer
        if time.time() - last_payment >= SURVIVAL_PAYMENT_INTERVAL:
            survival.pay_survival_fee()
            last_payment = time.time()

        print(f"[STATUS] Balance: {wallet.get_balance():.4f}")
        time.sleep(5)

if __name__ == "__main__":
    main()
