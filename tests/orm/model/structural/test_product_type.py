import pytest
from django.db import models

from orm_app.models import ProductType

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists():
    try:
        from orm_app.models import ProductType  # noqa F401
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
        (ProductType, "id", models.AutoField),
        (ProductType, "name", models.CharField),
        (ProductType, "parent", models.ForeignKey),
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
- [ ] Ensure that column relationships are correctly defined.
"""


@pytest.mark.parametrize(
    "model, field_name, expected_type, related_model, on_delete_behavior, allow_null, allow_blank",
    [
        (
            ProductType,
            "parent",
            models.ForeignKey,
            ProductType,
            models.CASCADE,
            True,
            True,
        ),
    ],
)
def test_model_structure_relationship(
    model,
    field_name,
    expected_type,
    related_model,
    on_delete_behavior,
    allow_blank,
    allow_null,
):
    # Check if the field exists in the model
    assert hasattr(
        model,
        field_name,
    )

    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if it's a ForeignKey
    assert isinstance(field, expected_type)

    # Check the related model
    assert field.related_model == related_model

    # Check the on_delete behavior
    assert field.remote_field.on_delete == on_delete_behavior

    # Check if the field allows null values
    assert field.null == allow_null

    # Check if the field allows blank values
    assert field.blank == allow_blank


"""
- [ ] Verify nullable or not nullable fields
"""


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (ProductType, "id", False),
        (ProductType, "name", False),
        (ProductType, "parent", True),
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
        (ProductType, "name", 100),
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
        (ProductType, "id", True),
        (ProductType, "name", False),
        (ProductType, "parent", False),
    ],
)
def test_model_structures_unique_fields(model, field_name, is_unique):
    field = model._meta.get_field(field_name)

    assert field.unique == is_unique


@pytest.mark.parametrize(
    "model, field_counts",
    [
        (ProductType, 3),
    ],
)
def test_model_structures_field_counts(model, field_counts):
    field_count = len(model._meta.fields)

    assert field_count == field_counts
