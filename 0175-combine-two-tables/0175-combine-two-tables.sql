SELECT FIRSTNAME, LASTNAME, CITY, STATE
FROM PERSON P LEFT JOIN ADDRESS A
ON A.PERSONID = P.PERSONID