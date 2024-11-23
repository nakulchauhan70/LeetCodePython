import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students = students[students['student_id'] == 101]
    # students = students.iloc[:, 0:2]

    students = students[['name', 'age']]
    return students


if __name__ == "main":
    students = {
        "student_id": [846, 749, 155, 160],
        "name": ["Mason", "Riley", "Bob", None],
        "age": [21, 30, 28, 25]
    }
    students = pd.DataFrame(students)
    print(selectData(students))
