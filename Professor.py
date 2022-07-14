from Person import Person


class Professor(Person):
    def __init__(self, id, first_name, second_name, last_name, status):
        super().__init__(id, first_name, second_name, last_name, status)

    def add_mark(self, mark, user_id, course_id):
        pass

    def add_note(self, note, user_id, course_id):
        pass

    def add_attachment(self, attachment, user_id, course_id):
        pass
