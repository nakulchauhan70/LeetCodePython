import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.loc[products['quantity'].isna(), 'quantity'] = 0
    return products


if __name__ == "main":
    products = {
        "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
        "quantity": [None, None, 779, 849],
        "price": [135, 821, 9319, 3051]
    }
    products = pd.DataFrame(products)
    print(fillMissingValues(products))
