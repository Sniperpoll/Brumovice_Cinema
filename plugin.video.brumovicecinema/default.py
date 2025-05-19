import sys
import xbmcplugin
import xbmcgui
import xbmcaddon

# Inicializace
addon = xbmcaddon.Addon()
addon_handle = int(sys.argv[1])
base_url = sys.argv[0]

# Získání přihlašovacích údajů
username = addon.getSetting('ws_username')
password = addon.getSetting('ws_password')

# Vytvoření základního menu
def main_menu():
    xbmcplugin.setPluginCategory(addon_handle, 'Brumovice Cinema')
    xbmcplugin.setContent(addon_handle, 'videos')

    # Přidáme položku "Ověřit přihlášení"
    li = xbmcgui.ListItem(label='🔐 Ověřit přihlášení')
    url = f'{base_url}?action=login'
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

# Hlavní vstup
if __name__ == '__main__':
    main_menu()
