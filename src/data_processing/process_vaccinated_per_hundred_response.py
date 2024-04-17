def process_vaccinated_per_hundred_response(raw_response, location_label, average_fully_vaccinated_per_hundred_label):
    processed_data = []
    
    for row in raw_response[1:]:
        location = row['Data'][0]['VarCharValue']
        average_fully_vaccinated_per_hundred = row['Data'][1]
        
        if 'VarCharValue' not in average_fully_vaccinated_per_hundred:
            continue
        
        average_fully_vaccinated_per_hundred = average_fully_vaccinated_per_hundred['VarCharValue']
        
        try:
            average_fully_vaccinated_per_hundred = float(average_fully_vaccinated_per_hundred)
        except ValueError:
            continue  
        
        processed_data.append({
            location_label: location,
            average_fully_vaccinated_per_hundred_label: average_fully_vaccinated_per_hundred
        })
    
    return processed_data