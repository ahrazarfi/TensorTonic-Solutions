import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    # sanayya
    df = pd.DataFrame(data)
    return {
      "data": df.to_dict("list"),
      "shape": list(df.shape),
      "columns": list(df.columns)
      }