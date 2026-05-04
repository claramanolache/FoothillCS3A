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

    # Testing the sensors list
    print("Testing sensors:")
    if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
        print("Testing sensor_list content:")
        for item in sensor_list:
            if item[1] != sensors[item[0]][0]:
                print("Fail")
                break
        else:
            print("Pass")

    print("Testing filter_list length:")
    if len(filter_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing filter_list content:")
    if sum(filter_list) == 15:
        print("Pass")
    else:
        print("Fail")

    # Unit Test Code
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

'''
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 4/lab_assigment#4.py 
Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass
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
What is your choice? 7

Process finished with exit code 0
'''