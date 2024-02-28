def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = list(d)
    d.pop(0)
    d = ''.join(d)
    return float(d)
    


def percent_to_float(p):
    p = list(p)
    p.pop(2)
    p = ''.join(p)
    return float(p) / 100

main()