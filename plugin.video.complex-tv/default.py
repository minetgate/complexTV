# Author : Pablo Mendez
# Company: Complex Media Inc
# 
# This addon is for free and redistribution . 	
#

import urllib2
import json
import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

#get the video list from oayalla.
complexNews = 'http://cdn-api.ooyala.com/v2/syndications/88af49794d964697ac4bdefd076f95e0/feed?pcode=ttYTMxOmh-6nk2wKZI-ih5W1iWxx'

#complexCDN = 'http://cdn-api.ooyala.com/v2/syndications/6fa7cb50ad2e40bda2007743062957b1/feed?pcode=ttYTMxOmh-6nk2wKZI-ih5W1iWxx'

response = urllib2.urlopen(complexNews)

html = response.read()
stream =  json.loads(html)

# add the videos to the playlist.

for videos in stream['media']:

    li = xbmcgui.ListItem(videos['title'], iconImage='DefaultVideo.png', thumbnailImage=videos['thumbURL'])
    
    li.setProperty('fanart_image', videos['thumbURL'])
    
    li.addStreamInfo('video', { 'codec': 'h264', 'aspect': 1.78, 'width': 1280, 'height': 720 })
    
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=videos['videoURL'], listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

## Settings about to develop

#my_addon = xbmcaddon.Addon()
#my_setting = my_addon.getSetting('complex_setting') # returns the string 'true' or 'false'
#my_addon.setSetting('complex_setting', 'false')
