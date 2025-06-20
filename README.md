# Introduction

The aim of this project is to understand how works Shamir's Secret-Sharing Sheme.
This project was fully created during an internship of 2 weeks and was only implemented for educational reasons


# How to use it


##  *Shamir.py*
This project can be used with Python *Shamir .py* which is more user-friendly and use terminal inputs to work.


## *Shamir_v2.ipynb*
On the other hand *Shamir_v2.ipynb* can be used as a quicker and more professional way to experiment Shamir's Shemes and use *data.txt* to work :
    The program will only work if the data is correctly specified like in this exemple :
    
    (x1;y1)
    (x2;y2)
    (x3;y3)
    ...

### 2 fonctions are available :



  - **`coder( n, k, s )`**



 
 >Where :
	 - n is the number of people who has a part of the secret 
	 - k is the number of people who is needed to decode the secret
     - s is the secret (in number)

It is used to secure the secret and split different points to
   people. The coordinates are written in *data.txt* .



- **`decoder( k )`**
 
 >Where k is the number of people who is needed to decode the secret


It is used to find the secret with the coordonates in *data.txt* .


## *Gauss_Matrix.py* and *Gauss_Matrix.ipnb*
Last, the code *Gauss_Matrix.py* / *Gauss_Matrix.ipnb* (which are almost the same) were used as draft to the decode fonction of Shamir's secret-sharing sheme by using a Matrix that solves itself by diagonalization.

It was essential to develop this program before implementing it directly in the main program

> Note : Gauss_Matrix now also uses the coordinates in *data.txt* instead of inputs





###### Created by Noam Baum,16
