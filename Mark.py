class Mark:
    def __init__(self, mark_id, user_id, course_id, mark, notes=None, attachment=None):
        self._mark_id = mark_id
        self._user_id = user_id
        self.course_id = course_id
        self._mark = mark
        self._notes = notes
        self._attachment = attachment

    def add_notes(self, note):
        pass

    def add_attachment(self, attachment):
        pass

    def set_mark(self, mark):
        pass

    def get_mark(self, mark_id):
        pass
