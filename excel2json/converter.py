import pandas as pd
from pathlib import Path


def excel_to_json(
    excel_path: str,
    output_path: str = None,
    sheet_name=0,
    orient: str = "records"
):
    """
    Convert Excel file to JSON.

    Args:
        excel_path (str): Path to Excel file
        output_path (str): Path to output JSON file
        sheet_name (str|int): Sheet name or index
        orient (str): JSON format orientation

    Returns:
        str: JSON string
    """
    excel_path = Path(excel_path)

    if not excel_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_path}")

    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    json_data = df.to_json(orient=orient, indent=4)

    if output_path:
        output_path = Path(output_path)
        output_path.write_text(json_data, encoding="utf-8")

    return json_data
