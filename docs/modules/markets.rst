from treco.core import scrape_specific_tables

# treco.markets 

## Module description 

Set of functions allowing to get the current values of
real asset related quantities.  

The functions return lists of tables.
The data in each table is formatted in a fixed way; 
that is:

1. Name of the indicator
2. Actual value (price, ratio, quotation etc.)

3. Point-wise change daily
4. Percentage change daily
5. Percentage change weekly
6. Percentage change monthly
7. Percentage YoY 
8. Today's date.





def currencies(fmt):
     
        ## Description

        Returns FX currency prices, as a list-of-tables. 
        Each entry in the list correspond to different geographic region.      

        ## Parameters

        fmt : desired output dataframe format

        ## Returns

        ret_val : dataframe with currency pair ratios

        

    ret_val = scrape_specific_tables("/currencies", fmt)
    return ret_val


def stock_indices(fmt):
    
    ## Description 

    provides stock market indexes quotes for several countries including the latest price, yesterday 
    session close, plus weekly, monthly and yearly percentage changes.
    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with stock indices

    

    ret_val = scrape_specific_tables("/stocks", fmt)
    return ret_val


def commodities(fmt):
    
    ## Description 

    Provides current commodity prices.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with major comodity prices

    

    ret_val = scrape_specific_tables("/commodities", fmt)
    return ret_val


def bonds(fmt):
    
    ## Description 

    Provides current prices for global bond market.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with bonds data

    

    ret_val = scrape_specific_tables("/bonds", fmt)
    return ret_val


def crypto(fmt):
    
    ## Description

    Provides current prices for major cryptocurrencies.

    ## Parameters 

    fmt : desired output dataframe format

    ## Returns

    ret_val : dataframe with cryptocurrency data 

    

    ret_val = scrape_specific_tables("/crypto", fmt)
    return ret_val
