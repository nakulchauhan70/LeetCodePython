import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_melt = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return report_melt


if __name__ == "main":
    report = {
        "product ": ["Umbrella", "SleepingBag"],
        "quarter_1": [417, 800],
        "quarter_2": [224, 936],
        "quarter_3": [379, 93],
        "quarter_4": [611, 875]
    }
    report = pd.DataFrame(report)
    print(meltTable(report))
