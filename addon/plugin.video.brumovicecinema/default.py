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
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "search"}),
        xbmcgui.ListItem(label="Vyhledávání"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "movies"}),
        xbmcgui.ListItem(label="Filmy"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "tvshows"}),
        xbmcgui.ListItem(label="Seriály"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "tvguide"}),
        xbmcgui.ListItem(label="TV Program"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "trakt"}),
        xbmcgui.ListItem(label="Trakt.tv"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "tmdb"}),
        xbmcgui.ListItem(label="TMDB"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "csfd"}),
        xbmcgui.ListItem(label="ČSFD"),
        isFolder=True
    )
    xbmcplugin.addDirectoryItem(
        handle,
        build_url({"action": "settings"}),
        xbmcgui.ListItem(label="Nastavení"),
        isFolder=True
    )

    xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main_menu()
