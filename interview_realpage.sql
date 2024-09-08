
SELECT department, gender, AVG(salary) AS avg_salary
FROM employees
GROUP BY department, gender;


WITH RankedSalaries AS (
    SELECT name, salary, department,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank
    FROM employees
)
SELECT name, salary, department
FROM RankedSalaries
WHERE rank = 1;
