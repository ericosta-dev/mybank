import pytest

from app.entities.category import Category


class TestCategory:
    def test_category_creation(self):
        category_obj = Category(id=1, name="Test Category", goal=100.00)

        assert category_obj.id == int(1)
        assert category_obj.name == "Test Category"
        assert category_obj.goal == float(100.00)

    def test_category_creation_with_invalid_id(self):
        with pytest.raises(TypeError) as excinfo:
            Category(id="1", name="Test Category", goal=100.00)

            assert "Category id must be an positive integer" in str(excinfo.value)

    def test_category_creation_with_invalid_name(self):
        with pytest.raises(TypeError) as excinfo:
            Category(id=1, name="", goal=100.00)

            assert "Category name must be a non-empty string" in str(excinfo.value)

    def test_category_creation_with_invalid_goal(self):
        with pytest.raises(TypeError) as excinfo:
            Category(id=1, name="Test Category", goal=-1.00)

            assert "Category goal must be a positive float" in str(excinfo.value)
