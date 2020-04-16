from phonebook import PhoneBook
import pytest

@pytest.fixture
def pb():
    pb = PhoneBook()
    yield pb
    pb.clear()


def test_lookup_by_name(pb):
    pb.add_contact("Amr", "123")
    assert "123" == pb.get("Amr")
