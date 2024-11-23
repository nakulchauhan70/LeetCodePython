import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2], axis=0)
    return df


if __name__ == "main":
    employees1 = {
        "name": ["Mason", "Riley", "Bob", "Mia"],
        "salary": [21, 30, 28, 25],
    }

    employees2 = {
        "name": ["Mason", "Riley", "Bob", "Mia"],
        "salary": [21, 30, 28, 25],
    }

    employees1 = pd.DataFrame(employees1)
    employees2 = pd.DataFrame(employees2)
    print(concatenateTables(employees1, employees2))
