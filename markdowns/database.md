# Database - San Francisco Crime Predictor 

##### OVERVIEW
A PostgreSql database has been created in AWS named _group4_.
It contains three tables with raw data: **crime_dates**, **geographic** and **sf_crime connected** by **PdId** field.

![ERD](../images/ERD.PNG?raw=true)
The schemas are as follow (file _queries/schemas.sql_).
```sql
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
        "Location" character varying(50),
        "ZipCode" int
    );

    -- Creation of crime_dates table
    CREATE TABLE crime_dates (
        "PdId" bigint,
        "DayOfWeek" character varying(10),
        "Date" date,
        "Time" time
    );
```
A complete view of all the data can be achieved with the following query (file _queries/queries.sql_):
```sql
    select * from sf_crime as cr
    inner join crime_dates as d on d."PdId"=cr."PdId"
    inner join geographic as geo on geo."PdId"=cr."PdId"
```

##### DATA LOAD
* The data has already been loaded and can be accessed by simply connecting to the AWS database from your local.
* To split the raw data into the desired tables the script _Notebooks/load_data.ipynb_ has been executed, additionally the zip code has been included as part of the geographic table and later a manual import has been performed.
  **NOTE**: Automatic load has been discarded as an exhaustive test proved that a load using sqlalchemy module would take around 3h30' per table, no matter how the data was bucketed while a manual load was less than 3 seconds per table.
  
##### CONFIGURATION
To access the database from a Notebook (ex. _Notebooks/new_cleaning_data.ipynb_) four variables should be configured. 

* Create a config.py file and place it in the root folder of the project. Add the following variables:
```python
    endpoint=<Database Endpoint>
    db_user=<Database username>
    db_password=<Database password>
    db_name="group4"
```
