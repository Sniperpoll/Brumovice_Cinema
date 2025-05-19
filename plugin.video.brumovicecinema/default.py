import sys
import xbmcplugin
import xbmcgui
import xbmcaddon

# Inicializace
addon = xbmcaddon.Addon()
addon_handle = int(sys.argv[1])
base_url = sys.argv[0]

def main_menu():
    xbmcplugin.setPluginCategory(addon_handle, 'Brumovice Cinema')
    xbmcplugin.setContent(addon_handle, 'videos')

    li = xbmcgui.ListItem(label='✅ Addon běží – klikni pro test hlášky')
    url = f'{base_url}?action=test'
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

def show_message():
    xbmcgui.Dialog().notification('Brumovice Cinema', 'Addon funguje správně ✅', xbmcgui.NOTIFICATION_INFO, 4000)

if __name__ == '__main__':
    import urllib.parse
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    action = params.get('action')
    if action == 'test':
        show_message()
    else:
        main_menu()
