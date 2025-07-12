#!/usr/bin/env python3

"""
finance_calculator.py

A script to compute a user's monthly savings and project annual savings
with a simple 5% interest rate, without using conditional statements.
"""

# Constants
ANNUAL_INTEREST_RATE = 0.05  # 5% annual interest
MONTHS_IN_YEAR = 12

def main() -> None:
    """Prompt user for income and expenses, then calculate savings."""
    income_str: str = input("Enter your monthly income: ")
    expenses_str: str = input("Enter your total monthly expenses: ")

    income: float = float(income_str)
    expenses: float = float(expenses_str)

    monthly_savings: float = income - expenses
    annual_savings: float = monthly_savings * MONTHS_IN_YEAR
    projected_savings: float = annual_savings + (annual_savings * ANNUAL_INTEREST_RATE)

    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
    main()
