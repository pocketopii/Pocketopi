SELECT A.EMP_NO, A.EMP_NAME, B.GRADE, CASE GRADE
    WHEN 'S' THEN SAL * 0.2
    WHEN 'A' THEN SAL * 0.15
    WHEN 'B' THEN SAL * 0.1
    ELSE 0 END AS BONUS
FROM HR_EMPLOYEES A NATURAL JOIN(SELECT EMP_NO, CASE 
                                 WHEN SUM(SCORE)/2 >= 96 THEN 'S'
                                 WHEN SUM(SCORE)/2 >= 90 THEN 'A'
                                 WHEN SUM(SCORE)/2 >= 80 THEN 'B'
                                 ELSE 'C' END AS GRADE
                                 FROM HR_GRADE
                                 GROUP BY 1) B
ORDER BY 1