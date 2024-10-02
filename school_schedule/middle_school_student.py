from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, get_transportation=False):
        super().__init__(name, grade, classes)
        self.get_transportation = get_transportation if get_transportation else []
    
    def display_transportation_message(self):
        has_message = "has" if self.get_transportation else "doesn't have"
        return f"{self.name} {has_message} transportation"
    
    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()
        return "\n".join((student_summary, transportation_message))

n = MiddleSchoolStudent("John", "6th", ["Geography"], get_transportation=False)
