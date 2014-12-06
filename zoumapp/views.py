import urllib2

from django.http.response import HttpResponse


def home(request):
    url = "http://alexandredesenfant.wix.com/zoumafrika"
    if request.method == 'GET':
        try:
            result = urllib2.urlopen(url)
        except urllib2.URLError, e:
            pass
        html=result.read()
        htmlclean=html.replace('<div comp="wysiwyg.viewer.components.WixAds" skin="wysiwyg.viewer.skins.wixadsskins.WixAdsWebSkin" id="wixFooter"></div>','')
        htmlclean=htmlclean.replace("http://www.wix.com/favicon.ico","http://zoumafrika.com/lyon.ico")
        return HttpResponse(htmlclean)
    elif request.method == 'POST':
        try:
            newrequest = urllib2.Request(dir, request.POST, headers={})
            response = urllib2.urlopen(newrequest).read()
        except urllib2.URLError, e:
            pass
        return HttpResponse(response)

