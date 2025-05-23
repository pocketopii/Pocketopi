WITH CTE AS (SELECT DISTINCT REQUESTER_ID AS ID
FROM REQUESTACCEPTED

UNION

SELECT DISTINCT ACCEPTER_ID AS ID
FROM REQUESTACCEPTED)

SELECT ID, COUNT(ID) AS NUM
FROM CTE C JOIN REQUESTACCEPTED R
ON ID = REQUESTER_ID OR ID = ACCEPTER_ID
GROUP BY ID
ORDER BY NUM DESC
LIMIT 1