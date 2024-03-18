def process_hospital_beds_response(raw_response):
    processed_data = []
    
    for row in raw_response['ResultSet']['Rows'][1:]:
        state = row['Data'][0]['VarCharValue']
        total_beds = int(row['Data'][1]['VarCharValue'])
        
        processed_data.append({'state': state, 'total_staffed_beds': total_beds})
        
    return processed_data