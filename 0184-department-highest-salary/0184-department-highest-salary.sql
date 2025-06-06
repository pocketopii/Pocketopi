SELECT D.NAME AS DEPARTMENT, E.NAME AS EMPLOYEE, SALARY
FROM EMPLOYEE E JOIN DEPARTMENT D
ON E.DEPARTMENTID = D.ID
WHERE (SALARY, DEPARTMENTID) IN (SELECT MAX(SALARY), DEPARTMENTID
                                 FROM EMPLOYEE
                                 GROUP BY DEPARTMENTID)