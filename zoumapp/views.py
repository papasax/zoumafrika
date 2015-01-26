import urllib2
from bs4 import BeautifulSoup

from django.http.response import HttpResponse
from xml.dom.minidom import parseString
import xml.dom.minidom


def home(request):
    url = "http://alexandredesenfant.wix.com/zoumafrika"
    if request.method == 'GET':
        try:
            page = urllib2.urlopen(url).read()
        except urllib2.URLError, e:
            pass
        page=page.replace("http://www.wix.com/favicon.ico","http://zoumafrika.com/favicon.ico")
        soup = BeautifulSoup(page)
        soup.select('#wixFooter')[0].extract()
        soup.select('script')[2].append('setTimeout(function(){myChildNode = document.getElementById("WIX_ADS");myChildNode.parentNode.removeChild(myChildNode);}, 3000);')
        htmlclean=str(soup)
        return HttpResponse(htmlclean)
    elif request.method == 'POST':
        try:
            newrequest = urllib2.Request(dir, request.POST, headers={})
            response = urllib2.urlopen(newrequest).read()
        except urllib2.URLError, e:
            pass
        return HttpResponse(response)

