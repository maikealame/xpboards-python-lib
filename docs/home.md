# XPBoards Python Library

## Installation

You can install the library directly from PyPI:

`pip install xpboards`

To check if the installation was successful, you can try to authenticate with your email and passoword:

```python
import xpboards

xpb_services = xpboards.services(
    email='your@email.com',
    password='your_password'
)

# This should output your dataset list or
# an empty list if you have no datasets in your account
xpb_services.list_datasets()

```
**Be aware:** A valid XPBoards account is needed to use most of the features of the library. You can easly create a free account [here](https://web.xpboards.com.br/customer/register).

## Topics

- [XPBoardsServices](#)
- [XPBoardsDataSet](#)
- [XPBoardsPlan](#)
- [Examples](#)

<sub>© 2021 by LongView</sub>