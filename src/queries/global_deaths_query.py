global_deaths_query = """
    WITH MonthlyDeathsData AS (
    SELECT
        country_name,
        MAX(date) AS last_day_of_month,  -- Pegando o último dia registrado de cada mês
        DATE_FORMAT(date_parse(date, '%Y-%m-%d'), '%m/%Y') AS month,  -- Formatado como MM/YYYY
        MAX(deaths) AS deaths_on_last_day  -- Pegando as mortes no último dia do mês
    FROM
        "covid-19"."enigma_aggregation_global_countries"
    GROUP BY
        country_name,
        DATE_FORMAT(date_parse(date, '%Y-%m-%d'), '%m/%Y')  -- Agrupamento deve usar a mesma formatação
    )

    -- Utilizando uma subconsulta para determinar os 5 últimos meses registrados para cada país
    , LatestMonths AS (
        SELECT
            country_name,
            month
        FROM (
            SELECT
                country_name,
                month,
                ROW_NUMBER() OVER (PARTITION BY country_name ORDER BY date_parse(month, '%m/%Y') DESC) AS rn
            FROM
                MonthlyDeathsData
        ) sub
        WHERE sub.rn <= 5
    )

    -- Selecionando os dados do último dia de cada um dos últimos 5 meses para cada país
    SELECT
        a.country_name,
        a.month,
        a.deaths_on_last_day
    FROM
        MonthlyDeathsData a
    JOIN
        LatestMonths b ON a.country_name = b.country_name AND
                        a.month = b.month
    ORDER BY
        a.country_name, a.month ASC;
"""