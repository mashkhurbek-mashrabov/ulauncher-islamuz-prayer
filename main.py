from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from prayer import Language, PrayerService


class PrayerExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        location = extension.preferences["location"]
        language = extension.preferences["language"]

        if language not in [Language.ENGLISH, Language.UZBEK]:
            language = Language.ENGLISH  # Default to English if an invalid language is selected

        prayer_service = PrayerService(location, language)
        prayer_times = prayer_service.get_prayer_times()

        return RenderResultListAction([
            ExtensionResultItem(icon='images/calendar.png',
                                name=f"{prayer_times.get_prayer_name('hij_date', language)} : {prayer_times.get_hijri_date()}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/fajr.png',
                                name=f"{prayer_times.get_prayer_name('fajr', language)} : {prayer_times.get_time('tong_saharlik')}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/sunrise.png',
                                name=f"{prayer_times.get_prayer_name('sunrise', language)} : {prayer_times.get_time('quyosh')}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/dhuhr.png',
                                name=f"{prayer_times.get_prayer_name('dhuhr', language)} : {prayer_times.get_time('peshin')}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/asr.png',
                                name=f"{prayer_times.get_prayer_name('asr', language)} : {prayer_times.get_time('asr')}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/maghrib.png',
                                name=f"{prayer_times.get_prayer_name('maghrib', language)} : {prayer_times.get_time('shom_iftor')}",
                                on_enter=HideWindowAction()),
            ExtensionResultItem(icon='images/isha.png',
                                name=f"{prayer_times.get_prayer_name('isha', language)} : {prayer_times.get_time('hufton')}",
                                on_enter=HideWindowAction())
        ])


if __name__ == '__main__':
    PrayerExtension().run()
