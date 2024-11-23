import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


if __name__ == "main":
    students = {
        "student_id": [846, 749, 155, 160],
        "name": ["Mason", "Riley", "Bob", None],
        "age": [21, 30, 28, 25],
        "grade": [73.0, 87.0, 99.9, 101.23]
    }

    students = pd.DataFrame(students)
    print(changeDatatype(students))
