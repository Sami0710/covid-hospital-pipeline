# COVID Hospital Pipeline

ETL pipeline on French hospital COVID data (data.gouv.fr).

## What it does
- **Extract**: Downloads 338,000+ rows of daily hospital data by department
- **Transform**: Cleans and filters data (hospitalisations, réanimations, décès, retours domicile)
- **Load**: Stores 113,118 rows into a PostgreSQL database

## Stack
- Python 3.15
- Pandas
- SQLAlchemy + psycopg2
- PostgreSQL 18

## Data source
[Données hospitalières COVID-19 — data.gouv.fr](https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7)

## How to run
```bash
python extract.py   # Download and save raw data
python transform.py # Clean and filter
python load.py      # Load into PostgreSQL
```

## Author
Sami Chiet