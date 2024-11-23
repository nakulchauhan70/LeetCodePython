from typing import List

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row_len = len(players.index)
    col_len = len(players.columns)

    return [row_len, col_len]


if __name__ == "main":
    players = {
        "player_id": [846, 749, 155],
        "name": ["Mason", "Riley", "Bob"],
        "age": [21, 30, 28]
    }
    print(getDataframeSize(players))
