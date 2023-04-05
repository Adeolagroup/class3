import requests
import json
import pandas as pd
org_data = []
Fetch_Info = False
page = 1
while Fetch_Info == False:
#    url = "https://192.168.1.103/api/v2/organizations/?page="+str(page)
    url = "https://192.168.1.103/api/v2/organizations/?page="+str(page)
    print(url)
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url=url,auth=("admin","password"),headers=headers)
    if res.status_code == 200:

        result = res.json()
        # print(result)
        for i in range(len(result['results'])):
            org_output={}
#            Tower_Organization_name = result['results'][i]['name']
            org = result['results'][i]
            org_output['name']=org['name']
            categories_and_urls = [(link, org['related'][link]) for link in org['related'] if link in ['inventories', 'job_templates', 'projects', 'credentials','teams','admins','users']]
            for category, url in categories_and_urls:
                related = requests.get(url='https://192.168.1.103'+url,auth=("admin","password"),headers=headers).json()['results']
                org_output[category]=[]
                for item in related:
                    org_output[category].append(item['name' if category not in ['users', 'admins'] else 'username'])
            org_data.append(org_output)
        page =page+1
    else:
        break
print(org_data)
with open('totalinfos.json', 'w') as jout:
    json.dump(org_data, jout)
df = pd.json_normalize(org_data)
df.to_csv("totalinfos.csv", index=False)
