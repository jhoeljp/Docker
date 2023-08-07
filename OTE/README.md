# OTE Initiative

[OTE](https://www.ote-cr.cz/en/welcome?set_language=en) is one of the largest Energy companies in Check Republic. They make their predictions of electricity prices readily available to the public on a day to day basis.

This project's aim is to perform data analysis and ML to contextualize their public data on energy resources.

## Overview 

There is 4 components to this project: 

1. Data Extraction (OTE website) 
2. Data Transformation (pandas) 
3. Data Manipulation (Docker and POSTgres DB)
4. Data Vizualization (Google Looker)

## WIP (Work In Progress)

Currently working on testing it on live serves, and scheduling a cron job for daily excel download.

## Requirements

* Docker Engine 24.0.2
* Python 3.10
    - pandas==1.4.2
    - psycopg2_binary==2.9.6
    - Requests==2.31.0
    - xlrd >= 1.0.0

No need to install python modules! 

## Getting Started

Download this repository on desktop and do the following: 

### Configuration

Change all relevant ports and DB naming info on docker-compose.yaml 

Change download dates on "__main__.py"

### Build

```
docker-compose up --build
```

### Status 
```
docker ps 
```

## Additional Resources

- [Google Looker Dashboard](https://lookerstudio.google.com)