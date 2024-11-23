import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # raises exception
    # students = students[students['name'] is not None]

    students = students[students['name'].notna()]

    return students


if __name__ == "main":
    students = {
        "student_id": [846, 749, 155, 160],
        "name": ["Mason", "Riley", "Bob", None],
        "age": [21, 30, 28, 25]
    }
    students = pd.DataFrame(students)
    print(dropMissingData(students))
