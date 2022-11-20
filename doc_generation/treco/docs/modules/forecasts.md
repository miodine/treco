from treco.core import MAIN_URL, get_data_from_tables, scrape_specific_tables


# treco.forecasts

## Module description

Functions for getting forecast on 
1. macro-economic indicators
2. real asset related quantities.  




def forecasts_by_country(region):
    
    ## Description 
    Forecast for all macro-economic indicators related to given country/region/area.

    ## Parameters
    region : geographical region name.

    ## Returns

    
    url = MAIN_URL + "/" + region.replace(" ", "-") + "/forecasts"
    forecast_lists = get_data_from_tables(url)
    return forecast_lists


def countries_by_forecast(indicator: str, scope="World"):
    
    ## Description 

    Returns a forecast of one selected indicator for multiple all the regions in given scope.

    ## Parameters 
    indicator : name of the indicator to search for.
    scope : geographical cluster of countries.

    ## Returns
    region_forecast_by_one_indicator : self explanatory.
    

    url = (
        MAIN_URL
        + "/forecast/"
        + indicator.lower().replace(" ", "-")
        + "?continent="
        + scope
    )
    region_forecast_by_one_indicator = get_data_from_tables(url)
    return region_forecast_by_one_indicator


def currencies_forecast(fmt):
     
        ## Description

        Returns forecast of FX currency prices, as a list-of-tables. 
        Each entry in the list correspond to different geographic region.      

        ## Parameters

        fmt : desired output dataframe format

        ## Returns

        ret_val : dataframe with currency pair ratios forecast

        

    ret_val = scrape_specific_tables("/forecast/currency", fmt)
    return ret_val


def stock_indices_forecast(fmt):
    
    ## Description 

    Provides forecast for stock market indexes quotes for several countries including the latest price, yesterday 
    session close, plus weekly, monthly and yearly percentage changes.
    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with stock indices forecast

    
    ret_val = scrape_specific_tables("/forecast/stock-market", fmt)
    return ret_val


def commodities_forecast(fmt):
    
    ## Description 

    Provides forecast for the comodity prices.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with major comodity prices forecast

    
    ret_val = scrape_specific_tables("/forecast/commodity", fmt)
    return ret_val


def bonds_forecast(fmt, show_all=True):
    
    ## Description 

    Provides forecast for the bond prices.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with bonds data forecast

    

    if show_all == True:
        ret_val = scrape_specific_tables("/forecast/government-bond-10y", fmt)
        return ret_val


def crypto_forecast(fmt):
    
    ## Description 

    Provides crypto forecast.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with cryptocurrency data forecast

    

    ret_val = scrape_specific_tables("/forecast/crypto", fmt)
    return ret_val
