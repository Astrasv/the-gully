import pandas as pd
import ast

def clean_list_string(val):
    """Converts string representation of lists to actual lists, returns None for NULLs."""
    # Since we use dtype=str, we check for string versions of nulls
    if pd.isna(val) or val == "" or str(val).lower() == "nan" or val == "[]" or val is None:
        return None  
    
    try:
        # If it looks like a list string "['item']", convert it
        if isinstance(val, str) and val.startswith('['):
            return ast.literal_eval(val)
        # If it's already a list, return it
        if isinstance(val, list):
            return val
        # Otherwise wrap the value in a list (for single name strings)
        return [val]
    except (ValueError, SyntaxError):
        return [val]