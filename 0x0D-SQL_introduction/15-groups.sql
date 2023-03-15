<<<<<<< HEAD
-- A script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
=======
-- A script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score 
ORDER BY COUNT(score) DESC;
>>>>>>> e9914911e30718f89860
