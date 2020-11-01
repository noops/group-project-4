-- Creation of sf_crime table

CREATE TABLE sf_crime (
	"PdId" bigint,
	"IncidntNum" int,
	"Category" character varying(50),
	"Descript" character varying(100),
	"Resolution" character varying(50)	
);

-- Creation of geographic table

CREATE TABLE geographic (
	"PdId" bigint,
	"PdDistrict" character varying(50),
	"Address" character varying(100),
	"X" numeric(15,12),
	"Y" numeric(15,12),
	"Location" character varying(50)
);

-- Creation of crime_dates table

CREATE TABLE crime_dates (
	"PdId" bigint,
	"DayOfWeek" character varying(10),
	"Date" date,
	"Time" time
);
