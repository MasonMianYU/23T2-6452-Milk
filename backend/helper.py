import cx_Oracle

def get_records(farmer_id, processor_id, distributor_id, retailer_id, packager_id, conn):
    result = []
    cursor = conn.cursor()
    cursor.execute("""
        SELECT FARMER_ADDRESS, FARMER_CONTACT, PRODUCING_DATE, COW_HEALTH_REORD
        FROM FARMER
        WHERE FARMER_ID = :farmer_id
    """, {'farmer_id': farmer_id})
    tmp = cursor.fetchone()
    if tmp is not None:
        tmp = list(tmp)
        tmp.insert(0, 'farmer')
        result.append(tmp)
    cursor.execute("""
        SELECT DISTRIBUTOR_ADDRESS, DISTRIBUTOR_CONTACT, DISTRIBUTOR_DATE
        FROM DISTRIBUTOR
        WHERE DISTRIBUTOR_ID = :distributor_id
    """, {'distributor_id': distributor_id})
    tmp = cursor.fetchone()
    if tmp is not None:
        tmp = list(tmp)
        tmp.insert(0, 'distributor')
        result.append(tmp) 
    cursor.execute("""
        SELECT PROCESSOR_ADDRESS, PROCESSOR_CONTRACT, PROCESSOR_DATE, PROCESSOR_METHOD
        FROM PROCESSOR
        WHERE PROCESSOR_ID = :processor_id
    """, {'processor_id': processor_id})
    tmp = cursor.fetchone()
    if tmp is not None:
        tmp = list(tmp)
        tmp.insert(0, 'processor')
        result.append(tmp)
    cursor.execute("""
        SELECT RETAILER_ADDRESS, RETAILER_CONTACT, RECEIVED_DATE
        FROM RETAILER
        WHERE RETAILER_ID = :retailer_id
    """, {'retailer_id': retailer_id})
    tmp = cursor.fetchone()
    if tmp is not None:
        tmp = list(tmp)
        tmp.insert(0, 'retailer')
        result.append(tmp)
    cursor.execute("""
        SELECT PACKAGER_ADDRESS, PACKAGER_CONTACT, PACKAGE_DATE
        FROM PACKAGER
        WHERE PACKAGER_ID = :packager_id
    """, {'packager_id': packager_id})
    tmp = cursor.fetchone()
    if tmp is not None:
        tmp = list(tmp)
        tmp.insert(0, 'packager')
        result.append(tmp)
        
    result.sort(key=lambda x: x[3])
    for i in range(len(result)):
        result[i][3] = result[i][3].strftime('%Y-%m-%d')
    
    return result