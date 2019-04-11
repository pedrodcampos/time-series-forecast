
from ..database.tickets import get_tickets_brand_level_since as _get_tickets_brand_level_since
from ..helpers.parser import str_to_mysql_datetime


def get_tickets_since(datetimestamp):
    datetime = str_to_mysql_datetime(datetimestamp)
    return _get_tickets_brand_level_since(datetime)
