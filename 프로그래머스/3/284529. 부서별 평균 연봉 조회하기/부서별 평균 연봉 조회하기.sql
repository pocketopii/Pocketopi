SELECT DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL),0) AS AVG_SAL
FROM HR_DEPARTMENT D NATURAL JOIN HR_EMPLOYEES E
GROUP BY DEPT_ID
ORDER BY 3 DESC