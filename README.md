# API REST for medical application

## Description
This is an API REST for a medical application. It is developed in Python using the FastAPI framework and the database is PostgreSQL.

## Installation
Python 3.10+ is required to run this application.

### Virtual environment
Create a virtual environment with the following command:
```bash
python -m venv venv
```

### Para MAC:
```bash
source venv/bin/activate
```

### Install the dependencies
```bash
pip install -r requirements.txt
```

## Configuration

### Database Configuration

Create the file `database.py` in the directory `app/config/` with the following connection variables for PostgreSQL database:


# app/config/database.py

DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_USER = "your_username"
DATABASE_PASSWORD = "your_password"
DATABASE_NAME = "your_database_name"

### Run the application
```bash
python app/main.py
```

### Look at the documentation
Go to the following URL: http://localhost:80/docs

### Format the code
Run the following commands to format the code, please make sure you are in the app directory of the project:
```bash
black --config ../pyproject.toml .
isort . --resolve-all-configs --config-root ..
flake8 --config ../.flake8 .
```

## Files structure
    
```bash 
API REST/
│
├── app/
│ ├── config/
│ │ ├── db_config.py
│ │ ├── session.py
│ │ ├── database.py
│ │ └── ...
│ │
│ ├── models/
│ │ ├── models.py
│ │ ├── responses_models.py
│ │ └── ...
│ │
│ ├── routes/
│ │ ├── router
│ │ │ ├── router1.py
│ │ │ ├── router2.py
│ │ │ └── ...
│ │ ├── api.py
│ │ └── ...
│ │
│ ├── schemas/
│ │ ├── schemas.py
│ │ ├── responses_schemas.py
│ │ └── ...
│ │
│ ├── utils/
│ │ ├── security.py
│ │ ├── validators.py
│ │ └── ...
│ │
│ ├── services/
│ │ ├── service1.py
│ │ ├── service2.py
│ │ └── ...
│ │
│ └── server.py
│
├── database/
│ ├── Dockerfile
│ ├── init_db.sh
│ └── ...
│
├── README.md
└── ...
```

- **app**: Contains all the application logic.
    - **config**: Contains the configuration of the database.
    - **models**: Contains the table models of the database.
    - **routes**: Contains the routes of the endpoints.
    - **schemas**: Contains the schemas of the data.
    - **utils**: Contains the utilities of the application.
    - **services**: Contains the services of the endpoints.
    - **server.py**: Main file.

- **database**: Contains the database configuration.
    - **Dockerfile**: Contains the configuration of the container.
    - **init_db.sh**: Contains the initialization of the database.