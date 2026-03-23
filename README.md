
# Professional Trade Risk Calculator

A clean and practical Python CLI tool for calculating position size, risk, and reward in trading.

## Features

- Position sizing based on risk percentage
- Supports LONG and SHORT trades
- Optional leverage support
- Fee estimation (entry + exit)
- Flexible value-per-unit (works across markets)

## Installation

```bash
git clone https://github.com/DanFozilov/trade-risk-calculator.git
cd trade-risk-calculator
python calculator.py --help
```

## Usage Example

```bash
python calculator.py \
  --balance 5000 \
  --risk 1 \
  --entry 100 \
  --sl 95 \
  --tp 110 \
  --value_per_unit 1 \
  --leverage 3 \
  --fee 0.04
```

## Parameters

| Parameter | Description |
|----------|------------|
| balance | Account size in USD |
| risk | Risk per trade (%) |
| entry | Entry price |
| sl | Stop loss |
| tp | Take profit |
| value_per_unit | Contract or asset value per unit |
| leverage | Leverage multiplier |
| fee | Fee percent per trade |

## Important Notes

- This tool is a simplified calculator, not a trading engine
- Forex requires proper pip value handling
- Futures require contract specifications
- Slippage is not modeled

## Roadmap

- Web interface (Streamlit)
- Telegram bot integration
- Exchange-specific calculators

## License

MIT License
"""
