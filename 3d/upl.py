# -*- coding: utf-8 -*-


url_dst = 'http://demo-threedim.staging.nextgis.com/api'
ngw_creds = ('administrator', 'admin')
feature_dst = '/resource/' + '1501' + '/feature/'   #layer id
new_id = '/33'          #feature id


import os
import requests
import json
cmd = 'python3 geojson2ngw.py --url http://demo-threedim.staging.nextgis.com --login administrator --password admin --parent 0 --debug --folder "Демо" --create --folder lenino-dachnoe'
print(cmd)
#os.system(cmd)

'''

'''


def upload_3d_model(url_dst,filepath,ngw_creds,name,parent_id):
    with open(filepath,'rb') as f:
        put_url = url_dst + '/component/file_upload/'
        print('upload '+filepath + ' to '+put_url)
        #req = requests.put(put_url, data=f, auth=ngw_creds)
        req = requests.put(put_url, data=f, auth=ngw_creds)
        
        json_data = req.json()
        json_data['name'] = name
        
        tdmd = {}
        tdmd['resource'] = {}
        tdmd['resource']['cls']='model_3d'
        tdmd['resource']['display_name']=name
        tdmd['resource']['parent']={}
        tdmd['resource']['parent']['id']=parent_id
        tdmd['model_3d']={}
        tdmd['model_3d']['file_upload']=json_data
        
        post_url = url_dst +'/resource/'
        print()
        print('make POST')
        
        print('POST '+post_url)
        print(json.dumps(tdmd, indent=2))
        req = requests.post(post_url, data=json.dumps(tdmd), auth=ngw_creds)
        print(req.content)
        '''
        

curl --user "administrator:demodemo" -H "Accept: */*" -X POST   -d '{'cls': 'model_3d', 'display_name': 'namehere', 'parent': {'id': 8}, 'model_3d': {'id': 'e11898f8-22a9-4ed8-a15a-ca81813df5d9', 'mime_type': 'text/plain', 'size': 863110, 'name': '1-510 3 entrances'}} ' http://demo-threedim.staging.nextgis.com/api/resource/
curl --user "administrator:admin" -H "Accept: */*" -X POST   -d '{"resource":{"cls": "model_3d", "display_name": "namehere", "parent": {"id": 8"}, "model_3d": {"id": "c44d59ce-9ede-481f-9c52-3b69402ee983", "mime_type": "text/plain", "size": 863110, "name": "1-510 3 entrances"}}} ' http://demo-threedim.staging.nextgis.com/api/resource/
   '''
        
upload_3d_model(url_dst=url_dst,filepath='models-export/1-510_3entrances.glb',ngw_creds=ngw_creds,name='1-510 3 entrances',parent_id=8)