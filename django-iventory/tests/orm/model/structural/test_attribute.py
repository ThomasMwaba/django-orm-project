import pytest
from django.db import models

from orm_app.models import Attribute

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists():
    try:
        from orm_app.models import Attribute  # noqa F401
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
        (Attribute, "id", models.AutoField),
        (Attribute, "name", models.CharField),
        (Attribute, "description", models.TextField),
    ],
)
def test_model_structure_column_data_types(model, field_name, expected_type):
    assert hasattr(
        model,
        field_name,
    ), f"{model.__name__} model does not have {field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type)


"""
- [ ] Verify nullable or not nullable fields
"""


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (Attribute, "id", False),
        (Attribute, "name", False),
        (Attribute, "description", True),
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
        (Attribute, "name", 100),
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
        (Attribute, "id", True),
        (Attribute, "name", True),
        (Attribute, "description", False),
    ],
)
def test_model_structures_unique_fields(model, field_name, is_unique):
    field = model._meta.get_field(field_name)

    assert field.unique == is_unique
