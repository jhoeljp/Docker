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

```
$ python3 -m pip install -r requirements.txt
```

To set up local timescale docker database

```
$ docker run timescale/timescaledb
```

## Additional Resources

- [Timescale Database](https://docs.timescale.com/self-hosted/latest/install/installation-docker/)
- [Google Looker Dashboard](https://lookerstudio.google.com)