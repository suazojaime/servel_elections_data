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

# elections_data.py

this file contains the code that runs a tkinter app that allow the user to choose the region an "comuna" to get the data from, after that it plots the data as its shown below in the examples. The code its fairly simple and it runs after you choose the Region and the "comuna" and press "run".

The code its been really simple in order to allow anyone to build over it 

![image](https://user-images.githubusercontent.com/81306499/144476047-de390448-b1da-4b08-a7f4-8a27fe45bf17.png)

![image](https://user-images.githubusercontent.com/81306499/144476188-9baced06-02ed-469d-a971-1e1b9fc3febb.png)

![image](https://user-images.githubusercontent.com/81306499/144476338-c7aaf7e8-5111-449d-9ffb-5974e955694b.png)

![image](https://user-images.githubusercontent.com/81306499/144476455-68719ec5-d0a5-41d9-929f-e7f82f852790.png)

![image](https://user-images.githubusercontent.com/81306499/144476511-2e166be0-f242-4166-887f-12357ce34937.png)
