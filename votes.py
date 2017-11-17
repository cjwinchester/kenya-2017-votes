import csv
from tabula import convert_into


def extract_data():
    """dump data from pdf to csv"""
    convert_into('kv.pdf', 'kv.csv', output_format='csv', pages='all')


def valid_row(row):
    return row[0] != '' and row[0][0].isnumeric()


def clean_row(row):
    for i, item in enumerate(row):

        row[i] = item.replace(',', '')

        if item in ['', '-']:
            row[i] = 0

    return row


def parse_csv():
    """parse csv into a clean file"""

    with open('kv.csv', 'r') as infile, open('kv-parsed.csv', 'w') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if valid_row(row):
                split_list = [x.replace('BARINGO  NORTH', 'BARINGO NORTH')
                               .split('  ') for x in row]
                flat_list = [y for z in split_list for y in z]

                clean_list = clean_row(flat_list)

                writer.writerow(clean_list[:15])


if __name__ == '__main__':
    extract_data()
    parse_csv()
