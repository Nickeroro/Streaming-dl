import re
import sys
import youtube_dl
import urllib.request
from bs4 import BeautifulSoup
#install ffmpeg

def excract_iframe_from_url(url):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    fp = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(fp)
    mybytes = BeautifulSoup(response.read(), "html.parser");
    #print(mybytes)
    # mystr = mybytes.decode("utf8")
    # response.close()
    #for iframe in mybytes.find_all('iframe', src=True):
    #    print("Found the URL:", iframe['src'])
    iframe = mybytes.iframe

    match = re.search('src="([^"]+)"', str(iframe))
    #print(iframe)
    url_without_http = (match[0])[5:][:-1]
    url_to_dl = 'https:'+url_without_http

    url_to_dl_formated = url_to_dl.replace('&', '"&"')

    print('url: ' + url_to_dl)
    return url_to_dl_formated


def dl_from_url(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])





cmdargs = str(sys.argv[1])
iframe_url = excract_iframe_from_url(cmdargs)
dl_from_url(iframe_url)
# print(html)

