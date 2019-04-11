from dateutil.parser import parse
import json
import datetime


class MySQLDateTimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(MySQLDateTimeEncoder, self).default(obj)


def str_to_mysql_datetime(datetimestr):
    datetime = parse(datetimestr)
    str_datetime = datetime.strftime("%Y-%m-%d %H:%M:%S")
    return str_datetime


def date_to_mysql_datetime(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")
