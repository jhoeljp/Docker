# OTE Initiative

[OTE](https://www.ote-cr.cz/en/welcome?set_language=en) is one of the largest Energy companies in Czech Republic. They make their predictions of electricity prices readily available to the public on a day to day basis.

This project's aim is to perform data analysis and ML to contextualize their public data on energy resources.

Current version can fetch records as early as June 18, 2021. 

Check out the most up to date dashboard [vizualization](https://lookerstudio.google.com/s/vMicIZTywxA)

## Overview 

There is 4 components to this project: 

1. Data Extraction (OTE website) 
2. Data Transformation (pandas) 
3. Data Manipulation (Docker and Postgre db)
4. Data Vizualization (Google Looker)

## Requirements

* Docker Engine
* docker-compose 

### Remote connection 
* ufw (Linux Uncomplicated firewall)
* on windows OS you need to create the Firewall outbound rule for port 5342 

## Getting Started

Download this repository on desktop and do the following: 

## Configuration

Change all relevant ports and DB naming info on docker-compose.yaml 

Change download dates on "__main__.py"


### Build

Having met all requirements, Open the terminal

To make the database container network readily available run:
```
docker network create mynetwork
```

Switch to the directory containing the docker-compose.yaml file

Run the following command: 
```
docker-compose up --build
```

After the containers have been initialized with no errors
configure the firewall using ufw (linux), for windows OS use <>

```
sudo ufw allow 5432
sudo ufw enable
```
This command opens port 5432 for incoming connections.
Allowing us to connect to our database container remotely

## Future Updates

* Run ML models to predict occurence of lowest energy price
* Accomodate for bigger data sample  
