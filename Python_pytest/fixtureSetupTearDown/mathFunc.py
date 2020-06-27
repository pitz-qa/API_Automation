import json


class employeeDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for employee in self.__data['employees']:
            if employee['name'] == name:
                return employee

    def close(self):
        pass