import pytest
from django.db import models

from orm_app.models import Category

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists():
    try:
        from orm_app.models import Category  # noqa F401
    except ImportError:
        assert False
    else:
        assert True


def test_model_1():
    assert True


def test_structure_2():
    assert True


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


@pytest.mark.parametrize(
    "model , field_name ,expected_type",
    [
        (Category, "id", models.AutoField),
        (Category, "name", models.CharField),
        (Category, "slug", models.SlugField),
        (Category, "is_active", models.BooleanField),
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
        (Category, "parent", models.ForeignKey, Category, models.PROTECT, True, True),
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
        (Category, "id", False),
        (Category, "name", False),
        (Category, "is_active", False),
    ],
)
def test_structure_nullable_constraints(model, field_name, expected_nullable):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the nullable constraint matches the expected value
    assert field.null == expected_nullable


"""
- [ ] Verify the correctness of default values for relevant columns.
 """


@pytest.mark.parametrize(
    "model, field_name, expected_default",
    [
        (Category, "is_active", False),
    ],
)
def test_model_structure_default_values(model, field_name, expected_default):
    field = model._meta.get_field(field_name)

    assert field.default == expected_default


@pytest.mark.parametrize(
    "model, field_name, expected_length",
    [
        (Category, "name", 100),
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
        (Category, "id", True),
        (Category, "name", True),
        (Category, "slug", True),
        (Category, "is_active", False),
    ],
)
def test_model_structures_unique_fields(model, field_name, is_unique):
    field = model._meta.get_field(field_name)

    assert field.unique == is_unique
