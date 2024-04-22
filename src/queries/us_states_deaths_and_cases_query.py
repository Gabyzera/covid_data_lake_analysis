us_states_deaths_and_cases_query = """
    SELECT
        state_name,
        date_format(date_trunc('month', cast(date as date)), '%m/%Y') AS month,
        SUM(cases) AS total_cases,
        SUM(deaths) AS total_deaths
    FROM
        "covid-19"."enigma_aggregation_us_states"
    WHERE
        date_trunc('month', cast(date as date)) > date '2020-02-01'
    GROUP BY
        state_name,
        date_format(date_trunc('month', cast(date as date)), '%m/%Y')
    ORDER BY
        state_name,
        date_format(date_trunc('month', cast(date as date)), '%m/%Y') ASC;
""" 