import json
import requests

def all_region():
    cookies = {
        '_ga': 'GA1.2.1405564328.1637065285',
        '_gid': 'GA1.2.869325178.1637065285',
        '_gat': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.servelelecciones.cl/',
        'Accept-Language': 'es-419,es;q=0.9',
    }

    response_allregions = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/filters/regiones/all.json', headers=headers, cookies=cookies)



    allregions = json.loads(response_allregions.content)
    regiones = list(n['d'] for n in allregions)
    print(allregions)

    return regiones, allregions








def get_region_index(region_name):
    regiones, allregions =  all_region()
    indice = int(regiones.index(regiones[0]))
    return indice, allregions



def get_region_code(region_name):
    index_, all_regions = get_region_index(region_name)
    all_regions[index_]['c']
    return all_regions[index_]['c']







#print('---'*20)
#print(indice)
#print('---'*20)
#print(by_region()[0])
#print('---'*20)


print(get_region_code('asfgdhf'))



