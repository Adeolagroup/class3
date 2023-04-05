import requests
import json
import pandas as pd
#org_names = []
org_id = []
Fetch_Info = False
page = 1
while Fetch_Info == False:
    url = "https://192.168.1.103/api/v2/organizations/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/credentials/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/teams/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/inventories/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/inventory_scripts/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/job_templates/?page="+str(page)
#    url = "https://192.168.1.103/api/v2/projects/?page="+str(page)
    print(url)
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url=url,auth=("admin","password"),headers=headers)
    if res.status_code == 200:

        result = res.json()
        # print(result)
        for i in range(len(result['results'])):
#            Tower_Organization_name = result['results'][i]['name']
#            Tower_Credentials_name = result['results'][i]['name']
#            Tower_Teams_name = result['results'][i]['name']
#            Tower_inventories_name = result['results'][i]['name']
#            Tower_inventory_scripts_name = result['results'][i]['name']
#            Tower_job_templates_name = result['results'][i]['name']
#            Tower_projects_name = result['results'][i]['name']
            Tower_projects_id = result['results'][i]['id']
            org_id.append(Tower_projects_id)
#            json_file = {"Organization": Tower_Organization_name}
#            json_file = {"Credentials": Tower_Credentials_name}
#            json_file = {"Teams": Tower_Teams_name}
#            json_file = {"Inventories": Tower_inventories_name}
#            json_file = {"Inventory_scripts": Tower_inventory_scripts_name}
#            json_file = {"Templates": Tower_job_templates_name}
#            json_file = {"Projects": Tower_projects_name}
#            org_names.append(json_file)


        page =page+1
    else:
        break
for i in range(len(org_id)):
    url = "https://192.168.1.103/api/v2/organizations/(org_id[i])/users/"
# print(org_names)
# with open('totalprojects.json', 'w') as jout:
#     json.dump(org_names, jout)
# jobs = open("totalprojects.json", encoding="utf-8-sig")
# info = json.load(jobs)
# df = pd.json_normalize(info)
# df.to_csv("totalprojects.csv", index=False)




print(org_id)
# with open('totaluserid.json', 'w') as jout:
#     json.dump(org_id, jout)
# jobs = open("totaluserid.json", encoding="utf-8-sig")
# info = json.load(jobs)
# df = pd.json_normalize(info)
# df.to_csv("totaluserid.csv", index=False)
