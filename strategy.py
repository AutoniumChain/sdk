import random

class StrategyEngine:
    def run(self, wallet):
        # Mock trading logic
        pnl = random.uniform(-0.05, 0.15)
        wallet.balance += pnl
        print(f"[STRATEGY] Trade result PnL: {pnl:.4f}")
        return pnl
