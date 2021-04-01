# XPBoardsServices

## Overview

The XPBoardsServices class is responsible to connect with the XPBoards api, providing methods to authenticate, view plan, retrieve and update datasets

Upon instance, the authentication is needed:

```python
    import xpboards

    xpb_services = xpboards.services(
        email='your@email.com',
        password='your-password'
    )
```

## Instance Methods

- [get_token](#get_token)
- [get_plan](#get_plan)
- [list_datasets](#list_datasets)
- [list_dataset_items](#list_dataset_items)
- [create_dataset](#create_dataset)
- [update_dataset](#update_dataset)
- [clear_dataset](#clear_dataset)

### get_token
Get the authenticated user token.

#### Params:
No params

#### Returns:
The authenticated user accessToken as a string

### get_plan
Get the authenticated user plan

#### Params:
No params

#### Returns:

A [Plan](#) instance

### list_datasets
Lists authenticated user dataset

#### Params:
No params

#### Returns:
Returns a dict with info about the user datasets.

*Example* 

```python

    [
        {
            "id": 1,
            "name": "Dataset 1",
            "code": None,
            "created_at": "2021-03-30T14:25:48.000000Z",
            "column_count": 5,
            "row_count": 20
        },
        {
            "id": 2,
            "name": "Dataset 2",
            "code": None,
            "created_at": "2021-03-30T14:31:22.000000Z",
            "column_count": 10,
            "row_count": 110
        }
    ]

```

### list_dataset_items
Get the selected dataset full information with rows and columns

#### Params:
- dataset_id _\<int>_ The dataset id

- raw _\<bool> defaults:`False`_

#### Returns:
If _raw_ param is set to `False`, returns a [XPBoardsDataSet](#) instance. When _raw_ is set to `True`, returns the api response json as a dict

### create_dataset
Creates a new dataset

#### Params:
- data _\<XPBoardsDataSet>_ 
- name _\<str>_ 

#### Returns:
Returns a dict with information about the created dataset (similar to _raw_ option in [list_dataset_items](#list_dataset_items))

**Be aware:** A dataset needs a name to be created, so don't forget to set it

*Example*

```python
import xpboards

xpb_services = xpboards.services(
    email='your@email.com',
    password='your_passoword'
)

my_dataset = xpboards.dataset.read_json(
    path='my_table.json'
)

xpb_services.create_dataset(data=my_dataset, name='My dataset')

```

### update_dataset
Replaces selected dataset data (columns, rows and name) with provided dataset

#### Params:
- dataset_id _\<int>_ The dataset id
- data _\<XPBoardsDataSet>_

#### Returns:
Returns a dict with information about the updated dataset (similar to _raw_ option in [list_dataset_items](#list_dataset_items))

### clear_dataset
A shortcut to passing an empty dataset (with no rows) to [update_dataset](#update_dataset). Deletes all rows of provided dataset and update it.

#### Params:
- dataset_id _\<int>_ The dataset id
- data _\<XPBoardsDataSet>_

#### Returns:
Returns a dict with information about the updated dataset (similar to _raw_ option in [list_dataset_items](#list_dataset_items))

<sub>© 2021 by LongView</sub>