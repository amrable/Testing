from phonebook import PhoneBook

def test_lookup_by_name():
    pb = PhoneBook()
    pb.add_contact("Amr","123")
    assert "123" == pb.get("Amr")