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

