
# Introduction

The aim of this project is to understand how works [Shamir's Secret-Sharing Scheme](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).
This project was fully created during an internship of 2 weeks and was only implemented for educational reasons.


# How to use it


##  *Shamir.py*
This project can be used with *Shamir.py* which is more user-friendly and use terminal inputs to work.


## *Shamir.ipynb*
On the other hand *Shamir.ipynb* can be used as a quicker and more professional way to experiment Shamir's Schemes and use *data.txt* to work.
The program will only work if the data is correctly specified like in this exemple :
    
$(x_1;y_1)$<br>$(x_2;y_2)$<br>$(x_3;y_3)$<br>$\dots$


### 2 functions are available :

  - ``coder( n, k, s )``

 
	 >Where :
		>- n is the number of people who has a part of the secret 
		 >- k is the number of people who is needed to decode the secret
	     >- s is the secret (in number)

It is used to secure the secret and split different shares to
   people. The coordinates are written in *data.txt* .

- ``decoder( k )``
 
 >Where k is the number of people who is needed to decode the secret


It is used to find the secret with the coordinates in *data.txt* .


## *Gauss_Matrix.py* and *Gauss_Matrix.ipynb*
The code *Gauss_Matrix.py* / *Gauss_Matrix.ipnb* (which are almost the same) were used as draft to the decode function of Shamir's secret-sharing scheme by using a Matrix that solves itself by diagonalization.

It was essential to develop this program before implementing it directly in the main program.

> Note : *Gauss_Matrix.ipynb* now also uses the coordinates in *data.txt* instead of inputs

Gauss_Matrix.ipynb uses the fonction ``solve( k )``
>Where k is the degree $+1$ of the polynomial or the number of points needed




## *Share_Refreshing.ipynb*

This program use a polynomial characteristic to create new shares using the $x$ coordinates of the initial shares.
It uses the data in *data.txt* written in an other way than the other :
 
$x_1$<br>$x_2$<br>$x_3$<br>$\dots$

The function ``share_refreshing( k )`` creates new shares with the data in *data.txt*

>Where k is the number of people who is needed to decode the secret







## *Finite_Field variant*

The variant Finite_Field uses Shamir's Scheme on a finite modular field. It includes the scripts :

 - *Shamir_Finite_Field.ipynb*
 - *Gauss_Matrix_Finite_Field.ipynb*
 - *Share_refreshing_Finite_Field.ipynb*

This variant is used in real application of secret sharing as infinite field can give information as they are implemented on $\mathbb{Z}$ to facilitate the calculation and so the computer don't omit some decimals.


The scripts uses the same fonction but with some slight modification:

 - In *Shamir_Finite_Field.ipynb*:

	``coder_finite_field( n, k, s , modulo )``

	>Where :
	> - n is the number of people who has a part of the secret 
	> - k is the number of people who is needed to decode the secret
	> - s is the secret (in number)
	> - modulo is the modulo of the field


	``decoder_finite_field( k, modulo )``
	
	> Where :
	> - k is the number of people who is needed to decode the secret
	> - modulo is the modulo of the field

 - In *Gauss_Matrix_Finite_Field.ipynb*:
 
 
	 ``decoder_finite_field( k, modulo )``
	
	> Where :
	> - Where k is the degree $+1$ of the polynomial or the number of points needed
	> - modulo is the modulo of the field
 - In *Gauss_Matrix_Finite_Field.ipynb*:
 
 
	 ``share_refreshing_finite_field( k, modulo )``
	
	> Where :
	> - Where k is the degree $+1$ of the polynomial or the number of points needed
	> - modulo is the modulo of the field

#
###### Created by Noam Baum, 16

