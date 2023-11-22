""" programme à compléter du kPPV"""
import csv
import math

nbExParClasse = 50
nbApprent = 25
nbCaract = 4

def lectureFichierCSV():
    with open("iris.data", "r")as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    
    # get list of 5 classes
    classes = []
    for data in dataset:
        if data[nbCaract] not in classes:
            classes.append(data[nbCaract])
    
    # create a tab for every class
    datasets = { classe:[] for classe in classes }
    
    for data in dataset:
        datasets[data[nbCaract]].append(data[:nbCaract])    
    
    return datasets

def calculDistance(dataset, dataToTest):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []
    for classe in dataset:
        for datas in dataset[classe][:nbExParClasse-nbApprent]:
            distance = 0
            
            for i in range(len(dataToTest)):
                distance += pow(float(datas[i])-float(dataToTest[i]), 2)
                
            distances.append({"classe": classe,"distance": distance ** 0.5, "testVector": dataToTest, "dataVector": datas})
    return distances
         
def getMin(distances):
    return min(distances, key=lambda x:x["distance"])       
          
          
def matriceConfusion(dataset):
    matrice = {classe:{classe:0 for classe in dataset} for classe in dataset}

    for classe in dataset:
        for datas in dataset[classe][nbApprent:]:
            distances = calculDistance(dataset, datas)
            minDistance = getMin(distances)
            
            sourceClasse = classe
            endClasse = minDistance["classe"]
            
            matrice[sourceClasse][endClasse] += 1

    return matrice

if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()
    
    distances = calculDistance(dataset, [5.8,2.7,5.1,1.9])
    # print(distances)
    minimum = getMin(distances)
    print(minimum)
    
    print("Matrice de confusion")
    matriceDeConfusion = matriceConfusion(dataset)
    print("from\t\tto")
    for data in matriceDeConfusion:
        print(data,"\t", matriceDeConfusion[data])
#--------------------------------- Fin kPPV -----------------------------------