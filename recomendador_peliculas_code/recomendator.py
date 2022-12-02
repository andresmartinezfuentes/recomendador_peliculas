import re
import pandas as pd
import os


def extract():
    df_m = pd.read_csv('movies.csv',sep=',')
    df_m = df_m.drop(df_m.loc[pd.isna(df_m['genres'])].index)
    df_m = df_m.drop_duplicates(subset=['title'])

    return df_m

def transform(df_m,tipo):
    def buscar(x,y):
        return re.findall(y, x)

    df_2 = df_m['genres'].apply(lambda x: buscar(x,tipo))
    indices = []
    orden = []
    for i in list(df_2.index):
        if df_2.loc[i] == []:
            indices.append(0)
        else:
            if len(df_2.loc[i]) == 2:
                indices.append(2)
            else:
                indices.append(1)
    df_m['coincidencias'] = indices

    df_m = df_m.sort_values(['coincidencias','vote_average'],ascending=False)
    peliculas=list(df_m['title'].iloc[:66])

    return peliculas

def load(peliculas):
    i = 0
    while i < len(peliculas):
        s = ''
        s += peliculas[i]
        s += ' '*(55-len(peliculas[i]))
        s += peliculas[i+1]
        s += ' '*(55-len(peliculas[i+1]))
        s += peliculas[i+2]
        print(s)
        i += 3

def menu():
    genero = ''
    print('Seleccione un genero:')
    print('\tHorror\t\tThriller\t\tFantasy\t\t\tAdventure\t\tFamily') 
    print('\tAction\t\tDrama\t\t\tScience Fiction\t\tComedy\t\t\tCrime') 
    print('\tRomance\t\tMystery\t\t\tWar\t\t\tAnimation\t\tTV Movie') 
    print('\tHistory\t\tDocumentary\t\tMusic\t\t\tWestern')
    tipo = input('Introduzca un genero tal y como se muestran en pantalla: ')
    while tipo != 'EXIT':
        os.system('cls')
        genero += '|' + tipo 
        gen_p = '\t\t\t' + genero
        print(gen_p)
        print('Seleccione otro genero o introduzca EXIT para continuar adelante:')
        print('\tHorror\t\tThriller\t\tFantasy\t\t\tAdventure\t\tFamily') 
        print('\tAction\t\tDrama\t\t\tScience Fiction\t\tComedy\t\t\tCrime') 
        print('\tRomance\t\tMystery\t\t\tWar\t\t\tAnimation\t\tTV Movie') 
        print('\tHistory\t\tDocumentary\t\tMusic\t\t\tWestern')
        tipo = input('Introduzca un genero tal y como se muestran en pantalla: ')
    return genero



if __name__ == '__main__':
    df_m = extract()
    tipo = menu()
    os.system('cls')
    print(f'\t\t\tGenerando recomendaciones para estos generos {tipo}')
    peliculas = transform(df_m,tipo)
    os.system('cls')
    load(peliculas)



