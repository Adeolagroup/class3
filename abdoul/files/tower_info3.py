import requests
import json
import pandas as pd
org_names = []
Fetch_Info = False
page = 1
while Fetch_Info == False:
#    url = "https://192.168.1.103/api/v2/organizations/?page="+str(page)
    url = "https://192.168.1.103/api/v2/hosts/?page="+str(page)
    print(url)
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url=url,auth=("admin","password"),headers=headers)
    if res.status_code == 200:

        result = res.json()
        # print(result)
        for i in range(len(result['results'])):
#            Tower_Organization_name = result['results'][i]['name']
            Tower_Hosts_name = result['results'][i]['name']
#            json_file = {"Organization": Tower_Organization_name}
            json_file = {"Hosts": Tower_Hosts_name}
            org_names.append(json_file)


        page =page+1
    else:
        break
print(org_names)
with open('totalHosts_awx.com.json', 'w') as jout:
    json.dump(org_names, jout)
jobs = open("totalHosts_awx.com.json", encoding="utf-8-sig")
info = json.load(jobs)
df = pd.json_normalize(info)
df.to_csv("totalHosts_awx.com.csv", index=False)
