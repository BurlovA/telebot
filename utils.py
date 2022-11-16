import requests
import json

class ConvertException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):


if len(values) > 3:
    raise ConvertException('Слишком много параметров')
quote, base, amount = values
if quote == base:
    raise ConvertException(f'Невозможно перевести одинаковые валюты {base}')
try:
    quote_ticket = keys[quote]
except KeyError:
    raise ConvertException(f'Не удалось обработать валюту {quote}')

try:
    base_ticket = keys[base]
except KeyError:
    raise ConvertException(f'Не удалось обработать валюту {base}')
try:
    amount = float(amount)
except ValueError:
    raise ConvertException(f'Не удалось обработать количетсво {amount}')


