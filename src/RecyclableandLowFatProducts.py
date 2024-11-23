import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products.category == 'N') & (products.low_fats == 'N')].filter(items=['product_id'])


if __name__ == "main":
    data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
    products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
        {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})

    print(find_products(products))
