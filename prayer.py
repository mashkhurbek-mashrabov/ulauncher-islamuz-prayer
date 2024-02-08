import requests
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem


class UserLanguage:
    ENGLISH = 'en'
    UZBEK = 'uz'

    def get_lang(self, language: str):
        if language == 'en':
            return self.ENGLISH
        elif language == 'uz':
            return self.UZBEK


class Prayer:
    def __init__(self, location: str, language: UserLanguage):
        self.location = location
        self.language = language
        self.fajr_time = ""
        self.sunrise_time = ""
        self.dhuhr_time = ""
        self.asr_time = ""
        self.maghrib_time = ""
        self.isha_time = ""
        self.date = ""
        self.hij_date = ""
        self.get_prayer_time()

    def get_prayer_time(self):
        response = requests.get(self.api_maker())
        if response.status_code == 200:
            data = response.json()
            self.date = data['date']
            self.hij_date = f"{data['hijri_date']['day']} {data['hijri_date']['month'].capitalize()}"
            times = data["times"]
            self.fajr_time = times['tong_saharlik']
            self.sunrise_time = times['quyosh']
            self.dhuhr_time = times['peshin']
            self.asr_time = times['asr']
            self.maghrib_time = times['shom_iftor']
            self.isha_time = times['hufton']
        else:
            raise Exception("Request failed: %s" % response.status_code)

    def get_fajr_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Bomdod"
        else:
            return "Fajr"

    def get_sunrise_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Quyosh"
        else:
            return "Sunrise"

    def get_dhuhr_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Peshin"
        else:
            return "Dhuhr"

    def get_asr_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Asr"
        else:
            return "Asr"

    def get_maghrib_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Shom"
        else:
            return "Maghrib"

    def get_isha_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Hufton"
        else:
            return "Isha"

    def get_hij_date_name(self):
        if self.language == UserLanguage.UZBEK:
            return "Hijriy sana"
        else:
            return "Hijri Date"

    def api_maker(self):
        return f"https://islomapi.uz/api/present/day?region={self.location}"

    def get_result_list(self):
        items = []

        items.append(
            ExtensionResultItem(icon='images/calendar.png',
                                name=f"{self.get_hij_date_name()} : {self.hij_date}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/fajr.png',
                                name=f"{self.get_fajr_name()} : {self.fajr_time}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/sunrise.png',
                                name=f"{self.get_sunrise_name()} : {self.sunrise_time}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/dhuhr.png',
                                name=f"{self.get_dhuhr_name()} : {self.dhuhr_time}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/asr.png',
                                name=f"{self.get_asr_name()} : {self.asr_time}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/maghrib.png',
                                name=f"{self.get_maghrib_name()} : {self.maghrib_time}",
                                on_enter=HideWindowAction()))

        items.append(
            ExtensionResultItem(icon='images/isha.png',
                                name=f"{self.get_isha_name()} : {self.isha_time}",
                                on_enter=HideWindowAction()))

        return items
