from fredapi import Fred
import pandas as pd
from string import ascii_uppercase


fred = Fred(api_key='')
ip = fred.get_series('GDPA')

print ip


#https://github.com/mortada/fredapi
