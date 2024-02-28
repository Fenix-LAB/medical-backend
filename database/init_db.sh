#!/bin/bash

# Function to check if the database exists
database_exists() {
    psql -U postgres -lqt | cut -d \| -f 1 | grep -wq "$1"
}

# Check if the database exists
if database_exists "medical_db"; then
    echo "Database 'medical_db' already exists."
else
    echo "Creating database 'medical_db'..."
    # Create the database
    psql -U postgres -c "CREATE DATABASE medical_db;"
    echo "Database 'medical_db' created."
fi