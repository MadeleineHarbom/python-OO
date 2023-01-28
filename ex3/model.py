import re
import string


class Person:
    def __init__(self, firstname: str, lastname: str, telephone_number=None, email=None, display_mode=None):
        if isinstance(firstname, str):
            raise TypeError

        self.firstname = firstname
        self.lastname = lastname
        self.telephone_number = telephone_number
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        if self.firstname == other.firstname and self.lastname == other.lastname:
            if self.email == other.email and self.telephone_number == other.telephone_number:
                return True
        return False

    def __hash__(self):
        return hash((self.firstname, self.lastname, self.telephone_number, self.email))

    def __repr__(self):
        if self.display_mode == "masked":
            return f"Person('{Person._obscure(self.firstname)}', '{Person._obscure(self.lastname)}')"
        if self.email is not None and self.telephone_number is not None:
            return f"Person('{self.firstname}', '{self.lastname}', telephone_number='{self.telephone_number}', email='{self.email}')"
        elif self.email is not None:
            return f"Person('{self.firstname}', '{self.lastname}', email='{self.email}')"
        elif self.telephone_number is not None:
            return f"Person('{self.firstname}', '{self.lastname}', telephone_number='{self.telephone_number}')"
        else:
            return f"Person('{self.firstname}', '{self.lastname}')"


    def __str__(self):
        return self.firstname[0] + self.lastname[0]

    def __format__(self, format_spec):
        if self.display_mode != 'masked' or format_spec == 'unmasked':
            additional_info=''
            if self.email is not None and self.telephone_number is not None:
                additional_info = f', telephone_number={self.telephone_number}, email={self.email}'
            elif self.email is not None:
                additional_info = f', email={self.email}'
            elif self.telephone_number is not None:
                f',telephone_number={self.telephone_number}'
            return f"Person(firstname={self.firstname}, lastname={self.lastname}{additional_info})"
        else:
            return f"Person(firstname={Person._obscure(self.firstname)}, lastname={Person._obscure(self.lastname)})"

    @classmethod
    def _obscure(cls, string):
        obscured_string = string[0] + (len(string)-1) * '*'
        return obscured_string



