# Excersice 1
def carre (n):
    res = []
    for x in n:
        res += [x*x]
    return res
list =[1,5,6]
print (carre(list))
list1 = [x**3 for x in range (5,16)]
print(list1)
# from random import *
# def auhasard (lis):
#     i = randint (0, len(lis)- 1)
#     res = lis[i]
#     del lis[i]
#     return res
# lis1 = [1,5,6,7,89,8]
# print (auhasard(lis1))    
uno = []
for i in range(1,10):
        for c in ['jaune','rouge','vert','bleu']:
              uno = uno + [[i,c]]
print (uno)
#Exercise5
somme = []
for a in range (1,7):
        for b in range (1,7):
                for c in range (1,7):
                        if a + b + c == 6:
                                somme += [[a,b,c]]
print (somme)

#Exercise 6.1
def estUnaire (liste):
        for x in liste:
                if x != 1:
                        return False
        return True
list2 = [1,5,6,7,0]
print (estUnaire(list2))
#Exercise 6.2
def valeursAsolues (liste1):
        for i in range(len(liste1)):
                liste1[i] = abs(liste1[i])
list6 = [4,-6,-8,8,9]      
print (valeursAsolues(list6))
#Excersie 6.3
def different (liste2):
        for i in range (0,len(liste2)):
                for j in range (i+1, len(liste2)):
                        if liste2[i] == liste2[j]:
                                return False
        return True
diff = [q,g,g]
print (different(diff))
#Exercise 6.4
def alphabétique (l):
        for i in range(0,len(l)-1):
                if l[i] > l[i + 1]:
                        return False
        return True
#Excercise 7.1
def sommeListe (l):
        res = 0
        for i in l:
                res += i
        return res
l1 = [1,6,7]
print (sommeListe(l1))      
#Exercise 7.2
def listDiviseurs (n):
        res = []
        for i in range (1,n):
                if n % i == 0:
                   res += [i]
        return res
print (listDiviseurs(10))
def Estparfait(n):
     return sommeListe(listDiviseurs) 
print (Estparfait(10))

  