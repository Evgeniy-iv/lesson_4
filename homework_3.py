from decimal import Decimal
from requests import get, utils
from datetime import datetime


def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    if content.find(char_code.upper()) != -1:  # Чтобы функция принимала аргумент в любом регистре используется метод
        # строки upper
        number_of_occurrences = content.count('<CharCode>', 0, content.index(char_code.upper()))
        rate = content.split('<Value>')[number_of_occurrences].split('</Value>')[0]
        valute_name = content.split('<Name>')[number_of_occurrences].split('</Name>')[0]
        date_rate = content.split('Date="')[1].split('"')[0]
        date_rate = date_rate.split('.')
        date_rate.reverse()
        date_rate = '-'.join(date_rate)

        date_time_obj = datetime.strptime(date_rate, '%Y-%m-%d')

        rate = rate.replace(',', '.')
        #    rate = float(rate)
        rate = Decimal(rate)  # Здесь используется импортированный из модуля decimal тип Decimal
        print(valute_name)
        print(rate, date_time_obj.date())
        print(type(rate))
    else:
        return None


currency_rates("USD")  # курс доллара
currency_rates("EUR")  # курс евро
