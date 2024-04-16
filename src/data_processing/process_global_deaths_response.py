def process_global_deaths_response(raw_response, country_label, month_label, total_deaths_label):
    processed_data = []

    for row in raw_response[1:]:
        data = row['Data']
        
        if len(data) < 3:
            continue  

        country_name = data[0].get('VarCharValue', '')
        month = data[1].get('VarCharValue', '')
        deaths_on_end_of_month = data[2].get('VarCharValue', '')

        # Lidar com erros
        try:
            total_deaths = float(deaths_on_end_of_month)
        except ValueError:
            continue 

        processed_data.append({
            country_label: country_name,
            month_label: month,
            total_deaths_label: total_deaths
        })
        
    return processed_data