import requests


class Language:
    ENGLISH = 'en'
    UZBEK = 'uz'


# prayer_times.py (update)

class PrayerTimes:
    PRAYER_NAMES = {
        Language.ENGLISH: {
            'fajr': 'Fajr',
            'sunrise': 'Sunrise',
            'dhuhr': 'Dhuhr',
            'asr': 'Asr',
            'maghrib': 'Maghrib',
            'isha': 'Isha',
            'hij_date': "Hijri Date"
        },
        Language.UZBEK: {
            'fajr': 'Bomdod',
            'sunrise': 'Quyosh',
            'dhuhr': 'Peshin',
            'asr': 'Asr',
            'maghrib': 'Shom',
            'isha': 'Hufton',
            'hij_date': "Hijriy Sana"
        },
    }

    def __init__(self, times: dict):
        self.times = times

    def get_time(self, key: str) -> str:
        return self.times['times'].get(key, "")

    def get_hijri_date(self) -> str:
        hijri_date = self.times.get('hijri_date', {})
        day = hijri_date.get('day', '')
        month = hijri_date.get('month', '').capitalize()
        return f"{day} {month}"

    def get_prayer_name(self, prayer_key: str, language: str) -> str:
        language_prayers = self.PRAYER_NAMES.get(language, {})
        return language_prayers.get(prayer_key.lower(), "")


class PrayerAPI:
    BASE_URL = "https://islomapi.uz/api/present/day"

    def __init__(self, location: str):
        self.location = location

    def get_prayer_times(self) -> dict:
        response = requests.get(f"{self.BASE_URL}?region={self.location}")
        response.raise_for_status()  # Raise an exception for non-200 responses
        return response.json()


class PrayerService:
    def __init__(self, location: str, language: str):
        self.location = location
        self.language = language

    def get_prayer_times(self) -> PrayerTimes:
        api = PrayerAPI(self.location)
        times_data = api.get_prayer_times()
        return PrayerTimes(times_data)
