import pytest
from xpboards import dataset as xpb_dataset


DATASET_DICT = [
    {
        'firstname': 'Maike',
        'lastname': 'Alame'
    },
    {
        'firstname': 'Fernando',
        'lastname': 'Palmeiro'
    }
]

# Fixtures

@pytest.fixture
def dataset_instance():
    return xpb_dataset.read_dict(DATASET_DICT)

# Test dataset importing

def test_dataset_read_dict():
    dataset = xpb_dataset.read_dict(DATASET_DICT)
    assert isinstance(dataset, xpb_dataset)

# Test dataset properties

def test_dataset_shape(dataset_instance):
    shape = dataset_instance.shape
    assert shape[0] == 2 and shape[1] == 2

# Test dataset manipulation

def test_dataset_append_column(dataset_instance):
    dataset_columns_count_before = dataset_instance.columns_count
    dataset_instance.append_column(name='awake', value_type='boolean', default_value='true')
    assert dataset_columns_count_before + 1 == dataset_instance.columns_count

def test_dataset_edit_column(dataset_instance):
    new_name = 'notfirstname'
    dataset_instance.edit_column(column_index=0, name=new_name)
    assert new_name == dataset_instance.columns[0].name

def test_dataset_remove_column(dataset_instance):
    dataset_columns_count_before = dataset_instance.columns_count
    dataset_instance.remove_column(column_index=0)
    assert dataset_columns_count_before - 1 == dataset_instance.columns_count

def test_dataset_append_item(dataset_instance):
    dataset_items_count_before = dataset_instance.items_count
    dataset_instance.append_item(['Douglas', 'Eloy'])
    assert dataset_items_count_before + 1 == dataset_instance.items_count

def test_dataset_remove_item(dataset_instance):
    dataset_items_count_before = dataset_instance.items_count
    dataset_instance.remove_item(item_index=0)
    assert dataset_items_count_before - 1 == dataset_instance.items_count