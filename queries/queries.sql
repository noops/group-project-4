-- Join tables to get complete dataset

select * from sf_crime as cr
inner join crime_dates as d on d."PdId"=cr."PdId"
inner join geographic as geo on geo."PdId"=cr."PdId"


