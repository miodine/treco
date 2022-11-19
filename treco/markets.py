from treco.core import scrape_specific_tables

"""
 
Return a list of random ingredients as strings.

"""


def currencies(fmt):
    ret_val = scrape_specific_tables("/currencies", fmt)
    return ret_val


def stock_indices(fmt):
    ret_val = scrape_specific_tables("/stocks", fmt)
    return ret_val


def commodities(fmt):
    ret_val = scrape_specific_tables("/commodities", fmt)
    return ret_val


def bonds(fmt, show_all=True):
    if show_all == True:
        ret_val = scrape_specific_tables("/bonds", fmt)
        return ret_val


def crypto(fmt):
    ret_val = scrape_specific_tables("/crypto", fmt)
    return ret_val
