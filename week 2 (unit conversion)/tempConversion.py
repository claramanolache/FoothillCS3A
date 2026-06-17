"""
Assignment Two: Temperature Conversions
Submitted by Clara Manolache
Submitted: April 8, 2026

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and
then converts that temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen
"""
import sys


def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    elif units == 1:
        return celsius_value * 9/5 + 32
    elif units == 2:
        return celsius_value + 273.15
    else:
        return None
def main():
    celsius_value = float(input("Enter a temperature in celsius: "))
    units = int(input("Enter conversion unit (0 for no change, 1 for Fahrenheit, 2 for Kelvin): "))
    converted_val = convert_units(celsius_value, units)
    if converted_val == None:
        print("Error converting, invalid unit.")
        print("Please rerun")
        return
    print(f"The converted value is {converted_val}")

if __name__ == "__main__":
    sys.exit(main())

"""
---------First Sample Output---------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 2 (unit conversion)/tempConversion.py 
Enter a temperature in celsius: 15
Enter conversion unit (0 for no change, 1 for Fahrenheit, 2 for Kelvin): 0
The converted value is 15.0

Process finished with exit code 0
---------Second Sample Output---------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 2 (unit conversion)/tempConversion.py 
Enter a temperature in celsius: 15
Enter conversion unit (0 for no change, 1 for Fahrenheit, 2 for Kelvin): 1
The converted value is 59.0

Process finished with exit code 0
---------Third Sample Output---------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 2 (unit conversion)/tempConversion.py 
Enter a temperature in celsius: 15
Enter conversion unit (0 for no change, 1 for Fahrenheit, 2 for Kelvin): 2
The converted value is 288.15

Process finished with exit code 0
---------Fourth Sample Output---------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 2 (unit conversion)/tempConversion.py 
Enter a temperature in celsius: 15
Enter conversion unit (0 for no change, 1 for Fahrenheit, 2 for Kelvin): -1
Error converting, invalid unit.
Please rerun

Process finished with exit code 0
"""
