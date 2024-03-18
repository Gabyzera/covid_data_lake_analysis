hospital_beds_query = """
    SELECT hq_state, SUM(num_staffed_beds) AS total_staffed_beds
    FROM "covid-19"."hospital_beds"
    GROUP BY hq_state
    ORDER BY total_staffed_beds DESC
"""
