
dollar = float(input("How much is the meal? ").lstrip("$"))
percent = float(input("What percent would you like to tip? ").rstrip("%"))
tip = dollar * (percent / 100)
total = dollar + tip

