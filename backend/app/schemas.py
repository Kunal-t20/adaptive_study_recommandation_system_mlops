from pydantic import BaseModel

class StudentInput(BaseModel):
    StudyHours: float
    Attendance: float
    Resources: int
    Extracurricular: int
    Motivation: int
    Internet: int
    Age: int
    LearningStyle: int
    OnlineCourses: int
    Discussions: int
    AssignmentCompletion: int
    EduTech: int
    StressLevel: int


class FeedbackInput(StudentInput):
    predicted: int
    actual: int