import argparse
from excel2json.converter import excel_to_json
from excel2json.utils import print_success, print_error


def main():
    parser = argparse.ArgumentParser(
        description="Convert Excel files to JSON"
    )

    parser.add_argument(
        "excel",
        help="Path to Excel file"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output JSON file path",
        default="output.json"
    )

    parser.add_argument(
        "-s",
        "--sheet",
        help="Sheet name or index",
        default=0
    )

    parser.add_argument(
        "--orient",
        help="JSON orientation",
        default="records"
    )

    args = parser.parse_args()

    try:
        excel_to_json(
            excel_path=args.excel,
            output_path=args.output,
            sheet_name=args.sheet,
            orient=args.orient
        )
        print_success(f"JSON file created: {args.output}")

    except Exception as e:
        print_error(str(e))


if __name__ == "__main__":
    main()
