#From pyinsee package

# Subscribe to api.insee.fr and get your credentials!
# Save your credentials with init_conn function :

# from pynsee.utils.init_conn import init_conn
# init_conn(insee_key="my_insee_key", insee_secret="my_insee_secret")

# Beware : any change to the keys should be tested after having cleared the cache
# Please do : from pynsee.utils import clear_all_cache; clear_all_cache()"

from pynsee.macrodata import get_dataset_list, get_series_list, get_series
import pandas as pd

# get macroeconomic datasets list
insee_dataset = get_dataset_list()

