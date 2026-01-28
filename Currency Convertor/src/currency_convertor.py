import requests
from cachetools import cached, TTLCache

ttl_cache = TTLCache(1000, 30)
@cached(ttl_cache)
def get_currencies_info(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    exchange_rate = response.json()['rates'][target_currency]
    time_last_updated = response.json()['time_last_updated']
    if response.status_code == 200:
        return exchange_rate, time_last_updated
    
    return None
        

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate
