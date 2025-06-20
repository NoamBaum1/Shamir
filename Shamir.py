#Algorithme  en python de codage et de décodage du partage de secret de Shamir
#Par Noam Baum, 16 ans, stagiaire

import random
print("\n\n")
#codage
def codage(n,k,secret): #avec k le nombre de points nécessaires pour décoder et n le nombre de points partagés
    f= [secret]
    pts = []
    ptX = 0
    for i in range(k-1):
        f.append(random.randint(-30,30))
    for i in range(n):
        while not(ptX in pts) or ptX != 0:
            print(ptX)
            ptX = random.randint(-200,200)
            ptY = 0
            degre = 0
            for i in f:
                ptY = ptY + i*(ptX**degre)
                degre += 1
            break
        pts.append("("+str(ptX)+";"+str(ptY)+")")
    
    return pts
    
#decodage

def decoder(k,pts):

    Matrice_Gauss = []
    for c in range(k):
        for l in range(k):
            Matrice_Gauss.append(pts[2*c]**l)
        Matrice_Gauss.append(pts[2*c+1])


    impossibilite = 0
    for colonneactive in range(k):
        
        pivot=Matrice_Gauss[colonneactive*(k+1)+colonneactive]
        if pivot == 0:
            impossibilite = 1
            break
        for l in range(k+1):
            
            Matrice_Gauss[colonneactive*(k+1)+l] = Matrice_Gauss[colonneactive*(k+1)+l]/pivot

        for c in range(k):
            coefcolonne = Matrice_Gauss[c*(k+1)+colonneactive]
            for l in range(k+1):
                if c != colonneactive:
                    Matrice_Gauss[c*(k+1)+l]=Matrice_Gauss[c*(k+1)+l]-Matrice_Gauss[colonneactive*(k+1)+l]*coefcolonne
    
    if impossibilite == 1:
        return "Les points fournis ne sont pas suffisants"
    else:
        return Matrice_Gauss[k]



action=int(input("Veux-tu coder(1) ou décoder(2) un secret ?\n"))

if action == 1:
    n = int(input("Avec combien de personnes veux-tu partager le secret ?\n"))
    k = int(input("Combien de personnes doivent être nécessaires pour trouver le secret ?\n"))
    if k <= 0:
        print("Erreur, cette valeur n'est pas valable")
    else:
        secret = int(input("Quel est le secret (en nombre) ?\n"))
        print("Voici les différents points à distribuer à chaques personnes :")
        
        for i in codage(k,n,secret):
            print(i)
        
else:
    pts = []
    k = int(input("Combien de personnes sont nécessaires pour trouver le secret ?\n"))
    if k <= 0:
        print("Erreur, cette valeur n'est pas valable")
    for i in range(k):
        pts.append(int(input("Quelles est l'abscisse du point n°"+str(i+1)+"\n")))
        pts.append(int(input("Quelles est l'ordonnée du point n°"+str(i+1)+"\n")))
        
    print("le secret est : ",decoder(k,pts))
        
print("\n\nFin du programme\n\n")