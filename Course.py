class Course:
    def __init__(self, course_id, course_name, course_credits, course_description):
        self._course_id = course_id
        self._course_name = course_name
        self.course_credits = course_credits
        self._course_description = course_description

    def get_professor_id(self):
        pass

    def add_course(self, course_info):
        # insert into Courses(course_info + professor_id)
        pass