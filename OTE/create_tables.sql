
'''
Hodina                    float64
Cena (EUR/MWh)            float64
Množství\n(MWh)           float64
Export                    float64
Import                    float64
Saldo                     float64
Date               datetime64[ns]
'''

CREATE TABLE ote_records (
    id SERIAL PRIMARY KEY,
    Day_Hour INTEGER, 
    Price FLOAT,
    Amount FLOAT, 
    Export FLOAT, 
    Import FLOAT, 
    Balance FLOAT, 
    record_date DATE
);