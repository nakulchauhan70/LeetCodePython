import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


if __name__ == "main":
    employees = {
        "name": ["Mason", "Riley", "Bob", "Mia"],
        "salary": [21, 30, 28, 25],
    }

    employees = pd.DataFrame(employees)
    print(modifySalaryColumn(employees))
