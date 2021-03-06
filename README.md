# XPBoards Python Library

A python implementation to improve [XPBoards](https://web.xpboards.com.br/) datasets handling.

## Installation

To install from PyPI:

`pip install xpboards`

## Usage

With this library you can import, export, manipulate, list, create, update and clear your datasets from [XPBoards](https://web.xpboards.com.br/)

A creation example importing from a csv file:

```python
from xpboards.services import XPBoardsServices
from xpboards.dataset import XPBoardsDataSet

xpb_services = XPBoardsServices(
    email="your-xpboards-account@email.com",
    password='your-password'
)

my_dataset = XPBoardsDataSet.from_json(
    path='my_data.json'
)
xpb_services.create_dataset(data=my_dataset, name='My Dataset')

```

Read the full documentation [here](#)

<sub>© 2021 by LongView</sub>