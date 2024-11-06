potential_coefficients = [1, 2.4, 'hello', 15, 70000.1, 0.0001, True, 2+5j]

for values in potential_coefficients:
    if values == type(int) or type(float):
        print("Умова успішна")

for values in potential_coefficients:
    if type(values) == int or type(values) == float:
        if values < 0.5 or values > 100:
            print(values)
        else:
            values = None


