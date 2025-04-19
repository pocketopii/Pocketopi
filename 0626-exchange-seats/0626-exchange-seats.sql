SELECT ROW_NUMBER() OVER (ORDER BY S_ID) AS ID, STUDENT
FROM (SELECT IF(ID % 2 = 0, ID - 1, ID + 1) AS S_ID, STUDENT
      FROM SEAT) AS A