# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install PostgreSQL client and server
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib && \
    apt-get clean

# Install psycopg2
RUN pip install psycopg2-binary

# Add the PostgreSQL binaries directory to the $PATH
ENV PATH="$PATH:/usr/lib/postgresql/13/bin"

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the PostgreSQL port
EXPOSE 5432

# Start the PostgreSQL service and create the database
RUN service postgresql start && \
    su - postgres -c 'psql -c "CREATE DATABASE ote_db;"' && \
    service postgresql stop

#python buffer flush 
ENV PYTHONUNBUFFERED=1

# Run the python script
CMD python3 __main__.py