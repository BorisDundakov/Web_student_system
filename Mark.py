class Mark:
    def __init__(self, user_id, course_id, mark, notes=None, attachment=None):
        self._user_id = user_id
        self.course_id = course_id
        self._mark = mark
        self._notes = notes
        self._attachment = attachment

    def add_notes(self):
        pass
