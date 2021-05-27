from csv import DictWriter
import requests
import json
import time
import calendar
count=0

while True:
    with open('craw_1000.csv', 'a+', newline='') as write_obj:
        fieldnames = ['No','cBB', 'cmd', 'd1', 'd2', 'd3', 'gBB', 'iJp', 'tJpV', 'tUB', 'tUS', 'timestamp', 'error']
        dict_writer = DictWriter(write_obj, fieldnames=fieldnames)
        try:
            response = requests.get("https://api-agent.gowsazhjo.tv/glms/v1/notify/taixiu")
            text = json.dumps(response.json(), sort_keys=True, indent=4)
            data = json.loads(text)
            employee_data = data['data']
            for emp in employee_data:
                if(emp['cmd']==1003):
                    ts = calendar.timegm(time.gmtime())
                    emp['timestamp']=ts
                    emp['No']=count
                    dict_writer.writerow(emp)
                    count+=1
                    print(count)
                    time.sleep(60)
        except:
            ts = calendar.timegm(time.gmtime())
            dict_writer.writerow({'error': ts})
            time.sleep(60)
