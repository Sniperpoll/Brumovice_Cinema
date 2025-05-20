import sys
import urllib.parse
import xbmcplugin
import xbmcgui
import xbmcaddon

addon_handle = int(sys.argv[1])
xbmcplugin.setPluginCategory(addon_handle, 'Brumovice Cinema')
xbmcplugin.setContent(addon_handle, 'videos')

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main_menu():
    items = [
        {'label': '🎬 Filmy', 'action': 'movies'},
        {'label': '📺 Seriály', 'action': 'series'},
        {'label': '🔍 Vyhledávání', 'action': 'search'},
        {'label': '⭐ Oblíbené', 'action': 'favorites'},
        {'label': '📂 Databáze', 'action': 'database'},
        {'label': '📺 TV Program', 'action': 'tvguide'},
        {'label': '⚙️ Nastavení', 'action': 'settings'}
    ]

    for item in items:
        url = build_url({'action': item['action']})
        list_item = xbmcgui.ListItem(label=item['label'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

def database_menu():
    sources = [
        {'label': '🎯 Trakt.tv', 'source': 'trakt'},
        {'label': '🎞️ ČSFD', 'source': 'csfd'},
        {'label': '🎬 TMDB', 'source': 'tmdb'}
    ]

    for item in sources:
        url = build_url({'action': 'database_source', 'source': item['source']})
        list_item = xbmcgui.ListItem(label=item['label'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

if __name__ == '__main__':
    args = urllib.parse.parse_qs(sys.argv[2][1:])
    action = args.get('action', [None])[0]

    if action is None:
        main_menu()
    elif action == 'database':
        database_menu()
    elif action == 'settings':
        xbmcaddon.Addon().openSettings()
    elif action == 'tvguide':
        xbmcgui.Dialog().notification("Brumovice Cinema", "TV Program zatím není implementován.", xbmcgui.NOTIFICATION_INFO, 3000)
        xbmcplugin.endOfDirectory(addon_handle)
    elif action == 'database_source':
        source = args.get('source', [''])[0]
        xbmcgui.Dialog().notification("Brumovice Cinema", f"Otevřena sekce: {source}", xbmcgui.NOTIFICATION_INFO, 3000)
        xbmcplugin.endOfDirectory(addon_handle)