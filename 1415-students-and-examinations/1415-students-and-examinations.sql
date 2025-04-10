SELECT C. STUDENT_ID, C.STUDENT_NAME, C.SUBJECT_NAME, COUNT(D.SUBJECT_NAME) AS ATTENDED_EXAMS
FROM (SELECT * FROM STUDENTS A JOIN SUBJECTS B) C LEFT JOIN EXAMINATIONS D
ON C.STUDENT_ID = D.STUDENT_ID AND C.SUBJECT_NAME = D.SUBJECT_NAME
GROUP BY 1,2,3
ORDER BY 1,3