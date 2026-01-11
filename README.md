# 📊 excel2json-converter

A simple, lightweight Python utility to convert Excel files (`.xlsx`, `.xls`)
into JSON format using Pandas.

---

## 🚀 Features

- Convert Excel to JSON in one command
- Supports multiple sheets
- CLI + Python API
- Clean project structure
- Ready for GitHub & PyPI

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/your-username/excel2json-converter.git
cd excel2json-converter
```

## Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Usage
### Command Line
```bash
python main.py data.xlsx -o output.json
```

### With options
```bash
python main.py data.xlsx \
  --output result.json \
  --sheet Sheet1 \
  --orient records
```

### As a Python Module
```bash
from excel2json.converter import excel_to_json

json_data = excel_to_json("data.xlsx", "output.json")
```

## 🔧 JSON Orient Options
Orient	Description
records	List of row objects
split	Dict with index, columns, data
index	Dict by index
columns	Dict by columns
values	Array only

## 🧪 Running Tests
```bash
pytest
```

## 📂 Example

Input Excel:

name	age	city
John	25	NY
Anna	30	LA

Output JSON:

[
  {
    "name": "John",
    "age": 25,
    "city": "NY"
  },
  {
    "name": "Anna",
    "age": 30,
    "city": "LA"
  }
]

## 📜 License

MIT License

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

## ⭐ Support

If you find this project useful, give it a ⭐ on GitHub!