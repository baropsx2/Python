'''
Created on 26/07/2018

@author: David Barocio
'''

i=j=0
while i <= 5:
    while j <= 9:
        print("El minuto es " + str(i) + str(j))
        j+=1
    j=0
    i+=1
    while i <= 5:
        while j <= 9:
            print("El segundo es " + str(i) + str(j))
            j+=1
        j=0
        i+=1
