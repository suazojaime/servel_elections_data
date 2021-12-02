
import pandas as pd
import servel
from tkinter import *
import matplotlib.pyplot as plt



def get_data():
    region = variable_regiones.get()
    comuna = variable_comunas.get()
    datos_regiones = servel.get_regiondata(region)
    datos_comunas = servel.get_comunadata(comuna)
    
    return datos_regiones, datos_comunas

def update_comunas(a,b,c):
    global variable_comunas
    root_comunas = Tk()

    region = variable_regiones.get()
    comunas = servel.get_comunas_by_region(region)
    print(comunas)

    variable_comunas = StringVar(root_comunas)
    variable_comunas.set(comunas[0])

    dropdown_comuna = OptionMenu(root_comunas, variable_comunas, *comunas)
    dropdown_comuna.grid(row=0,column=1, pady=5, padx=100)

    return comunas
    

def plot_data(datos_comunas, datos_regiones, datos_chile, by_all_regions, by_all_comunas):
 
    fig, ax = plt.subplots(1,3, sharey='all')  

    ax[0].barh(datos_chile['Nombre de los Candidatos'], datos_chile['Percent'])
    ax[0].set_title('Todo Chile')

    ax[1].barh(datos_regiones['Nombre de los Candidatos'], datos_regiones['Percent'])
    ax[1].set_title(variable_regiones.get())

    ax[2].barh(datos_comunas['Nombre de los Candidatos'], datos_comunas['Percent'])
    ax[2].set_title(variable_comunas.get())

    plt.draw()
    plt.pause(0.001)

    plt.figure()

    fig, ax = plt.subplots(1,1)

    table = by_all_regions.pivot_table(index='Region', columns= 'Nombre de los Candidatos'
    , values = 'Votos', margins=True).sort_values(by = 'All', ascending=False).drop('All', axis=1).drop('All').reset_index()

    table.plot(x='Region', kind = 'bar', stacked=False, ax = ax)

    ax2 = ax.twinx()

    #table.plot(x='Region', kind = 'line', stacked=True, ax = ax2)

    total_x = by_all_regions.groupby(by='Region')['Votos'].sum().sort_values(ascending=False).index
    total_y = by_all_regions.groupby(by='Region')['Votos'].sum().sort_values(ascending=False).values
    
    ax2.plot(total_x,total_y, color='red', label='Total votos por region', linestyle='dashed', marker='o',  markersize=12 )
    ax2.legend(bbox_to_anchor=(0.6,0.5))

    ax.set_title(f'Por Región')

    plt.draw()
    plt.pause(0.001)

    plt.figure()


    table = by_all_comunas.pivot_table(index='Comuna', columns= 'Nombre de los Candidatos'
    , values = 'Votos', margins=True).sort_values(by = 'All', ascending=False).drop('All', axis=1).drop('All').reset_index()

    table.plot(x='Comuna', kind = 'bar', stacked=True)
    plt.title(f'Por comuna de : {variable_regiones.get()}')
    plt.draw()
    plt.pause(0.001)

    plt.figure()
    





def get_and_clean_data():

    datos_regiones, datos_comunas = get_data()

    datos_chile = servel.get_allchile()

    datos_regiones['Votos'] = datos_regiones['Votos'].str.replace('.','')
    datos_regiones['Votos'] = datos_regiones['Votos'].astype('int64') 
    datos_regiones['Percent'] = datos_regiones['Votos']/datos_regiones['Votos'].sum()*100

    datos_comunas['Votos'] = datos_comunas['Votos'].str.replace('.','')
    datos_comunas['Votos'] = datos_comunas['Votos'].astype('int64') 
    datos_comunas['Percent'] = datos_comunas['Votos']/datos_comunas['Votos'].sum()*100

    
    datos_chile['Votos'] = datos_chile['Votos'].str.replace('.','')
    datos_chile['Votos'] = datos_chile['Votos'].astype('int64')
    datos_chile = datos_chile.sort_values(by='Votos')
    datos_chile['Percent'] = datos_chile['Votos']/datos_chile['Votos'].sum()*100


    by_all_regions = servel.votes_by_region()
    by_all_regions['Votos'] = by_all_regions['Votos'].str.replace('.','')
    by_all_regions['Votos'] = by_all_regions['Votos'].astype('int64')
    #by_all_regions.groupby(by=['Region','Nombre de los Candidatos'])['Votos'].sum()
    by_all_regions = by_all_regions.groupby(by=['Region','Nombre de los Candidatos'])['Votos'].sum().reset_index()
    

    by_all_comunas = servel.votes_by_comunas(variable_regiones.get())
    by_all_comunas['Votos'] = by_all_comunas['Votos'].str.replace('.','')
    by_all_comunas['Votos'] = by_all_comunas['Votos'].astype('int64')
    by_all_comunas = by_all_comunas.groupby(by=['Comuna','Nombre de los Candidatos'])['Votos'].sum().reset_index()
    





    print('----'*20)
    print(datos_regiones)
    print('----'*20)
    print(datos_comunas)
    print('----'*20)
    print(datos_chile)
    print('----'*20)
    print(datos_regiones.dtypes)

    
    
    return datos_comunas, datos_regiones, datos_chile, by_all_regions, by_all_comunas


def run():
    datos_comunas, datos_regiones, datos_chile, by_all_regions, by_all_comunas = get_and_clean_data()
    plot_data(datos_comunas, datos_regiones, datos_chile, by_all_regions, by_all_comunas)
    print(servel.votes_by_region())
    by_all_regions = servel.votes_by_region()





regiones, alldata = servel.all_regions()

root = Tk()

variable_regiones = StringVar(root)
variable_regiones.set('Select Region')
dropdown_region = OptionMenu(root, variable_regiones, *regiones)
dropdown_region.grid(row=0,column=0, pady=5, padx=5)
variable_regiones.trace("w", update_comunas)


button_accept = Button(root,text='Buscar', command=get_data)
button_accept.grid(row=0,column=2, padx=5)

button_run = Button(root,text='Run', command=run)
button_run.grid(row=0,column=3, padx=5)


root.mainloop()

