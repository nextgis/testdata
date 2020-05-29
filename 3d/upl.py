# -*- coding: utf-8 -*-


url_dst = 'http://demo-threedim.staging.nextgis.com/api'
ngw_creds = ('administrator', 'admin')
feature_dst = '/resource/' + '1501' + '/feature/'   #layer id
new_id = '/33'          #feature id


import os
import requests
cmd = 'python3 geojson2ngw.py --url http://demo-threedim.staging.nextgis.com --login administrator --password admin --parent 0 --debug --folder "Демо" --create --folder lenino-dachnoe'
print(cmd)
#os.system(cmd)

'''

'''


def upload_3d_model(url_dst,filepath,ngw_creds,name,parent_id):
    with open(filepath) as f:
        req = requests.put(url_dst + '/component/file_upload/upload', data=f, auth=ngw_creds)
        
        json_data = req.json()
        json_data['name'] = name
        
        tdmd = {}
        tdmd['cls']='model_3d'
        tdmd['parent']['id']=parent_id
        tdmd['model_3d']=json_data
        
        
        print(tdmd)
        req = requests.post(url_dst + str(parent_id), data=json.dumps(tdmd), auth=ngw_creds)
        
upload_3d_model(url_dst=url_dst,filepath='models-export/1-510_3entrances.glb',ngw_creds=ngw_creds,name='1-510 3 entrances',parent_id=8)