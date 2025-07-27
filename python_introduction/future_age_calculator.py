#!/usr/bin/env python3

"""
future_age_calculator.py

A simple script that prompts the user for their current age and calculates
how old they will be in the year 2050.
Assumes the current year is 2023.
"""

TARGET_YEAR = 2050
CURRENT_YEAR = 2023


def main() -> None:
    """Run the age calculator logic."""
    current_age_str: str = input("How old are you? ")
    current_age: int = int(current_age_str)
    years_to_add: int = TARGET_YEAR - CURRENT_YEAR
    future_age: int = current_age + years_to_add
    print(f"In {TARGET_YEAR}, you will be {future_age} years old.")


if __name__ == "__main__":
    main()
