SELECT TRANSACTION_DATE, 
    SUM(CASE 
    WHEN AMOUNT % 2 = 1 THEN AMOUNT
    ELSE 0 END) AS ODD_SUM,
    SUM(CASE 
    WHEN AMOUNT % 2 = 0 THEN AMOUNT
    ELSE 0 END) AS EVEN_SUM
FROM TRANSACTIONS
GROUP BY TRANSACTION_DATE
ORDER BY TRANSACTION_DATE