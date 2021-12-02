import json
import requests
import pandas as pd

def all_regions():
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

    return regiones, allregions


def get_region_index(region_name):
    regiones, allregions =  all_regions()
    indice = int(regiones.index(region_name))
    return indice, allregions



def get_region_code(region_name):
    index_, all_regions = get_region_index(region_name)
    all_regions[index_]['c']
    return all_regions[index_]['c']


def get_regiondata(region_name):
    index_servel = get_region_code(region_name)
    cookies = {
        '_ga': 'GA1.2.1405564328.1637065285',
        '_gid': 'GA1.2.869325178.1637065285',
        '_gat': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.servelelecciones.cl/',
        'Accept-Language': 'es-419,es;q=0.9',
    }

    response = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/computo/regiones/'+str(index_servel)+'.json', headers=headers, cookies=cookies)

    data = json.loads(response.content)
    df_r = pd.DataFrame(columns= list(data['title'].keys()))
    df_r = df_r.append(data['data'], ignore_index=True)
    df_r.columns = list(data['title'].values())
    return df_r
    
    
    #return json.loads(response.content)

def get_comunas_by_region(region_name):
    index_servel = get_region_code(region_name)
    cookies = {
        '_ga': 'GA1.2.310706262.1638380181',
        '_gid': 'GA1.2.1782980774.1638380181',
        '_gat': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Opera";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.servelelecciones.cl/',
        'Accept-Language': 'es-419,es;q=0.9',
    }

    response = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/filters/comunas/byregion/'+str(index_servel)+'.json', headers=headers, cookies=cookies)
    print('--**--'*30)
    print(index_servel)
    print(response)
    print('--**--'*30)
    allcomunas = json.loads(response.content)
    comunas = list(n['d'] for n in allcomunas)
    return comunas


def get_allcomunas():
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

    response_allcomunas = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/filters/comunas/all.json', headers=headers, cookies=cookies)
    allcomunas = json.loads(response_allcomunas.content)
    comunas = list(n['d'] for n in allcomunas)
    return comunas, allcomunas	
#print(get_comunas_by_region('DE COQUIMBO'))



def get_comuna_index(comuna_name):
    comunas, allcomunas =  get_allcomunas()
    indice = int(comunas.index(comuna_name))
    return indice, allcomunas

def get_comuna_code(comuna_name):
    index_, all_comunas = get_comuna_index(comuna_name)
    all_comunas[index_]['c']
    return all_comunas[index_]['c']


def get_comunadata(comuna_name):
    
    index_servel = get_comuna_code(comuna_name)

    cookies = {
        '_ga': 'GA1.2.1405564328.1637065285',
        '_gid': 'GA1.2.869325178.1637065285',
        '_gat': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.servelelecciones.cl/',
        'Accept-Language': 'es-419,es;q=0.9',
    }

    response = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/computo/comunas/'+str(index_servel)+'.json', headers=headers, cookies=cookies)

    data = json.loads(response.content)
    df_c = pd.DataFrame(columns= list(data['title'].keys()))
    df_c = df_c.append(data['data'], ignore_index=True)
    df_c.columns = list(data['title'].values())
    return df_c

def get_allchile():

    global df_a
    cookies = {
        '_ga': 'GA1.2.1405564328.1637065285',
        '_gid': 'GA1.2.869325178.1637065285',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.servelelecciones.cl/',
        'Accept-Language': 'es-419,es;q=0.9',
    }

    response_total = requests.get('https://www.servelelecciones.cl/data/elecciones_presidente/computo/global/19001.json', headers=headers, cookies=cookies)
    data = json.loads(response_total.content)

    #df = pd.DataFrame(columns= list(data['title'].values()))
    df_a = pd.DataFrame(columns= list(data['title'].keys()))
    df_a = df_a.append(data['data'], ignore_index=True)
    df_a.columns = list(data['title'].values())
    return df_a

def votes_by_region():
    data= pd.DataFrame(columns=['Nombre de los Candidatos',
    'Partido','Votos','Porcentaje','Candidatos','Elcecto','None','Percent'])

    regions, allregions = all_regions()
    for n in regions:
        data_ = get_regiondata(n)
        data_['Region'] = n
        data = data.append(data_) 
    return data



def votes_by_comunas(region_name):

    comunas = get_comunas_by_region(region_name)
    
    data= pd.DataFrame(columns=['Nombre de los Candidatos',
    'Partido','Votos','Porcentaje','Candidatos','Elcecto','None','Percent'])

    #regions, allregions = all_regions()
    for n in comunas:
        data_ = get_comunadata(n)
        data_['Comuna'] = n
        data = data.append(data_) 
    return data
