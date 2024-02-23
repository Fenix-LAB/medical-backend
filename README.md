# Full API REST on fastAPI

## Description

This is a simple API REST with fastAPI and SQLAlchemy ORM.

## API REST
API REST is an application programming interface that uses HTTP requests to GET, PUT, POST and DELETE data.
Graphic representation of the API REST:
![REST API](images/REST_Graph.png)

## SQLAlchemy ORM
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

## fastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Installation
Python 3.6+ is required to run this application.

### Clone the repository
```bash
git clone
```

### Install the dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
uvicorn app.server:app --reload
```

### Run the database
```bash
docker build -t database .
docker run -d -p 5432:5432 database
```


## Files structure
    
```bash 
API REST/
│
├── app/
│ ├── config/
│ │ ├── db_config.py
│ │ ├── session.py
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