SELECT DATE_FORMAT(TRANS_DATE, '%Y-%m') AS MONTH, COUNTRY, COUNT(1) AS TRANS_COUNT, 
    SUM(CASE WHEN STATE = 'approved' THEN 1
        ELSE 0 END) AS APPROVED_COUNT, SUM(AMOUNT) AS TRANS_TOTAL_AMOUNT,
    SUM(CASE WHEN STATE = 'approved' THEN AMOUNT
        ELSE 0 END) AS APPROVED_TOTAL_AMOUNT 
FROM TRANSACTIONS
GROUP BY 1,2