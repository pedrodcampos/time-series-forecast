import csv
from datetime import datetime
from src.helpers.parser import date_to_mysql_datetime


def csv_export(filename, data, header=True):

    with open(filename, 'w+') as csv_file:
        writer = csv.writer(csv_file)
        if header:
            item_keys = data[0].keys()
            writer.writerow(item_keys)

        for row in data:
            cell_values = []
            for _, value in row.items():
                if isinstance(value, datetime):
                    value = date_to_mysql_datetime(value)
                cell_values.append(value)
            writer.writerow(cell_values)
