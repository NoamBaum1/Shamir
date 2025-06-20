#Matrice de Gauss

k=int(input("Quel est le nombre de points nécessaires pour retrouver la fonction (nombre supérieur à 0) ?\n"))
if k <= 0:
	print("Erreur, on ne peux pas trouver de courbe sans points au préalable")
else:
	pts = []
	for i in range(k):
		pts.append(int(input("Quelles est l'abscisse du point n°"+str(i+1)+"\n")))
		pts.append(int(input("Quelles est l'ordonnée du point n°"+str(i+1)+"\n")))


	def afficher(k,Matrice_Gauss):
		for c in range(k):
			for l in range(k+1):
				print(Matrice_Gauss[c*(k+1)+l],end=" , ")
			print()
			
			
	Matrice_Gauss=[]


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
		print("Les points fournis ne sont pas adaptés")
	else:
		print("Matrice diagonalisée :")
		afficher(k,Matrice_Gauss)
		print("La fonction est : f(x) = ",end="")
		for c in range(k):
			if c == 0:
				print(Matrice_Gauss[k],end="",sep="")
			elif c == 1:
				print(" + ",Matrice_Gauss[(c+1)*(k+1)-1],"x",end="",sep="")
			else:
				print(" + ",Matrice_Gauss[(c+1)*(k+1)-1],"x^",c,end="",sep="")

		print()
