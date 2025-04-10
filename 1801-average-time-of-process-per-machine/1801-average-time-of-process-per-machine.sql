SELECT A.MACHINE_ID, ROUND(AVG(A.TIMESTAMP - B.TIMESTAMP),3) AS PROCESSING_TIME
FROM ACTIVITY A INNER JOIN ACTIVITY B
ON A.MACHINE_ID = B.MACHINE_ID AND A.PROCESS_ID = B.PROCESS_ID
WHERE A.ACTIVITY_TYPE = 'END' AND B.ACTIVITY_TYPE = 'START'
GROUP BY MACHINE_ID