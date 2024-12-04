--1
/* in this query, we want to find out the portion of female and males participating in this survey.
so we select the 'gender' column from the 'person' table and calculate the count of each gender.
then we multiplies this count by 100.0 and divide it by the total count of rows in the 'person' table
to get the percentage of each gender. */

SELECT
    gender,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM person) AS percentage
FROM
    person
GROUP BY
    gender;
	
-----------------------------------------------------------------------------------------------------
--2
/* top 3 Hours of the day when most interviews which are conducted.
we select the 'hour' column from the 'time' table and count the number
of occurrences for each distinct hour. using GROUP BY we calculate the
count of interviews separately for each distinct hour. 
*/

SELECT
    hour,
    COUNT(*) AS num_interviews
FROM
    time
GROUP BY hour
ORDER BY
    num_interviews DESC
LIMIT 3;

-----------------------------------------------------------------------------
--3
/* top 3 countries with the most interviews which are conducted.
we select the 'country' column from the 'person' table and count
the number of occurrences for each distinct country using Group By. 
*/

SELECT country, COUNT(*) AS interview_count
FROM person
GROUP BY country
ORDER BY interview_count DESC LIMIT 3;

-----------------------------------------------------------------------------
--4
/* Find the percentage of persons who reported changes in habits and growing stress:
we count the total number of rows in the 'interview' table where both 'changes_habits'
and 'growing_stress' are 'Yes', then we multiply it by 100.0 and then divide it by the
total count of rows in the 'interview' table.
*/

SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM interview)) AS percentage
FROM interview
WHERE changes_habits = 'Yes' AND growing_stress = 'Yes';

-------------------------------------------------------------------------------
--5
/* percentage of females and males in each country facing social weakness
*/

SELECT 
    p.country, 
    p.gender, 
    (COUNT(*) * 100.0 / total_rows.total_row_count) AS social_weakness_percentage
FROM 
    person p
JOIN 
    interview i ON p.person_id = i.interview_id
JOIN 
    (SELECT country, COUNT(*) AS total_row_count
     FROM person
     GROUP BY country) AS total_rows ON p.country = total_rows.country
WHERE 
    i.social_weakness = 'Yes'
GROUP BY 
    p.country, p.gender, total_rows.total_row_count;

---------------------------------------------------------------------------
--6
/* calculate the average changes in habits reported in interviews conducted each year.
we use a conditional statement within the AVG function. If the value of 'changes_habits'
in the 'interview' table is 'Yes', we assign a value of 1, otherwise 0. The AVG function
then calculates the average of these values GROUP BY year which produces the avg in each year.
*/

SELECT year, AVG(CASE WHEN i.changes_habits = 'Yes' THEN 1 ELSE 0 END)*100 AS avg_changes_habits
FROM time 
JOIN interview i ON time.id = i.interview_id
GROUP BY year;

----------------------------------------------------------------------------
--7
/* top 5 countries with the highest average growing stress reported:
first we calculate the average of groving stress for each country, then order them from high to low
*/

SELECT country, AVG(CASE WHEN growing_stress = 'Yes' THEN 1 ELSE 0 END)*100 AS avg_growing_stress
FROM person p
JOIN interview i ON p.person_id = i.interview_id
GROUP BY country
ORDER BY avg_growing_stress DESC
LIMIT 5;

---------------------------------------------------------------------------
--8
/* average percentage of reported social weaknesses per gender:
*/

SELECT gender, AVG(CASE WHEN social_weakness = 'Yes' THEN 1 ELSE 0 END)*100 AS avg_social_weakness 
FROM person p
JOIN interview i ON p.person_id = i.interview_id
GROUP BY gender;


---------------------------------------------------------------------------
--9 
/* 	top 5 country with self employed occupations 
*/

SELECT country , AVG(CASE WHEN self_employed = 'Yes' THEN 1 ELSE 0 END)*100 AS avg_slef_emploed
FROM person 
JOIN interview on person.person_id = interview.interview_id
GROUP BY country
ORDER BY avg_slef_emploed desc

---------------------------------------------------------------------
--10 
/*  Query to Identify top 5 Countries with High Growing Stress but Low Family History of Mental Health 
*/

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
LIMIT 5;