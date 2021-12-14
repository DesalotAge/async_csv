"""Define all celery tasks for working in this app."""
import csv
from celery import shared_task


@shared_task
def sum_csv_file(filename: str) -> float:
    """Sum every ten-th column in csv file."""
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        # extracting field names through first row
        rez = float(0)
        for row in csvreader:
            # first column is date so we will count all from 11 column
            for num in row[10::10]:
                # trying to convert string to float
                try:
                    rez += float(num)
                except ValueError:
                    """If num is not float number it will be cause of this exception."""
        return rez
