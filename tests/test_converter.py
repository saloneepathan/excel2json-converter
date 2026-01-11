from excel2json.converter import excel_to_json


def test_excel_to_json():
    json_data = excel_to_json("examples/sample.xlsx")
    assert json_data is not None
