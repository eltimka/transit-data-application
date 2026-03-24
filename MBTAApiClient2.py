import urllib.request, json
import mysqldb2
from datetime import datetime

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            
            # Original fields you had
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['bearing'] = bus['attributes']['bearing']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['label'] = bus['attributes']['label']
            busDict['route_id'] = bus['relationships']['route']['data']['id']
            busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
            
            # Additional fields from JSON
            busDict['vehicle_type'] = bus.get('type', 'vehicle')
            busDict['speed'] = bus['attributes'].get('speed')
            busDict['current_status'] = bus['attributes'].get('current_status')
            busDict['occupancy_status'] = bus['attributes'].get('occupancy_status')
            busDict['revenue'] = bus['attributes'].get('revenue')

            busDict['stop_id'] = bus['relationships']['stop']['data']['id']    
            busDict['trip_id'] = bus['relationships']['trip']['data']['id']
            busDict['updated_at'] = bus['attributes'].get('updated_at')
            
            mbtaDictList.append(busDict)
    
    mysqldb2.insertMBTARecord(mbtaDictList) 
    return mbtaDictList
