import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MyNewPass",
        database="MBTAdb",
        port=3308
    )

    mycursor = mydb.cursor()
    
    # Updated SQL with ALL fields from your adjusted code
    sql = """INSERT INTO mbta_buses ( 
        id, longitude, latitude, bearing, direction_id, label, route_id, current_stop_sequence,
        vehicle_type, speed, current_status, occupancy_status, revenue, stop_id, trip_id, updated_at
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )"""
    
    for mbtaDict in mbtaList:
        # Updated values tuple with ALL fields from your adjusted code
        val = (
            mbtaDict['id'], 
            mbtaDict['longitude'], 
            mbtaDict['latitude'],  
            mbtaDict['bearing'],
            mbtaDict['direction_id'], 
            mbtaDict['label'], 
            mbtaDict['route_id'], 
            mbtaDict['current_stop_sequence'],
            mbtaDict.get('vehicle_type'),
            mbtaDict.get('speed'),
            mbtaDict.get('current_status'),
            mbtaDict.get('occupancy_status'),
            mbtaDict.get('revenue'),
            mbtaDict.get('stop_id'),
            mbtaDict.get('trip_id'),
            mbtaDict.get('updated_at')
        )
        mycursor.execute(sql, val)

    mydb.commit()
