import pytest

from django.urls import reverse, resolve

from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def cheese():
    return CheeseFactory()


def test_list_reverse():
    """cheeses:list should reverse to cheeses"""
    assert reverse("cheeses:list") == "/cheeses/"


def test_list_resolve():
    """cheeses resolve to cheeses:list"""
    assert resolve("/cheeses/").view_name == "cheeses:list"
