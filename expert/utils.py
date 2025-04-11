import pandas as pd
from typing import List, Dict, Any

def load_apps_info(file_name: str = "AppleStore.csv") -> pd.DataFrame:
    """
    Load the apps information from a CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing app information.
    """
    return pd.read_csv(file_name)

