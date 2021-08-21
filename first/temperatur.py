from temp_lib import convert

print("\n=== Temperature Convert ===\n")

print("Convert from: ")
print("1. Celcius (\N{DEGREE SIGN}C)")
print("2. Fahrenheit (\N{DEGREE SIGN}F)")
print("3. Kelvin (\N{DEGREE SIGN}K)")
menu = int(input("Choose: "))

temp = float(input("\nInput temperature: "))

print('')
convert(menu, temp)
print('')