# Strategy Lab V2 backtester
class Backtester:
    def __init__(self, initial_balance=1000.0):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.trades = []

    def record_trade(self, trade):
        self.trades.append(trade)

    def summary(self):
        wins = sum(1 for trade in self.trades if trade.get('profit', 0) > 0)
        losses = sum(1 for trade in self.trades if trade.get('profit', 0) < 0)

        return {
            'initial_balance': self.initial_balance,
            'final_balance': self.balance,
            'total_trades': len(self.trades),
            'wins': wins,
            'losses': losses,
        }