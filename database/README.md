# Database PostgreSQL
We build a PostgreSQL database with Docker. The database is used to store the data of the application.

### Image:

https://hub.docker.com/_/postgres

### Docker build and run

Build the image of PostgreSQL

```bash
docker build -f database/Dockerfile -t my_image_medical .
```

Run a container with the image of PostgreSQL

```bash
docker run -d \
--name medical_db \
-p 5432:5432 \
-e POSTGRES_PASSWORD=medical \
-v ${PWD}:/home/postgres/pgdata/data \
my_image_medical
```

One line

```bash
docker run -d --name medical_db -p 5432:5432 -e POSTGRES_PASSWORD=medical -v ${PWD}:/home/postgres/pgdata/data my_image_medical
```

### Docker run database

Run a container with the image of PostgreSQL


```bash
docker run -d \
--name my_base_timescaledb \
-p 5432:5432 \
-e POSTGRES_PASSWORD=password \
-v ${PWD}:/home/postgres/pgdata/data \
postgres:latest
```

### Docker exec

```bash
docker exec -it <id_container> bash
```

```bash
docker exec -it <id_container> psql -u postgres
```

### SQL Shell

Init the SQL Shell

```bash
psql -U postgres
```

Create database:

```bash
create database <name>;
```

Show databases:

```bash
\l
```

Change database:

```bash
\c <name>
```

Show tables:

```bash
\dt
```

Get information of a table:

```bash
\d+ "<name>";
```

Show data of a table:

```bash
SELECT * <"FROM table_name">;
```

Delete a table:

```bash
DROP TABLE <"table_name">;
```