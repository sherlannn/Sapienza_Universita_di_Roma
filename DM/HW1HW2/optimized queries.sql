1 - /* main query */ 

SELECT
    gender,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM person) AS percentage
FROM
    person
GROUP BY
    gender;
	
-- time : 158 msec---

1 - /*optimized version */

CREATE INDEX idx_gender ON person (gender);

SELECT
    gender,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM person) AS percentage
FROM
    person
GROUP BY
    gender;
	
/* the time is : 111ms */

2- /* main query */ 

SELECT country, COUNT(*) AS interview_count
FROM person
GROUP BY country
ORDER BY interview_count DESC LIMIT 3;
 /* time : 179 */
 
 
2- /* optimized  query */
CREATE INDEX idx_country ON person (country); 

SELECT country, COUNT(*) AS interview_count
FROM person
GROUP BY country
ORDER BY interview_count DESC LIMIT 3;

/* time : 102 */


3 - /* main query */  

SELECT country, AVG(CASE WHEN growing_stress = 'Yes' THEN 1 ELSE 0 END) AS avg_growing_stress
FROM person p
JOIN interview i ON p.person_id = i.interview_id
GROUP BY country
ORDER BY avg_growing_stress DESC
LIMIT 5;

-- time to execute : 180ms

3 - /* optimized query */ 

CREATE INDEX idx_growing_stress ON interview (growing_stress);

SELECT country, AVG(CASE WHEN growing_stress = 'Yes' THEN 1 ELSE 0 END) AS avg_growing_stress
FROM person p
JOIN interview i ON p.person_id = i.interview_id
GROUP BY country
ORDER BY avg_growing_stress DESC
LIMIT 5;

-- time to execute 152ms 

4-- query optimization


-- main query usually take 170ms to run 

SELECT p.country , count(*)
FROM person p
JOIN interview i ON p.person_id = i.interview_id
WHERE i.growing_stress = 'Yes'
AND p.country NOT IN (
    SELECT DISTINCT p2.country
    FROM person p2
    WHERE p2.family_history = 'Yes'
)
GROUP BY p.country
ORDER BY COUNT(*) DESC
LIMIT 10;


-- optimized query take 130ms to run - more than 20percent faster 
-- chages made : removing distict and adding not exists intead of not in 

SELECT p.country, COUNT(*) AS stress_count
FROM person p
JOIN interview i ON p.person_id = i.interview_id
WHERE i.growing_stress = 'Yes'
AND NOT EXISTS (
    SELECT 1
    FROM person p2
    WHERE p2.family_history = 'Yes'
    AND p2.country = p.country
)
GROUP BY p.country
ORDER BY stress_count DESC
LIMIT 10;

--------------
-- even more optimized 
-- This eliminates the need to recompute the result set every time the query is executed.
-- Create or replace the materialized view
-- Create the materialized view if it does not exist
CREATE MATERIALIZED VIEW IF NOT EXISTS my_materialized_view AS
SELECT p.country, COUNT(*) AS stress_count
FROM person p
JOIN interview i ON p.person_id = i.interview_id
WHERE i.growing_stress = 'Yes'
AND NOT EXISTS (
    SELECT 1
    FROM person p2
    WHERE p2.family_history = 'Yes'
    AND p2.country = p.country
)
GROUP BY p.country;


SELECT *
FROM my_materialized_view
ORDER BY stress_count DESC
LIMIT 10;


