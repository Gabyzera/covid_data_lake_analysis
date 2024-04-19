us_first_and_second_dose_pfizer_vaccine_query = """
    SELECT
        jurisdiction,
        week_of_allocations,
        SUM(first_dose_allocations) AS total_first_doses,
        SUM(second_dose_allocations) AS total_second_doses
    FROM
        "covid-19"."cdc_pfizer_vaccine_distribution"
    GROUP BY
        jurisdiction,
        week_of_allocations
    ORDER BY
        week_of_allocations, jurisdiction;
"""