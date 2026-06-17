"""
Assignment Three: Implementing a Menu
Submitted by Clara Manolache
Submitted: April 8, 2026

Assignment 3: This assignment adds code to build a menu and support it. The menu provides the interface that a user will use to interact with the program.

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and then converts that temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen
"""
import sys
def convert_units(celsius_value, units):
    """
    From lab assigment #2, takes in a celsius_value
    temperature and converts to fahrenheits or kelvin
    """
    if units == 0:
        return celsius_value
    elif units == 1:
        return celsius_value * 9/5 + 32
    elif units == 2:
        return celsius_value + 273.15
    else:
        return None
def print_menu():
    """
    Prints the menu
    """
    print("Main Menu\n---------\n"
        "1 - Process a new data file\n2 - Choose units\n3 - Edit room filter\n"
        "4 - Show summary statistics\n5 - Show temperature by date and time\n"
        "6 - Show histogram of temperatures\n7 - Quit")
def new_file(dataset):
    """
    Open a new file, if user chooses item 1
    """
    print("New File Function Called")
def choose_units():
    """
    Called if user choose item 2
    """
    print("Choose Units Function Called")
def change_filter(sensor_list, active_sensors):
    """
    Called if user choose item 3
    """
    print("Change Filter Function Called")
def print_summary_statistics(dataset, active_sensors):
    """
    Called if user choose item 4
    """
    print("Print Summary Statistics Function Called")
def print_temp_by_day_time(dataset, active_sensors):
    """
    Called if user choose item 5
    """
    print("Print Temp By Day/Time Function Called")
def print_histogram(dataset, active_sensors):
    """
    Called if user choose item 6
    """
    print("Print Histogram Function Called")
def main():
    """
    Called if user choose item 5
    """
    print("STEM Center Temperature Project")
    print("Clara Manolache")
    while (True):
        print()
        print_menu()
        choice = input("What is your choice? ")
        try:
            choice = int(choice)
        except:
            print("Please enter an integer")
            continue
        if (choice == 1):
            new_file(None)
        elif (choice == 2):
            choose_units()
        elif (choice == 3):
            change_filter(None, None)
        elif (choice == 4):
            print_summary_statistics(None, None)
        elif (choice == 5):
            print_temp_by_day_time(None, None)
        elif (choice == 6):
            print_histogram(None, None)
        elif (choice == 7):
            exit()
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.")
if __name__ == "__main__":
    sys.exit(main())

"""
Sample Output #1:
---------------------------------------------------------------------------------------------------------------------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 3 (menu)/lab_assignment 3.py 
STEM Center Temperature Project
Clara Manolache

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? -1
Invalid Choice, please enter an integer between 1 and 7.

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 1
New File Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 2
Choose Units Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 3
Change Filter Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 4
Print Summary Statistics Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 5
Print Temp By Day/Time Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 6
Print Histogram Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 7

Process finished with exit code 0


Sample Output #2:
---------------------------------------------------------------------------------------------------------------------
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 3 (menu)/lab_assignment 3.py 
STEM Center Temperature Project
Clara Manolache

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? hello
Please enter an integer

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 7

Process finished with exit code 0

"""
