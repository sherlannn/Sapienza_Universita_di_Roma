CREATE TABLE IF NOT EXISTS person (
    person_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL,
    country VARCHAR(30) NOT NULL,
    self_employed VARCHAR(3) NOT NULL,
    family_history VARCHAR(3) NOT NULL
);

CREATE TABLE IF NOT EXISTS time (
    id SERIAL PRIMARY KEY,
    year SMALLINT NOT NULL,   -- makeing smallint can lead to storage and index efficiency improvement
    month SMALLINT NOT NULL,
    hour SMALLINT NOT NULL
);

CREATE TABLE IF NOT EXISTS interview (
    interview_id SERIAL PRIMARY KEY,
    occupation VARCHAR(20) NOT NULL,
    days_indoors VARCHAR(30) NOT NULL,
    growing_stress VARCHAR(10) NOT NULL,
    changes_habits VARCHAR(10) NOT NULL,
    mental_health_history VARCHAR(10) NOT NULL,
    mood_swings VARCHAR(10) NOT NULL,
    coping_struggles VARCHAR(10) NOT NULL,
    work_interest VARCHAR(10) NOT NULL,
    social_weakness VARCHAR(10) NOT NULL,
    mental_health_interview VARCHAR(10) NOT NULL,
    care_options VARCHAR(10) NOT NULL
);




-----------------------





COPY person FROM 'D:\Sapienza\s2\DM\projects\hw1 hw2\person_table.csv' DELIMITER ',';
COPY time FROM 'D:\Sapienza\s2\DM\projects\hw1 hw2\time_table.csv' DELIMITER ',';
COPY interview FROM 'D:\Sapienza\s2\DM\projects\hw1 hw2\interview_table.csv' DELIMITER ',';

/*
n a foreign key reference,
a link is created between two tables when the column or 
columns that hold the primary key value for one table are 
referenced by the column or columns in another table. This
column becomes a foreign key in the second table.

*/ 
-- now i want to make a relation between person and time tables based on the primary keys they have
ALTER TABLE time
ADD CONSTRAINT fk_time
    FOREIGN KEY (id)
    REFERENCES person(person_id);
	

-- now i want to make a relation between person and interview tables 
ALTER TABLE interview
ADD CONSTRAINT fk_time
    FOREIGN KEY (interview_id)
    REFERENCES person(person_id);



-- relationship between interview and time 

ALTER TABLE interview
ADD CONSTRAINT fk_time1
	FOREIGN KEY (interview_id)
	REFERENCES time(id)