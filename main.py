
class Contact:

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        for contact_object in cls.all_contacts:
            return cls.all_contacts.remove(contact_object)
