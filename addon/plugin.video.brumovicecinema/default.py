import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
import urllib.parse

addon = xbmcaddon.Addon()
handle = int(sys.argv[1])
base_url = sys.argv[0]

def build_url(query):
    return base_url + '?' + urllib.parse.urlencode(query)

def main_menu():
    items = [
        ("Vyhledávání", "search"),
        ("Filmy", "movies"),
        ("Seriály", "tvshows"),
        ("TV Program", "tvguide"),
        ("Trakt.tv", "trakt"),
        ("TMDB", "tmdb"),
        ("ČSFD", "csfd"),
        ("Nastavení", "settings"),
    ]
    for label, action in items:
        url = build_url({"action": action})
        li = xbmcgui.ListItem(label)
        xbmcplugin.addDirectoryItem(handle, url, li, True)
    xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main_menu()
