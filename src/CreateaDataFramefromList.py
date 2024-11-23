from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return student_df


if __name__ == "main":
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]

    print(createDataframe(student_data))
