from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

import json

class CodeCoverage(Extension):

    def __init__(self):
        super(CodeCoverage, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        prefs = extension.preferences
        options = json.loads(prefs['cc_mapping'])
        filePath = prefs['cc_filepath']
        for key,value in options.items():
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='%s' % key,
                                             description='View Code coverage for %s' % value,
                                             on_enter=OpenUrlAction(filePath % value)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    CodeCoverage().run()
