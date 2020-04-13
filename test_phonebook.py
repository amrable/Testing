import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        # Create instance while setting up tests
        self.phonebook = PhoneBook()

    # it is used to free any allocated resources after finishing the tests
    def tearDown(self) -> None:
        super().tearDown()

    def test_lookup_by_name(self):
        self.phonebook.add_contact("Ahmed", "123")
        # Test
        value = self.phonebook.get("Ahmed")
        # Validate using assertEqual( true value , actual value )
        self.assertEqual("123", value)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.get("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.phonebook_is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add_contact("Amr","123")
        self.phonebook.add_contact("Ahmed","456")
        self.assertTrue(self.phonebook.phonebook_is_consistent())

    def test_is_inconsistent_with_duplicate_entries(self):
        self.phonebook.add_contact("Amr", "123")
        self.phonebook.add_contact("Ahmed", "123")
        self.assertFalse(self.phonebook.phonebook_is_consistent())

    def test_is_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add_contact("Amr", "123")
        self.phonebook.add_contact("Ahmed", "12345")
        self.assertFalse(self.phonebook.phonebook_is_consistent())
