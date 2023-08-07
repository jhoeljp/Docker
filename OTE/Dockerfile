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


# COPY init.sql /docker-entrypoint-initdb.d/

# Start the PostgreSQL service and execute the init.sql script
# RUN service postgresql start && \
#     su - postgres -c 'psql -c "CREATE DATABASE ote_db;"' && \
#     su - postgres -c 'psql ote_db < ote_records.sql;"'
    # service postgresql stop
    # python3 __main__.py

# Set the entrypoint to start PostgreSQL and then execute the Python script
# ENTRYPOINT service postgresql start && python3 __main__.py

# # Run the Python script
# CMD ["python3", "__main__.py"]

# Run script to populate database
# CMD ["python3", "__main__.py"]

RUN service postgresql start && \
    su postgres -c "psql -c 'CREATE DATABASE ote_db;' && psql ote_db < ote_records.sql"
    # python3 __main__.py

# Run script to populate database
CMD ["python3", "__main__.py"]