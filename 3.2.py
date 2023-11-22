class Address:
    def __init__(self, city, street, plaque):
        self.address_data = {
            "city": city,
            "street": street,
            "plaque": plaque
        }

    def display(self):
        return f"Address: {self.address_data['city']}, {self.address_data['street']}, {self.address_data['plaque']}"


class Person:
    def __init__(self, customer_id, first_name, last_name, phone_number, email):
        self.person_data = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email": email
        }

    def display(self):
        return f"Person: {self.person_data['first_name']} {self.person_data['last_name']}, " \
               f"Phone: {self.person_data['phone_number']}, Email: {self.person_data['email']}"


class Contact(Person, Address):
    def __init__(self, customer_id, first_name, last_name, phone_number, email, city, street, plaque):
        Person.__init__(self, customer_id, first_name, last_name, phone_number, email)
        Address.__init__(self, city, street, plaque)
        self.contact_data = {**self.person_data, **self.address_data}

    def display(self):
        person_info = super(Person, self).display()
        address_info = super(Address, self).display()
        return f"{person_info}, {address_info}"


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_customer(self, last_name):
        for contact in self.contacts:
            if contact.contact_data['last_name'] == last_name:
                return contact.display()
        return "Customer Unknown"

    def display(self):
        return "\n".join(contact.display() for contact in self.contacts)


# نمونه‌هایی از کلاس Contact
contacts = [
    Contact(1, "John", "Doe", "123456789", "john@example.com", "City1", "Street1", 10),
    Contact(2, "Jane", "Doe", "987654321", "jane@example.com", "City2", "Street2", 20),
    
]

# نمونه کلاس PhoneBook و اضافه کردن تماس‌ها
phone_book = PhoneBook()
for contact in contacts:
    phone_book.add_contact(contact)

# نمایش دفترچه تلفن
print(phone_book.display())

# جستجوی مشتری
print(phone_book.search_customer("Doe"))
