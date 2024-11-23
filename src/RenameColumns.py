import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace=True)
    return students


if __name__ == "main":
    students = {
        "id": [846, 749, 155, 160],
        "first": ["Mason", "Riley", "Bob", None],
        "last": ["AAA", "BBB", "CCC", "DDD"],
        "age": [21, 30, 28, 25]
    }
    students = pd.DataFrame(students)
    print(renameColumns(students))
