from core import *


def currencies(fmt):
    ret_val = scrape_specific_data('/currencies', fmt)
    return ret_val


def stock_indices(fmt):
    ret_val = scrape_specific_data('/stocks', fmt)
    return ret_val


def commodities(fmt):
    ret_val = scrape_specific_data('/commodities', fmt)
    return ret_val


def bonds(fmt, show_all=True):
    if show_all == True:
        ret_val = scrape_specific_data('/bonds', fmt)
        return ret_val


def crypto(fmt):
    ret_val = scrape_specific_data('/crypto', fmt)
    return ret_val
