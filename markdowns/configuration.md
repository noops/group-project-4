# Configuration - San Francisco Crime Predictor

## Database:
##### CREATION
To configure the database a few steps are needed:
* Create a postgresql database. Name will be configurable so choose whichever you want.
* Execute the script queries/squemas.sql to create the incident_info table. It will contain the raw data.

##### LOAD DATA
* Create a config.py file and place it in the root folder of the project. Add the following variables:
```python
    dbPassword=<your_database_password>
    dbName=<name_of_the_created_database>
```
* To automatically load the data in the created table, execute the code in Notebooks/loadRawData.ipynb.

**WARNING**: Several executions will duplicate data as the script appends rows to the database. 