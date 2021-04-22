# Algoritmo Genetico para minimizar la funcion de Beale
import random as rd

print("Algoritmo Genetico\n")

tam_gen = 2 # Tamanio del material genetico por individuo
tam_poblacion = 25 # Tamanio de la poblacion
n_selecionados = 10 # Cantidad de selecionados par reproduccion/cruza
prob_mutacion = 0.4 # Probabilidad de mutacion por individuo

def aptitud(var): # recibe vector de variables [x1,x2]
    '''
     evalua la funcion beale
     fun a minimizar, precision .00000
    '''
    f = pow(1.5-var[0]*(1-var[1]),2) + pow(2.25-var[0]*(1-pow(var[1],2)),2) +\
        pow(2.625-var[0]*(1-pow(var[1],3)),2)
    return f

def individuo():
    '''
    Crea un individuo
     0<= x1 <=20
     0<= x2 <=30
    '''
    ind = []
    min = 0 # limite inferior x1,x2
    max = 20 # limte superir x1
    for x in range(tam_gen):
        ind.append(rd.uniform(min,max))
        max = 30 # truco para limite de x2
    return ind

def crear_poblacion():
    """
    Crea una poblacion nueva de individuos
    """
    po = []
    for y in range(tam_poblacion): # for en tamanio poblacion
        po.append(individuo()) # grega un nuevo individuo
    return po


def seleccion_cruza(po):
    '''
    Se aplica Seleccion de Estado Uniforme y Cruza Simple
    :param po: recive la poblacion
    :return: poblacion ordenada por su aptitud
    '''

    aptitudes = []
    ordenados = []
    for z in po: # se recorre en cada individuo
        # se calcula su aptitud y se guarda como : [aptitud,[x1,x2]] => [2092.030,[2,5]]
        aptitudes.append([aptitud(z),z])
    #print(aptitudes)

    for w in sorted(aptitudes,reverse= 1): # los ordena de mayor a menor
        ordenados.append(w[1])
    po = ordenados

    # selecciona los n individuos del fin(minimizar) de ordenados
    selecion = ordenados[(len(ordenados)-n_selecionados):]

    #print("poblacion ordenada\n",po)
    #print("Select\n",selecion)

    # cruza entre selecionados, remplaza al resto de po
    for j in range(len(po)-n_selecionados):
        # se aplica una cruza simple
        padres = rd.sample(selecion, 2)

        po[j][0] = padres[0][0]
        po[j][1] = padres[1][1]
    # retorn la nueva poblacion
    return po

def mutacion(pobl):
    """
    Se aplica la Mutacion Uniforme
    :param pobl: recive poblacion
    :return: poblacion mutada
    """

    for i in range(len(pobl)-n_selecionados):

        if rd.random() <= prob_mutacion:
            # se realiza la mutacion
            vk_punto = rd.randint(0,1)
            if vk_punto ==0: # para x1 [0,20]
                pobl[i][vk_punto] = rd.uniform(0,20)
            else:
                pobl[i][vk_punto] = rd.uniform(0,30)
    return pobl


#inicio
pob = crear_poblacion()

print("Poblacion inicial")
for ind in pob:
    print(ind)

for w in range(1000):
    pob = seleccion_cruza(pob)
    pob = mutacion(pob)

print("\nPoblacion Final")
for ind in pob:
    print(ind)

aptitudes = []
ordenados = []
for z in pob: # se recorre en cada individuo
    # se calcula su aptitud y se guarda como : [aptitud,[x1,x2]] => [2092.030,[2,5]]
    aptitudes.append([aptitud(z),z])
for w in sorted(aptitudes,reverse= 1): # los oredena de mayor a menor
    ordenados.append(w[1])

print("\nFin ------------------------------>>>\n",ordenados[-1],"\nEvaluación===>",aptitud(ordenados[-1]))