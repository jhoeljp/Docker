# OTE Initiative

[OTE](https://www.ote-cr.cz/en/welcome?set_language=en) is one of the largest Energy companies in Check Republic. They make their predictions of electricity prices readily available to the public on a day to day basis.

This project's aim is to perform data analysis and ML to contextualize their public data on energy resources.

## Overview 

There is 4 components to this project: 

1. Data Extraction (OTE website) 
2. Data Transformation (pandas) 
3. Data Manipulation (Docker and POSTgres DB)
4. Data Vizualization (Google Looker)

## Requirements

OTE requires:
python 3.10 or higher 
Docker Engine 24.0.2 or higher

## Getting Started

on path of environment clone this repository and do the following: 

### build docker image
```
$ docker build -t ote_image .
```

### build container from docker image 
```
$ docker run -d --name ote_container -p 5432:5432 -e POSTGRES_PASSWORD=password ote_image
```

### make sure container is running 
```
docker ps 
```


## Additional Resources

- [Timescale Database](https://docs.timescale.com/self-hosted/latest/install/installation-docker/)
- [Google Looker Dashboard](https://lookerstudio.google.com)