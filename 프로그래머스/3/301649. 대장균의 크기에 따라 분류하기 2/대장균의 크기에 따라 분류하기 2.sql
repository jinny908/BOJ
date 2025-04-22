WITH 
row_count AS (
    SELECT COUNT(*) AS cnt FROM ecoli_data
),
ranked AS (
    SELECT 
        id,
        ROW_NUMBER() OVER (ORDER BY size_of_colony DESC) AS rn
    FROM ecoli_data
)
SELECT 
    r.id,
    CASE 
        WHEN r.rn <= c.cnt * 0.25 THEN 'CRITICAL'
        WHEN r.rn <= c.cnt * 0.50 THEN 'HIGH'
        WHEN r.rn <= c.cnt * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS colony_name
FROM ranked r
JOIN row_count c
ORDER BY r.id;