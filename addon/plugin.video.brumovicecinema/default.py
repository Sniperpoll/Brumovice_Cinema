import xbmcplugin
import xbmcgui
import xbmcaddon
import sys

addon = xbmcaddon.Addon()
handle = int(sys.argv[1])

xbmcplugin.endOfDirectory(handle)
