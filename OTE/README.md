# OTE Initiative

[OTE](https://www.ote-cr.cz/en/welcome?set_language=en) is one of the largest Energy companies in Check Republic. They make their predictions of electricity prices readily available to the public on a day to day basis.

This project's aim is to perform data analysis and ML to contextualize their public data on energy resources.

Current version can fetch records as early as June 18, 2021. 

## Overview 

There is 4 components to this project: 

1. Data Extraction (OTE website) 
2. Data Transformation (pandas) 
3. Data Manipulation (Docker and Postgre db)
4. Data Vizualization (Google Looker)

## Work In Progress

* Testing it on live servers.
* Connecting db to Google Looker dashboard

## Requirements

* Docker Engine 24.0

## Getting Started

Download this repository on desktop and do the following: 

### Configuration

Change all relevant ports and DB naming info on docker-compose.yaml 

Change download dates on "__main__.py"

### Build

Open the terminal 
Switch to directory containing docker-compose.yaml 

Run the following command: 
```
docker-compose up --build
```

## Additional Resources

- [Google Looker Dashboard](https://lookerstudio.google.com)
