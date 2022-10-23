# TODO
# 1. Callendar
# 2. Heatmap
# 3. News

from treco.core import HEADERS, MAIN_URL, get_data_from_tables
from treco.core import get_data_from_stream


def news(amount=10, country="NULL", category="NULL"):
    return get_data_from_stream(size=amount, country=country, category=category)


def heatmap(region=""):
    get_args = "?g=" + region.lower()
    url = MAIN_URL + "matrix" + get_args
    ret_val = get_data_from_tables(url)
    return ret_val


def _experimental_calendar():
    url = MAIN_URL + "calendar"
    ret_val = get_data_from_tables(url)
    return ret_val
