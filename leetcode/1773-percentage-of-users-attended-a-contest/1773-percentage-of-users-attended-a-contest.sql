SELECT CONTEST_ID, ROUND(COUNT(USER_ID)/(SELECT COUNT(1) FROM USERS) * 100,2) AS PERCENTAGE
FROM REGISTER
GROUP BY 1
ORDER BY 2 DESC, 1