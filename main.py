from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from prayer import Prayer


class PrayerExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        location = extension.preferences["location"]
        language = extension.preferences["language"]
        prayer = Prayer(location, language)
        return RenderResultListAction(prayer.get_result_list())


if __name__ == '__main__':
    PrayerExtension().run()
