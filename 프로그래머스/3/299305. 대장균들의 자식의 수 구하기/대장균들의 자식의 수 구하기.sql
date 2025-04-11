SELECT A.ID, COUNT(B.PARENT_ID) AS CHILD_COUNT
FROM ECOLI_DATA A LEFT JOIN ECOLI_DATA B
ON A.ID = B.PARENT_ID
GROUP BY 1
ORDER BY 1