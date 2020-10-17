-- Creation of incident_info table

CREATE TABLE incident_info (
	IncidentNum int,
	Category character varying(50),
	Description character varying(100),
	DayOfWeek character varying(10),
	"Date" date,
	"Time" time,
	PdDistrict character varying(50),
	Resolution character varying(50),
	Address character varying(100),
	Latitude numeric(15,12),
	Longitude numeric(15,12),
	Location character varying(50),
	PdId bigint
);	
