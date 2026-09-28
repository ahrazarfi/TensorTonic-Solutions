import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    # Sanayya
    df = pd.DataFrame(data)
    _dict = {"values": df[column].to_list(), "length": len(df[column])}
    return _dict
