class TradeCalculator:
    def __init__(self, balance, risk_percent):
        self.balance = balance
        self.risk_amount = balance * (risk_percent / 100)

    def calculate_metrics(self, entry, stop_loss, take_profit):
        try:
            price_risk = abs(entry - stop_loss)
            if price_risk == 0:
                raise ValueError("Stop Loss cannot be equal to Entry price.")

            units = self.risk_amount / price_risk
            profit_per_unit = abs(take_profit - entry)
            
            total_profit = units * profit_per_unit
            rr_ratio = profit_per_unit / price_risk

            return {
                "units": round(units, 4),
                "risk_dollars": round(self.risk_amount, 2),
                "potential_profit": round(total_profit, 2),
                "rr_ratio": f"1:{round(rr_ratio, 2)}"
            }
        except Exception as e:
            return {"error": str(e)}

def main():
    print("--- Professional Risk Manager ---")
    try:
        # Input validation
        bal = float(input("Balance ($): "))
        risk = float(input("Risk per trade (%): "))
        entry = float(input("Entry Price: "))
        sl = float(input("Stop Loss: "))
        tp = float(input("Take Profit: "))

        calc = TradeCalculator(bal, risk)
        result = calc.calculate_metrics(entry, sl, tp)

        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\n" + "="*20)
            print(f"Position Size: {result['units']} units")
            print(f"Risk Amount:   ${result['risk_dollars']}")
            print(f"Target Profit: ${result['potential_profit']}")
            print(f"Risk/Reward:   {result['rr_ratio']}")
            print("="*20)
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()