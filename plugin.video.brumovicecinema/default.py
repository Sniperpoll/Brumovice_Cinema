import sys
import urllib.parse
import xbmcplugin
import xbmcgui
import xbmcaddon
import requests

# Inicializace
addon = xbmcaddon.Addon()
addon_handle = int(sys.argv[1])
base_url = sys.argv[0]
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))

# Získání přihlašovacích údajů
username = addon.getSetting('ws_username')
password = addon.getSetting('ws_password')

# Přihlášení k Webshare API
def login_to_webshare():
    url = 'https://webshare.cz/api/login/'
    data = {'username': username, 'password': password}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200 and 'token' in response.json():
            token = response.json()['token']
            xbmcgui.Dialog().notification('Brumovice Cinema', 'Přihlášení OK ✅', xbmcgui.NOTIFICATION_INFO, 3000)
        else:
            xbmcgui.Dialog().notification('Brumovice Cinema', 'Chyba přihlášení ❌', xbmcgui.NOTIFICATION_ERROR, 3000)
    except Exception as e:
        xbmcgui.Dialog().notification('Chyba', str(e), xbmcgui.NOTIFICATION_ERROR, 5000)

# Základní menu
def main_menu():
    xbmcplugin.setPluginCategory(addon_handle, 'Brumovice Cinema')
    xbmcplugin.setContent(addon_handle, 'videos')

    li = xbmcgui.ListItem(label='🔐 Ověřit přihlášení')
    url = f'{base_url}?action=login'
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

# Hlavní vstup
if __name__ == '__main__':
    action = params.get('action')
    if action == 'login':
        login_to_webshare()
    else:
        main_menu()
