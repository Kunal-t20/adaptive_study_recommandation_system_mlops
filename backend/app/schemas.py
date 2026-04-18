from pydantic import BaseModel

class StudentInput(BaseModel):
    StudyHours: float
    Attendance: float
    Resources: int
    Extracurricular: int
    Motivation: int
    Internet: int
    Gender: int
    Age: int
    LearningStyle: int
    OnlineCourses: int
    Discussions: int
    AssignmentCompletion: int
    EduTech: int
    StressLevel: int


class FeedbackInput(BaseModel):
    StudyHours: float
    Attendance: float
    Resources: int
    Extracurricular: int
    Motivation: int
    Internet: int
    Gender: int
    Age: int
    LearningStyle: int
    OnlineCourses: int
    Discussions: int
    AssignmentCompletion: int
    EduTech: int
    StressLevel: int
    predicted: int
    actual: int