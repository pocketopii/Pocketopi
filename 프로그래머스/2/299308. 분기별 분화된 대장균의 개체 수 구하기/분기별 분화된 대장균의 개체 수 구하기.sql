SELECT CASE 
    WHEN MONTH(DIFFERENTIATION_DATE) >= 1 AND MONTH(DIFFERENTIATION_DATE) <= 3 THEN '1Q'
    WHEN MONTH(DIFFERENTIATION_DATE) >= 4 AND MONTH(DIFFERENTIATION_DATE) <= 6 THEN '2Q'
    WHEN MONTH(DIFFERENTIATION_DATE) >= 7 AND MONTH(DIFFERENTIATION_DATE) <= 9 THEN '3Q'
    ELSE '4Q' 
    END AS QUARTER, 
    COUNT(1) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY 1
ORDER BY 1