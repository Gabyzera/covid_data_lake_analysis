us_states_vaccinated_per_hundred_query = """
    WITH RankedVaccinations AS (
        SELECT 
            location,
            AVG(people_fully_vaccinated_per_hundred) AS average_fully_vaccinated_per_hundred,
            ROW_NUMBER() OVER (ORDER BY AVG(people_fully_vaccinated_per_hundred) DESC) AS rn_desc,
            ROW_NUMBER() OVER (ORDER BY AVG(people_fully_vaccinated_per_hundred) ASC) AS rn_asc
        FROM 
            "covid-19"."owid_us_state_vaccinations"
        WHERE 
            location <> 'United States' AND 
            date_parse(date, '%Y-%m-%d') BETWEEN date '2022-12-01' AND date '2022-12-31'
        GROUP BY 
            location
        )
        SELECT location, average_fully_vaccinated_per_hundred
        FROM RankedVaccinations
        WHERE rn_desc <= 10 OR rn_asc <= 10;
"""