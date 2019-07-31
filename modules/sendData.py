import requests

def sendData(base_url:str, api_key:str, name:str, value:int):
    try:
        url = "{0}/{1}/{2}".format(base_url,name,value)
        headers = {'x-api-key':'{0}'.format(api_key)}
        r = requests.get(url,headers=headers)
        print(r.content)
    except Exception as e:
        print(e)