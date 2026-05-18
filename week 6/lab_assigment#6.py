"""
Assignment six: Bubble sort using recursion
Submitted by Clara Manolache
Submitted: May 17, 2026

Assignment 5: This program is to practice list recursion and to understand bubble sort algorithm and it's implement.
adds the recursive sort method

Assignment 4: Builds sensor list to use. Practice with tuples.

Assignment 3: This assignment adds code to build a menu and support it. The menu provides the interface that a user
 will use to interact with the program.

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and then converts that
temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen

"""
def recursive_sort(list_to_sort, key):
    """
    Bubble sort a list of tuples by either the first or second element,
    first element if key == 0, second element if key == 1
    Uses recursion. Applied on sensor list
    """
    pass_list = list_to_sort.copy()
    swaps = False
    len_minus_one = len(list_to_sort) - 1
    for i in range (len_minus_one):
        if pass_list[i][key] > pass_list[i + 1][key]:
            pass_list[i], pass_list[i + 1] = pass_list[i + 1], pass_list[i]
            swaps = True
    if len_minus_one == 1 or not swaps:
        return pass_list
    final_list = recursive_sort(pass_list[0:len_minus_one], key)
    final_list.append(pass_list[-1])
    return final_list


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
    """ Builds data structures required for the program
        and provides the unit test code
    """
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }
    sensor_list = [(room, data[0], data[1]) for room, data in sensors.items()]
    filter_list = [(data[1]) for data in sensors.values()]

    # Unit test
    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n", recursive_sort(sensor_list, 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
    print("\nOriginal unsorted list\n", sensor_list)

    # propmting the user
    while (True):
        print()
        print_menu()
        choice = input("What is your choice? ")
        try:
            choice = int(choice)
        except:
            print("Please enter an integer")
            continue
        if choice == 1:
            new_file(None)
        elif choice == 2:
            choose_units()
        elif choice == 3:
            change_filter(None, None)
        elif choice == 4:
            print_summary_statistics(None, None)
        elif choice == 5:
            print_temp_by_day_time(None, None)
        elif choice == 6:
            print_histogram(None, None)
        elif choice == 7:
            exit()
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.")


if __name__ == "__main__":
    main()

'''
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 6/lab_assigment#6.py 

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

List sorted by room number
 [('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 5), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

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
'''
