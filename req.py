import requests


def available_valute(curr=False):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    valute_keys = list(res["Valute"].keys())
    valute_info = 'Список доступных валют: \n'
    if curr:
        for i in valute_keys:
            valute_info += f'{i} - {res["Valute"][i]["Name"]} - {res["Valute"][i]["Value"]}' + '\n'
        return valute_info
    else:
        for i in valute_keys:
            valute_info += f'{i} - {res["Valute"][i]["Name"]}' + '\n'
            return valute_info


def valute(code):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    valute_keys = list(res["Valute"].keys())
    if code in valute_keys:
        return f'{res["Valute"][code]["Name"]} - {res["Valute"][code]["Value"]}'
    else:
        return 'Неправильный код валюты'
