import argparse
import csv
import json
import os

def csv_to_json(data):
    # Read CSV data
    reader = csv.DictReader(data.splitlines())

    # Convert CSV data to a JSON format
    return json.dumps([row for row in reader], indent=4)

def csv_to_html(data):
    # Convert CSV data to HTML table format
    reader = csv.reader(data.splitlines())
    html = "<table>\n"
    for row in reader:
        html += "  <tr>\n"
        for col in row:
            html += f"    <td>{col}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

def parse_prn(data):
    # Parse PRN data
    lines = data.split('\n')
    if lines[0].startswith('SEP='):
        sep = lines[0].replace('SEP=', '')
        lines = [line.split(sep) for line in lines[1:] if line.strip()]
    else:
        lines = [line.split('\t') for line in lines if line.strip()]
    return lines

def prn_to_json(data):
    # Convert PRN data to a JSON format
    prn_data = parse_prn(data)
    headers = prn_data[0]
    result = []
    for values in prn_data[1:]:
        result.append(dict(zip(headers, values)))
    return json.dumps(result, indent=4)

def prn_to_html(data):
    # Convert PRN data to HTML table format
    prn_data = parse_prn(data)
    html = "<table>\n"
    for i, row in enumerate(prn_data):
        html += "  <tr>\n"
        for col in row:
            html += f"    <td>{col}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

def main():
    parser = argparse.ArgumentParser(description="Convert CSV or PRN files to JSON or HTML")
    parser.add_argument("format", choices=["json", "html"], help="Output format: json or html")
    parser.add_argument("file", help="Path to the input file")
    args = parser.parse_args()

    # Read data from the input file
    with open(args.file, 'r') as file:
        data = file.read()

    # Determine the file extension
    _, file_extension = os.path.splitext(args.file)
    file_extension = file_extension[1:].lower()

    # Convert based on format option and file extension
    if args.format == "json":
        if file_extension == "prn":
            result = prn_to_json(data)
        else:
            result = csv_to_json(data)  
    else:
        if file_extension == "prn":
            result = prn_to_html(data)
        else:
            result = csv_to_html(data)

    print(result)

if __name__ == "__main__":
    main()
