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
        soup = BeautifulSoup(page)
        #pub
        soup.select('script')[2].append('setTimeout(function(){myNode = document.getElementById("WIX_ADSdesktopTopAd");nbNodes=myNode.childNodes.length; for (var i=0;i<nbNodes;i++){myNode.removeChild(myNode.childNodes[0]);} }, 3000);')
        #favicon
        soup.select('script')[2].append('setTimeout(function(){el = document.getElementsByTagName("link");for (var i=0;i<el.length;i++){if (el[i].rel=="shortcut icon"){el[i].href="http://zoumafrika.com/favicon.ico";}}}, 3000);')
        htmlclean=str(soup)
        return HttpResponse(htmlclean)
    elif request.method == 'POST':
        try:
            newrequest = urllib2.Request(dir, request.POST, headers={})
            response = urllib2.urlopen(newrequest).read()
        except urllib2.URLError, e:
            pass
        return HttpResponse(response)

