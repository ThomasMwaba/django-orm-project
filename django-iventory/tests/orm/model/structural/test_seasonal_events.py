import pytest
from django.db import models

from orm_app.models import SeasonalEvent

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists():
    try:
        from orm_app.models import SeasonalEvent  # noqa F401
    except ImportError:
        assert False
    else:
        assert True


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


@pytest.mark.parametrize(
    "model , field_name ,expected_type",
    [
        (SeasonalEvent, "id", models.AutoField),
        (SeasonalEvent, "start_date", models.DateField),
        (SeasonalEvent, "end_date", models.DateField),
        (SeasonalEvent, "name", models.CharField),
    ],
)
def test_model_structure_column_data_types(model, field_name, expected_type):
    assert hasattr(
        model,
        field_name,
    ), f"{model.__name__} model does not have {field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type)


@pytest.mark.parametrize(
    "model , expected_field_count",
    [
        (SeasonalEvent, 4),
    ],
)
def test_model_structure_field_count(model, expected_field_count):
    field_count = len(model._meta.fields)
    assert field_count == expected_field_count


"""
 - [ ] Verify nullable or not nullable fields
"""


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (SeasonalEvent, "id", False),
        (SeasonalEvent, "start_date", False),
        (SeasonalEvent, "end_date", False),
        (SeasonalEvent, "name", False),
    ],
)
def test_structure_nullable_constraints(model, field_name, expected_nullable):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the nullable constraint matches the expected value
    assert field.null == expected_nullable


@pytest.mark.parametrize(
    "model, field_name, expected_length",
    [
        (SeasonalEvent, "name", 100),
    ],
)
def test_model_structure_column_lengths(model, field_name, expected_length):
    field = model._meta.get_field(field_name)

    assert field.max_length == expected_length


"""
- [ ] Validate the enforcement of unique constraints for columns requiring unique values.
"""


@pytest.mark.parametrize(
    "model, field_name, is_unique",
    [
        (SeasonalEvent, "id", True),
        (SeasonalEvent, "name", True),
    ],
)
def test_model_structures_unique_fields(model, field_name, is_unique):
    field = model._meta.get_field(field_name)

    assert field.unique == is_unique
