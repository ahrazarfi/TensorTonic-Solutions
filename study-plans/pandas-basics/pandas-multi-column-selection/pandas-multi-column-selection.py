import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """
    # sanayya
    df = pd.DataFrame(data)
    selected_columns = df[columns]
    return selected_columns.to_dict(orient='list')
