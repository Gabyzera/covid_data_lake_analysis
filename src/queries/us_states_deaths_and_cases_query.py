us_states_deaths_and_cases_query = """
    SELECT
        state_name,
        date_format(cast(date as date), '%Y-%m') AS month,
        SUM(cases) AS total_cases,
        SUM(deaths) AS total_deaths
    FROM
        "covid-19"."enigma_aggregation_us_states"
    GROUP BY
        state_name,
        date_format(cast(date as date), '%Y-%m')
    ORDER BY
        state_name,
        month;
""" 