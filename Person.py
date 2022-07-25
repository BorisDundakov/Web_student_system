class Person:
    def __init__(self, id, first_name, second_name, last_name, age, status):
        self._id = id
        self._first_name = first_name
        self._second_name = second_name
        self._last_name = last_name
        self._age = age
        self._status = status

    def generate_univeristy_email(self, faculty_number=None):

        status = self._status
        first_name = self._first_name
        last_name = self._last_name

        university_email = ""
        email_name = first_name + last_name
        # status 1 = admin; status 2 = user
        if status == 1:
            university_email = email_name + "university_domain from consants"
        if status == 2:
            university_email = email_name + "_" + faculty_number + "university_domain from consants"

        return university_email
