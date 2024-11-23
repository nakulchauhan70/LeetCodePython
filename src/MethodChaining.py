import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100]
    animals = animals.sort_values(by=['weight'], ascending=False)
    animals_name = animals[['name']]
    return animals_name
