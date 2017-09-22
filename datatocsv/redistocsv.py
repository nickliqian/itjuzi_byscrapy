#coding=utf-8
import redis
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = redis.Redis(host='127.0.0.1', port=6379)


with open('itjuzidata.csv','w') as f:
	writer = csv.writer(f)
	for i in range(16680):
            r = client.lindex("juzi:items",i)
            if r == None:
                break
	    data = str(r)
	    dic  = json.loads(data)
	    if i == 0:
	    	writer.writerow(dic.keys())
	    else:
                dic['companyName'] = dic['companyName'][0]
	    	tag = ''
                for i in dic['tag']:
                    tag += i+ ','
                dic['tag'] = tag
                writer.writerow(dic.values())
