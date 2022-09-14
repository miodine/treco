from core import *


def forecasts_by_country(country):
    url = MAIN_URL + '/' + country.replace(' ', '-') + '/forecasts'
    forecast_lists = get_data_from_tables(url)
    return forecast_lists


def countries_by_forecast(indicator: str, region='World', format='pandas'):
    url = MAIN_URL + '/forecast/' + indicator.lower().replace(' ', '-') + \
        '?continent=' + region
    indicator_by_country_list = get_data_from_tables(url)
    return indicator_by_country_list


def currencies_forecast(fmt):
    ret_val = scrape_specific_data('/forecast/currency', fmt)
    return ret_val


def stock_indices_forecast(fmt):
    ret_val = scrape_specific_data('/forecast/stock-market', fmt)
    return ret_val


def commodities_forecast(fmt):
    ret_val = scrape_specific_data('/forecast/commodity', fmt)
    return ret_val


def bonds_forecast(fmt, show_all=True):
    if show_all == True:
        ret_val = scrape_specific_data('/forecast/government-bond-10y', fmt)
        return ret_val


def crypto_forecast(fmt):
    ret_val = scrape_specific_data('/forecast/crypto', fmt)
    return ret_val
