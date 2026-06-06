"""
Assignment eight: Dataset Class
Submitted by Clara Manolache
Submitted: May 31, 2026
CWID: 20653756

Assigment description:
Practice making classes. Set up more methods to be implemented later. Does
backend work to abstract our code.
"""
class TempDataset:
    totDatasets = 0

    def __init__(self):
        """
        Constructor increments total data sets and initializes two
        instance variables, data set and name to standard values.
        Takes no arguments
        """
        TempDataset.totDatasets += 1
        self._data_set = None
        self._name = "Unnamed"

    def process_file(self, filename):
        """
        To be implemented later, returns False always
        """
        return False

    def get_summary_statistics(self, filter_list):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return default tuple.
        """
        if self._data_set is None:
            return None
        return 0, 0, 0

    def get_avg_temperature_day_time(self, filter_list, day, time):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return 0.
        """
        if self._data_set is None:
            return None
        return 0

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return 0.
        """
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return 0.
        """
        if self._data_set is None:
            return None
        return 0

    @classmethod
    def get_num_objects(cls):
        """
        Class Method
        :return: total number of objects of the type TempDataset
        """
        return cls.totDatasets

    # Setters and Getters
    @property
    def name(self):
        """Getter for the dataset name"""
        return self._name

    @name.setter
    def name(self, value):
        """
        Checks if new name fits conditions, if not returns error
        if fits conditions, name is set to value
        """
        if len(value) < 3:
            raise ValueError("Too Short Name")
        elif len(value) > 20:
            raise ValueError("Too Long Name")
        else:
            self._name = value

def main():
    """
    Unit test for this assigment
    """
    current_set = TempDataset()

    print("First test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 1:
        print("Success")
    else:
        print("Fail")

    second_set = TempDataset()

    print("Second test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 2:
        print("Success")
    else:
        print("Fail")

    print("Testing get_name and set_name: ")

    print("- Default Name:", end='')

    if current_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("- Try setting a name too short: ", end='')

    try:
        current_set.name = "to"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name too long: ", end='')

    try:
        current_set.name = "supercalifragilisticexpialidocious"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name just right (Goldilocks): ", end='')

    try:
        current_set.name = "New Name"
        if current_set.name == "New Name":
            print("Success")
        else:
            print("Fail")
    except ValueError:
        print("Fail")

    print("- Make sure we didn't touch the other object: ", end='')
    if second_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("Testing get_avg_temperature_day_time: ", end='')
    if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_num_temps: ", end='')
    if current_set.get_num_temps(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_loaded_temps: ", end='')
    if current_set.get_loaded_temps() is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_summary_statistics: ", end='')
    if current_set.get_summary_statistics(None) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing process_file: ", end='')
    if current_set.process_file(None) is False:
        print("Success")
    else:
        print("Fail")

if __name__ == "__main__":
    main()

"""
Output from Unit Test:

/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 8/TempDataset.py 
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success

Process finished with exit code 0

"""