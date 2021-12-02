# servel_data_scraping

Librarie servel.py provides a variety of functions to connect to servel.cl and get the data from last presidentail elections.

* servel.all_regions() gets the data from all regions by region
* servel.get_region_code(region_name) gets the code that servel uses to identify that region in particular
* servel.get_regiondata(region_name) gets the data from that region in particular
* servel.get_comunas_by_region(region_name) gets a list of all the "comunas" inside that region in particular
* servel.get_allcomunas() show a list of all "comunas" of the country
* servel.get_comuna_code(comuna_name) gets the code that servel uses to identify that "comuna" in particular
* servel.get_comunadata(comuna_name) gets the data from that comuna in particular
* servel.get_allchile() gets the global results
* servel.votes_by_region() gets the vote by region
* servel.votes_by_comunas(region_name) gets the votes by "comuna" inside that region in particular
