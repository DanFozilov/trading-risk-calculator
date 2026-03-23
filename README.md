A Python-based risk management tool for calculating precise position sizes and R/R ratios in trading (SMC/ICT models).
# Trading Risk and Position Size Calculator

This is a Python-based utility developed to handle the mathematical side of trading risk management. It is specifically designed for traders using SMC or ICT models who need to calculate precise position sizes based on their stop loss and account equity.

## Overview
Programming and data analysis are my primary focuses, and I treat trading as a data-driven hobby. This project was built to bridge the gap between algorithmic logic and financial markets. It eliminates the emotional stress of manual calculations by providing a purely objective, mathematical approach to entry strategies.

## Key Features
- Automatic Direction Detection: The system identifies whether a trade is Long or Short based on the entry and stop loss relationship.
- Logic Validation: Includes strict validation rules to ensure Take Profit and Stop Loss levels are mathematically consistent with the trade direction.
- Precision Sizing: Calculates the exact number of units to trade based on specific risk tolerance and account balance.
- RR Ratio Analysis: Automatically calculates the Risk-to-Reward ratio to filter out low-probability setups.
- OOP Structure: Built using Object-Oriented Programming principles to ensure the code is modular and maintainable.

## Technical Logic
The calculator follows the standard risk management formula:
Position Size = (Account Balance * Risk Percentage) / |Entry - Stop Loss|

## Tech Stack
- Language: Python 3.x
- Paradigm: Object-Oriented Programming (OOP)

## How to Run
1. Clone the repository:
   git clone https://github.com/DanFozilov/trading-risk-calculator.git

2. Run the script:
   python main.py

3. Follow the terminal prompts to enter your balance, risk percentage, and price levels.

---

### About the Developer
I am a software developer with a strong focus on Data Analysis and its applications in Industrial Engineering. My long-term goal is to integrate Machine Learning into industrial processes to improve efficiency and decision-making. I prioritize building clean, maintainable systems that solve real-world optimization problems. Trading serves as a practical playground for testing mathematical logic, but my professional path is centered on data-driven engineering.
