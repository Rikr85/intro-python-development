

########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.urlencode({
    # Request parameters
    'features': '{array}',
    'model-version': 'latest',
    'language': 'en',
    'smartcrops-aspect-ratios': '{array}',
    'gender-neutral-caption': 'False',
})

try:
    conn = httplib.HTTPSConnection('*.cognitiveservices.azure.com')
    conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2024-02-01&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'features': '{array}',
    'model-version': 'latest',
    'language': 'en',
    'smartcrops-aspect-ratios': '{array}',
    'gender-neutral-caption': 'False',
})

try:
    conn = http.client.HTTPSConnection('*.cognitiveservices.azure.com')
    conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2024-02-01&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

