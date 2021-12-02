# servel.py

Librarie servel.py provides a variety of functions to connect to servel.cl and get the data from last presidentail elections.
The original data comes in json sintaxis but the functions from this library return pandas dataframes so its easy work with, e.g plot the data

* ***servel.all_regions()*** gets the data from all regions by region
* ***servel.get_region_code(region_name)*** gets the code that servel uses to identify that region in particular
* ***servel.get_regiondata(region_name)*** gets the data from that region in particular
* ***servel.get_comunas_by_region(region_name)*** gets a list of all the "comunas" inside that region in particular
* ***servel.get_allcomunas()*** show a list of all "comunas" of the country
* ***servel.get_comuna_code(comuna_name)*** gets the code that servel uses to identify that "comuna" in particular
* ***servel.get_comunadata(comuna_name)*** gets the data from that comuna in particular
* ***servel.get_allchile()*** gets the global results
* ***servel.votes_by_region()*** gets the vote by region
* ***servel.votes_by_comunas(region_name)*** gets the votes by "comuna" inside that region in particular

![image](https://user-images.githubusercontent.com/81306499/144479407-dd586df2-16a4-40cb-8ad1-588b9f3c3bdf.png)

![image](https://user-images.githubusercontent.com/81306499/144479946-71899d22-d1e8-4742-bcf5-fbf8c702f17b.png)


# elections_data.py

this file contains the code that runs a tkinter app that allow the user to choose the region and "comuna" to get the data from, after that it plots the data as its shown below in the examples. The code its fairly simple and it runs after you choose the Region and the "comuna" and press "run".

> examples: 

![image](https://user-images.githubusercontent.com/81306499/144476047-de390448-b1da-4b08-a7f4-8a27fe45bf17.png)

![image](https://user-images.githubusercontent.com/81306499/144476188-9baced06-02ed-469d-a971-1e1b9fc3febb.png)

![image](https://user-images.githubusercontent.com/81306499/144476338-c7aaf7e8-5111-449d-9ffb-5974e955694b.png)

![image](https://user-images.githubusercontent.com/81306499/144476455-68719ec5-d0a5-41d9-929f-e7f82f852790.png)

![image](https://user-images.githubusercontent.com/81306499/144476511-2e166be0-f242-4166-887f-12357ce34937.png)
