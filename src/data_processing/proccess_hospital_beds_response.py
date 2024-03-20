def process_hospital_beds_response(raw_response, x_label, y_label):
    processed_data = []
    
    for row in raw_response['ResultSet']['Rows'][1:]:
        state = row['Data'][0]['VarCharValue']
        total_beds = int(row['Data'][1]['VarCharValue'])
        
        processed_data.append({x_label: state, y_label: total_beds})
        
    return processed_data