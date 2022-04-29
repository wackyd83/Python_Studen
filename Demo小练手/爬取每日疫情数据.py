import requests
import pprint
import json
import pandas as pd


url=r'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&_=1638361173347'

response=requests.get(url)

json_data=response.json()['data']



json_data=json.loads(json_data)
json_data=json_data['areaTree'][0]['children']
pprint.pprint(json_data)
# data_set=[]
# for i in json_data:
#     data_dict={}
#     data_dict['province']=i['name']  #省份
#     data_dict['nowConfirm']=i['total']['nowConfirm']  #现有确诊
#     data_dict['dead']=i['total']['dead']  #死亡人数
#     data_dict['heal']=i['total']['heal']  #康复人数
#     data_dict['deadRate']=i['total']['deadRate']  #死亡率
#     data_set.append(data_dict)
#
#
# df=pd.DataFrame(data_set)
#
# df.to_csv('data.csv')
# df.set_index(['province'],inplace=True)
# print(df.head(10))