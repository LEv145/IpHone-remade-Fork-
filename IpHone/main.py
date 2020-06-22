import requests

class Ip():
    def __init__(self, ip):
        self._ip = ip
    def get_ip(self):
        response = requests.get(f'http://ipinfo.io/{self._ip}/json')

        data = ['ip','city','region','country','loc','org','timezone']

        out_data = []

        for elem in data:
            try:
                out_data.append(response.json()[elem])
            except KeyError:
                out_data.append("Не найдено")





        print(f"""
    [INFORMATION ABOUT IP: {out_data[0]}]
    ===================================
    CITY: {out_data[1]}
    REGION: {out_data[2]}
    COUNTRY: {out_data[3]}
    LOCATION: {out_data[4]}
    TIMEZONE: {out_data[5]}""")

class Phone():
    def __init__(self, phone):
        self._phone = phone
    def get_phone(self):
        response            = requests.get(f'https://htmlweb.ru/geo/api.php?json&telcod={self._phone}')

        try:
            user_city           = response.json()['capital']['english']
        except KeyError:
            user_city = "Не найдено"
        try:
            user_region         = response.json()['country']['id']
        except KeyError:
            user_region = "Не найдено"
        try:
            user_country        = response.json()['country']['english']
        except KeyError:
            user_country = "Не найдено"
        try:
            user_w, user_h      = response.json()['capital']['latitude'], response.json()['capital']['longitude']
        except KeyError:
            user_w, user_h = "Не найдено"
        try:
            user_post           = response.json()['capital']['post']
        except KeyError:
            user_post = "Не найдено"
        try:
            user_operator       = response.json()['0']['oper']
        except KeyError:
            user_operator = "Не найдено"


        print(f"""
    [INFORMATION ABOUT PHONE: {self._phone}]
    ===================================
    CITY: {user_city}
    REGION: {user_region}
    COUNTRY: {user_country}
    LOCATION: {user_w} {user_h}
    """)
