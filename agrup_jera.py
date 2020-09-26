import random
import bokeh

def genera_coord(numero_coordenadas):
    coordenadas = []
    for _ in range(numero_coordenadas):
        x , y = random.randint(-50,50) , random.randint(-50,50)
        coordenadas.append((x,y))

    return coordenadas

def distancia_euclidiana(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def genera_distancias(coordenadas):
    distancias = []
    for a in range(len(coordenadas)):
        for b in range(a+1,len(coordenadas)):
            distancias.append(distancia_euclidiana(coordenadas[a],coordenadas[b]))        
    return distancias

def dicc_distancias(coordenadas,distancias):
    keys = []
    
    for a in range(len(coordenadas)):
        for b in range(a+1,len(coordenadas)):
            keys.append(f"{str(coordenadas[a])},{str(coordenadas[b])}")
    
    diccionario_distancias = dict(zip(keys,distancias)) 
    return diccionario_distancias

def cluster_jerarquico():
    
    distancia_minima = min(dic_distancias.values())
    print(distancia_minima)


if __name__ == "__main__":
    random.seed(1994)
    numero_coordenadas = int(input("Introduzca el número de coordenadas que desea generar: "))
    coordenadas = genera_coord(numero_coordenadas)
    distancias = genera_distancias(coordenadas)
    dic_distancias = dicc_distancias(coordenadas,distancias) 
    
    for coord in dic_distancias.items():
        print(coord)


        