def process_cases_and_deaths_response(raw_response, state_label: str, month_label: str, deaths_label: str, cases_label: str):
    processed_data = []
    
    for row in raw_response['ResultSet']['Rows'][1:]:
        month = row['Data'][1]['VarCharValue']
        state_name = row['Data'][0]['VarCharValue']
        total_cases = float(row['Data'][2]['VarCharValue'])
        total_deaths = float(row['Data'][3]['VarCharValue'])
        
        data_dict = {
            state_label: state_name,
            month_label: month,
            cases_label: total_cases,
            deaths_label: total_deaths
        }
        
        processed_data.append(data_dict)
        
    return processed_data