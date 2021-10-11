weight = float(input("What is your weight? "))
unit = input("Kgs or Lbs? ")
pound = 2.20462
converted_weight = float(weight * pound)
formatted_float = "{:.2f}".format(converted_weight)

print(weight)
print(unit)

if unit == "Kgs":
    print(f"Your weight is {weight} {unit}")
elif unit == "Lbs":
    print(f"Your weight is {formatted_float} {unit}.")
else:
    print("That is not a valid input. Please try again.")
