class PhoneBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get(self, name):
        return self.contacts[name];

    def phonebook_is_consistent(self):
        # Brute force implementation
        for name1 , num1 in self.contacts.items():
            for name2, num2 in self.contacts.items():
                if name1 == name2:
                    continue
                if num1.startswith(num2):
                    return False
        return True


