def process_total_vaccinations_and_people_fully_vaccinated_response(raw_response, location_label, total_vaccinations_label, people_fully_vaccinated_label):
    processed_data = []

    if not all(isinstance(row, dict) and 'Data' in row for row in raw_response):
        raise ValueError("Unexpected data format in raw_response")

    for row in raw_response[1:]:  # Assuming the first row is headers
        if not isinstance(row['Data'], list) or len(row['Data']) < 3:
            continue  # Skip rows that do not have the expected format

        data = row['Data']
        try:
            location = data[0]['VarCharValue']
            total_vaccinations = int(data[1]['VarCharValue'])
            people_fully_vaccinated = int(data[2]['VarCharValue'])

            processed_data.append({
                location_label: location,
                total_vaccinations_label: total_vaccinations,
                people_fully_vaccinated_label: people_fully_vaccinated
            })
        except (ValueError, KeyError) as e:
            print(f"Error processing row {data}: {e}")
    
    return processed_data
