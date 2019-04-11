from src.services.tickets import get_tickets_since
from src.helpers.export import csv_export

a = get_tickets_since("2019-04-01")
csv_export('data/export.csv', a[0])
