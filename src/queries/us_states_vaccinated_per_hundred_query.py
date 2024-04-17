us_states_vaccinated_per_hundred_query = """
    SELECT 
        location,
        AVG(people_fully_vaccinated_per_hundred) AS average_fully_vaccinated_per_hundred
    FROM 
        "covid-19"."owid_us_state_vaccinations"
    WHERE 
        location <> 'United States' AND 
        date_parse(date, '%Y-%m-%d') BETWEEN date '2022-12-01' AND date '2022-12-31'
    GROUP BY 
        location
    ORDER BY 
        RAND()
    LIMIT 20;
"""