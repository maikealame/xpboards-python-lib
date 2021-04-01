# XPBoardsDataSet

## Overview

The XPBoardsDataSet is the dataset manipulation class. With this class you can import and export a dataset from a csv, json files or a python dict and manipulate columns and rows in your dataset.

## Instance Properties

#### Read olny

- id _\<int>_The dataset id
- columns_count _\<int>_ The dataset number of columns
- items_count _\<int>_ The dataset number of rows(items)
- columns _\<list \<Column> >_ The dataset list of columns
- items _\<list \<Row> >_ The list of rows in the dataset
- shape _\<tuple \<int> >_ A (columns_count, items_count) tuple for the dataset

#### Read and Write
- name _\<str>_ The name of the dataset

## Static Methods

<!-- - [from_csv](#from_csv) -->
- [read_json](#read_json)
- [read_dict](#read_dict)

<!-- ### from_csv
Imports a dataset from a CSV file

#### Params:
- path _\<str>_ The path file to read from
- delimiter _\<str> defaults:`,`_ The delimiter for the columns in the CSV file
- quotechar _\<str> defaults:`"` The quotechar used in the CSV file

#### Returns:
A XPBoardsDataSet instance
-->

### read_json
Imports a dataset from a JSON file

The JSON file must follow the following pattern to be read:

```json
    [
        {"firstname": "Ragnar", "lastname": "Lothbrok"},
        {"firstname": "Ivar", "lastname": "Lothbrok"}
    ]
```

The keys become columns and the values are the corresponding row values

#### Params:
- path _\<str>_ The path file to read from

#### Returns:
A XPBoardsDataSet instance

### read_dict
Imports a dataset from a python dicts list

#### Params:
- data _\<list <dict>>_The dataset as a dict

The pattern should be the same as the [read_json](#read_json):

```python
    my_dict = [
        {"firstname": "Ragnar", "lastname": "Lothbrok"},
        {"firstname": "Ivar", "lastname": "Lothbrok"}
    ]
```

#### Returns:
A XPBoardsDataSet instance

## Instance Methods

- [to_csv](#to_csv)
- [to_json](#to_json)
- [to_dict](#to_dict)
- [append_column](#append_column)
- [edit_column](#edit_column)
- [remove_column](#remove_column)
- [append_item](#append_item)
- [remove_item](#remove_item)

### to_csv
Outputs the dataset to a CSV file given a path

#### Params:
- path _\<str>_ The path file to output to
- delimiter _\<str> defaults:','_ Character used as a delimiter
- quotechar _\<str> defaults:'"'_ Character used for quotes
#### Returns:
No return

### to_json
Outputs the dataset to a JSON file given a path

#### Params:
- path _\<str>_ The path file to output to
#### Returns:
No return

### to_dict
Outputs the dataset to a python in memory list of dicts
#### Params:
No params

#### Returns:

A list of dicts with the column names as the keys and the correponding row values

```python

# A dataset with the given format:
#
# fistname  lastname
# Ragnar    Lothbrok
# Ivar      Lothbrok
#
# Should return a list of dictionaries similar to: 

[
    {"firstname": "Ragnar", "lastname": "Lothbrok"},
    {"firstname": "Ivar", "lastname": "Lothbrok"}
]
```


### append_column
Appends a column to the end of the columns list

#### Params:
- name _\<str>_ Name of the column
- value_type _\<str> defaults:'text'_ The type for the column values (read more at [ColumnTypes](#columntypes) section)
- default_value _\<str> defaults:''_ The default value for all the row values for this column
#### Returns:
No return
### edit_column

#### Params:
- column_index _\<int>_ The column index
- name _\<str>_ The new name for the given column
- value_type _\<str> defaults:'text'_ The type for the column values (read more at [ColumnTypes](#columntypes) section)
#### Returns:
No return

### remove_column
Removes column at given index
#### Params:
- column_index _\<int>_ The column index

#### Returns:
No return

### append_item
Appends a row to the end of the rows list
#### Params:
- values _\<list \<str>>_ list of strings for each column
#### Returns:
No return

### remove_item
Removes a row at given index
#### Params:
- item_index _\<int>_ The row index
#### Returns:
No return

## Child Classes

### ColumnTypes
Constrains for the current value_types for columns

Avaiable values:
DECIMAL, INTEGER, PERCENTAGE, DATE, DATETIME, TIME, TEXT, BOOLEAN

*Example*

```python
import xpboards
from xpboards.services import ColumnTypes

my_dataset = xpboards.services.read_json(
    path='my_data.json'
)

my_dataset.edit_column(
    column_index=5,
    value_type=ColumnTypes.TEXT,
)
```
### Column

#### Properties

#### Read olny

- id _\<str>_ An internal unique id for the column

#### Read and Write

- name _\<str>_ The name of the column
- value_type _\<str>_ The type of the values for this column

### Row
#### Properties

#### Read olny

- id _\<str>_ An internal unique id for the row

#### Read and Write

- values _\<list \<str>>_ The list of values for this item

*Example*
```python
import xpboards

# If the JSON has the followiong items:
# [{
#   "firstname": "Ragnar",
#   "lastname": "Lothbrok"
# },
# {
#   "firstname": "Ivar",
#   "lastname": "Lothbrok"
# }]

my_dataset = xpboards.dataset.read_json(
    path='my_data.json',
)

my_dataset.items[0].values # Should display ['Ragnar', 'Lothbrok']

```
<sub>© 2021 by LongView</sub>