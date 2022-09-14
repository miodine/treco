import core
import debug_tools
from forecasts import currencies_forecast
import indicators

print("STARTING TESTS")
df = core.get_data_from_lists(
    'https://tradingeconomics.com/earnings')
print(df)

df_ind = indicators.countries_by_indicator('gdp growth rate')

df_fore = currencies_forecast()
