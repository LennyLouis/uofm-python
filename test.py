import numpy as np

dollar = float(input("How much is the meal?").lstrip("$"))
percent = float(input("What percent would you like to tip?").rstrip("%"))
round_up = input("Would you like to round up the tip to whole dollar? (y/n)").lower()

tip = dollar * (percent / 100)

if round_up == "y":
    tip = np.ceil(tip)

print(f"You should tip ${tip:.2f}")

total = dollar + tip
print(f"Your total is ${total:.2f}")