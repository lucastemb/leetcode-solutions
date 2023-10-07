# Write your MySQL query statement below
SELECT * FROM cinema WHERE description NOT like 'boring' and mod(id, 2) = 1 ORDER BY rating DESC;