import csv
import json

class XPBoardsDataSet:
    def __init__(self, dataset):
        """
            The dataset must have the following pattern:

            {
                "id": <integer>, (for XPBoards datasets that already exists, optional)
                "name": <string>,
                "columns":[
                    {
                        "type": <string>, (integer, text, decimal, date)
                        "name": <string>
                    }   
                ],
                "rows": [
                    "values": {
                        "value": <any> (any primitive type)
                    }
                ]
            }
        
        """

        self.__id = dataset.get('id', None)
        self.__name = dataset.get('name', None)

        self.__columns = []

        for column in dataset['columns']:
            self.__columns.append(
                self.Column(
                    name=column['name'],
                    value_type=column['type']
                )
            )

        self.__rows = []

        for row in dataset['rows']:

            self.__rows.append(
                self.Row(
                    values=list(map(lambda item: item['value'], row['values']))
                )
            )

    @property
    def columns_count(self):
        """
            Returns the number of columns in the dataset
        """

        return len(self.__columns)

    @property
    def rows_count(self):
        """
            Returns the number of rows in the dataset
        """

        return len(self.__rows)

    @property
    def columns(self):
        """
            Returns the list of columns of the dataset
        """

        return self.__columns
    
    @staticmethod
    def from_csv(path, separator=';'):
        """
            Returns a new XPBoardsDataSet instance reading from specified CSV file
        """

        pass

    @staticmethod
    def from_json(obj, path=None):
        """
            Returns a new XPBoardsDataSet instance reading from specified JSON file or python dict
        """

        pass

    def to_csv(self, to, separator=';'):
        """ 
            Outputs dataset to a CSV file given a path ('to' param)
        """

        pass
    
    def to_json(self, to=None):
        """ 
            Outputs the dataset to a JSON file given a path ('to' param)

            If a path is not provided, returns the result as a python dict
        """

        # self.columns_count()

        dataset_json = []

        for row in self.__rows:
            json_row = {}

            for i in range(self.columns_count):
                json_row[self.__columns[i].name] = row.values[i]

            dataset_json.append(json_row)

        if to:
            with open(to, 'w') as f:
                json.dump(dataset_json, f)
        else:
            return dataset_json

    def append(self):
        """ 
            Append item to the end of the dataset
        """

        pass

    def remove(self):
        """ 
            Remove specified item from the dataset
        """

        pass

    class Column:
        def __init__(self, name, value_type):
            self.__name = name
            self.__value_type = value_type

        def __repr__(self):
            return self.__name

        @property
        def name(self):
            return self.__name

        @property
        def value_type(self):
            return self.__value_type

    class Row:
        def __init__(self, values):
            self.__values = values

        @property
        def values(self):
            return self.__values
        

    
