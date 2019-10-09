import aliyun.api
import urllib.request
import json


class DNS:
    jsonFile = open('key.json')
    s = json.load(jsonFile)
    aliyun.setDefaultAppInfo(str(s['id']), str(s['secret']))

    def getDNSIp(self):
        b = aliyun.api.Dns20150109DescribeDomainRecordInfoRequest()
        try:
            f = b.getResponse()
            return str(f.get('Value'))
        except Exception as e:
            print('getDNSIp:', e)
            return None

    def getMyIp(self):
        try:
            u = urllib.request.urlopen('http://members.3322.org/dyndns/getip')
            return u.read().strip('\n')
        except Exception as e:
            print('getMyIp:', e)
            return None

    def main(self, newIp):
        a = aliyun.api.Dns20150109UpdateDomainRecordRequest(newIp)
        a.DBInstanceId = ""
        try:
            print("start")
            f = a.getResponse()
            print(f)
        except Exception as e:
            print('main:', e)


if __name__ == '__main__':
    d = DNS()
    oldip = d.getDNSIp()
    newip = d.getMyIp()
    if oldip != newip and oldip is not None:
        print('oldIp:', oldip)
        print('newIp:', newip)
        d.main(newip)
