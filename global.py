from modules import sendData
import sys
import os

if __name__ == '__main__':
    argvs = ["apikey", "url", "name", "value"]
    if len(sys.argv) == len(argvs):
        try:
            sendData.sendData(base_url=url, api_key=apikey, name=name, value=value)
        except exception as e:
            print('error')
    else:
        print("{0}:[{1}] [{2}] [{3}] [{4}]".format(os.path.basename(__file__), argvs[0], argvs[1], argvs[2], argvs[3]))