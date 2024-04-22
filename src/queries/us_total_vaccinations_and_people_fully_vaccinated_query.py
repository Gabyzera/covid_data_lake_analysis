us_total_vaccinations_and_people_fully_vaccinated_query = """
    SELECT 
        location,
        MAX(total_vaccinations) as total_vaccinations,
        MAX(people_fully_vaccinated) as people_fully_vaccinated
    FROM 
        "covid-19"."owid_us_state_vaccinations"
    WHERE 
        location <> 'United States'
    GROUP BY 
        location
    """