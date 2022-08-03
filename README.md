# estate shop

## Installation Steps:

```bash
git clone
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Database Migrations
To generate new migrations:
```bash
python manage.py migrate -n '<MIGRATION_MESSAGE>'
```

To apply migrations: 
```bash
python manage.py migrate
```

## Running Server

```bash
python manage.py runserver
```
