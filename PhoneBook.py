class PhoneBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get(self, name):
        return self.contacts[name];


print('hi')
