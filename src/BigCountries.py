import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # return world[(world.population >= 25000000) | (world.area  >= 3000000)].filter(items=['name', 'population', 'area'])
    world = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    world = world[['name', 'population', 'area']]
    return world


if __name__ == "main":
    data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
            ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
            ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
    world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
        {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

    print(big_countries(world))

# NOTE: 3 million no mentioned in if condition is wrong in problem statement
