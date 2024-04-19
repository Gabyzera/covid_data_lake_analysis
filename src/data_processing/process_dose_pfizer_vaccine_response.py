def process_vaccine_allocation_data(raw_response, jurisdiction_label, week_of_allocations_label, first_dose_allocations_label, second_dose_allocations_label):
    processed_data = []
    
    for row in raw_response[1:]:
        jurisdiction = row['Data'][0]['VarCharValue']
        week_of_allocations = row['Data'][1]['VarCharValue']
        first_doses_allocations = row['Data'][2]['VarCharValue']
        second_doses_allocations = row['Data'][3]['VarCharValue']
        
        try:
            first_doses_allocations = int(first_doses_allocations)
            second_doses_allocations = int(second_doses_allocations)
        except ValueError:
            continue
        
        processed_data.append({
            jurisdiction_label : jurisdiction,
            week_of_allocations_label: week_of_allocations,
            first_dose_allocations_label: first_doses_allocations,
            second_dose_allocations_label: second_doses_allocations
        })
    
    return processed_data
