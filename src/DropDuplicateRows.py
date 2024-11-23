import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'])
    return customers


if __name__ == "main":
    customers = {
        "customer_id": [1, 2, 3, 4, 5, 6],
        "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        "email": ["emily@example.com", "michael@example.com", "sarah@example.com", "john@example.com",
                  "john@example.com", "alice@example.com"]
    }
    customers = pd.DataFrame(customers)
    print(dropDuplicateEmails(customers))

# https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/