from treco.core import *


def indicators_by_country(country):
    url = MAIN_URL + "/" + country.replace(" ", "-") + "/indicators"
    indicator_lists = get_data_from_tables(url)
    return indicator_lists


def countries_by_indicator(indicator: str, region="World"):

    url = (
        MAIN_URL
        + "/country-list/"
        + indicator.lower().replace(" ", "-")
        + "?continent="
        + region
    )
    indicator_by_country_list = get_data_from_tables(url)
    return indicator_by_country_list
