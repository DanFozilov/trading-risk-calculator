#!/usr/bin/env python3
"""
Professional Trade Risk Calculator
--------------------------------
Supports basic position sizing with:
- configurable value per unit (works for stocks, crypto, forex approximation)
- optional leverage awareness
- fee estimation
- clean CLI interface

NOTE:
This is still a simplified model. Real markets require instrument-specific calculations.
"""

from dataclasses import dataclass
import argparse


@dataclass
class TradeResult:
    trade_type: str
    position_size: float
    risk_dollars: float
    potential_profit: float
    rr_ratio: float
    fees: float


class TradeCalculator:
    def __init__(self, balance: float, risk_percent: float, fee_percent: float = 0.0):
        self.balance = balance
        self.risk_percent = risk_percent
        self.risk_amount = balance * (risk_percent / 100)
        self.fee_percent = fee_percent / 100

    def calculate(self, entry: float, stop_loss: float, take_profit: float,
                  value_per_unit: float = 1.0, leverage: float = 1.0) -> TradeResult:

        if entry == stop_loss:
            raise ValueError("Stop Loss cannot be equal to Entry price.")

        # Determine trade type
        if stop_loss < entry:
            if take_profit <= entry:
                raise ValueError("For LONG, Take Profit must be above Entry.")
            trade_type = "LONG"
        else:
            if take_profit >= entry:
                raise ValueError("For SHORT, Take Profit must be below Entry.")
            trade_type = "SHORT"

        price_risk = abs(entry - stop_loss)
        profit_per_unit = abs(take_profit - entry)

        # Position sizing
        position_size = self.risk_amount / (price_risk * value_per_unit)

        # Apply leverage (affects exposure, not risk directly)
        effective_position = position_size * leverage

        # Profit calculation
        gross_profit = effective_position * profit_per_unit * value_per_unit

        # Fees (entry + exit)
        notional = effective_position * entry * value_per_unit
        fees = notional * self.fee_percent * 2

        net_profit = gross_profit - fees

        rr_ratio = profit_per_unit / price_risk

        return TradeResult(
            trade_type=trade_type,
            position_size=round(position_size, 6),
            risk_dollars=round(self.risk_amount, 2),
            potential_profit=round(net_profit, 2),
            rr_ratio=round(rr_ratio, 2),
            fees=round(fees, 2)
        )


def main():
    parser = argparse.ArgumentParser(description="Professional Trade Risk Calculator")

    parser.add_argument("--balance", type=float, required=True, help="Account balance in USD")
    parser.add_argument("--risk", type=float, required=True, help="Risk per trade (%)")
    parser.add_argument("--entry", type=float, required=True, help="Entry price")
    parser.add_argument("--sl", type=float, required=True, help="Stop loss price")
    parser.add_argument("--tp", type=float, required=True, help="Take profit price")

    parser.add_argument("--value_per_unit", type=float, default=1.0,
                        help="Value per unit (e.g. contract size, pip value)")
    parser.add_argument("--leverage", type=float, default=1.0, help="Leverage multiplier")
    parser.add_argument("--fee", type=float, default=0.0, help="Fee percent per trade")

    args = parser.parse_args()

    calc = TradeCalculator(args.balance, args.risk, args.fee)

    try:
        result = calc.calculate(
            entry=args.entry,
            stop_loss=args.sl,
            take_profit=args.tp,
            value_per_unit=args.value_per_unit,
            leverage=args.leverage
        )

        print("\n=== Trade Summary ===")
        print(f"Type:            {result.trade_type}")
        print(f"Position Size:   {result.position_size}")
        print(f"Risk ($):        {result.risk_dollars}")
        print(f"Potential Profit:{result.potential_profit}")
        print(f"Risk/Reward:     1:{result.rr_ratio}")
        print(f"Estimated Fees:  {result.fees}")
        print("====================\n")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


