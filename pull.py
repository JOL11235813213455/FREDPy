from fredapi import Fred
import pandas as pd
from string import ascii_uppercase


fred = Fred(api_key='47df1dd2cde5f239d39b2e750c64de83')
ip = fred.get_series('GDPA')

print ip


#https://github.com/mortada/fredapi
