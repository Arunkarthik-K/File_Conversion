# File_Conversion

## Steps to run:
1. Download the python file **"convert.py"**
2. Make this python file as an executable one by using the command line **'chmod +x convert.py'**
3. Now you can use the below mentioned cmd line to convert the files without any data loss.

## cmd line:
>*To convert from csv to html*
1. cat incident.csv | python3 convert.py html incident.csv > csv_html.html
>*To convert from csv to json*
2. cat incident.csv | python3 convert.py json incident.csv > csv_json.json
>*To convert from prn to html*
3. cat incident.prn | python3 convert.py html incident.prn > prn_html.html
>*To convert from prn to json*
4. cat incident.prn | python3 convert.py json incident.prn > prn_json.json
