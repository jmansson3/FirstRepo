def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    meal_cost = d.replace("$", "")
    return float(meal_cost)


def percent_to_float(p):
    tip_amount = p.replace("%", "")
    converted_tip = float(tip_amount) / 100
    return converted_tip


main()
