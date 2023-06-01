#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:57:51 2021

@author: luisosvaldo
"""

#%% 

class Mi_Primera_Clase():
    pass

Mi_Primer_Objeto = Mi_Primera_Clase()
print( Mi_Primer_Objeto) 
#%% Atributos

class Ser_Humano():
    nombre     = ''
    dedos_mano = 5
    desdos_pie = 5
    orejas     = 2
    nariz      = 1
    
Luis = Ser_Humano()
print(Luis)
print(Luis.orejas)
print(Luis.dedos_mano)

#%% Metodos

class Humano_1():
    nombre = ''
    nariz  = 1
    edad   = 0
    
    # Todos los metodos deben llevar el self
    # La identacion es de 4 espacios
    # La palabra identacion no existe en espaniol
    # debe ser sangrado
    def crecio(self):
        self.edad += 1
        
Natalia = Humano_1()
print(Natalia.edad)

for i in range(20):
    Natalia.crecio()
    
print( Natalia.edad )

#%% Constructor ini

class Humano_2():
    # nombre = ''
    edad   = 0
    nariz  = 1
    nacio = False
    
    def __init__(self, name, ojos, pelo):
        self.nombre = name
        self.color_ojos = 'Ojos ' + ojos
        self.color_pelo = 'Pelo ' + pelo
        self.nacer() #metodo
    
    # Siempre poner el self
    def crecio(self):
        self.edad += 1
    
    def nacer(self):
        print(self.nombre + ' esta llorando :( y tiene ' + str(self.edad) + ' anios')
        self.nacio = True
    
Felix = Humano_2('Felix', 'Negros', 'Negro')
print(Felix.nacio)
print(Felix.edad)
print(Felix.nombre)

#%% Herencia

class Humano_3( Humano_2 ):
    def __init__(self, name, ojos, pelo):
        Humano_2.__init__(self, name, ojos, pelo)
        self.enamorado = False
        
    def enamorarse(self):
        self.enamorado = True
        
    def crecio(self):
        self.edad += 2
        
Humano_experimental = Humano_3('Bayron', 'Negros', 'Rubio')
print(Humano_experimental.nombre)
print(Humano_experimental.enamorado)
print(Humano_experimental.edad)
Humano_experimental.crecio()
print(Humano_experimental.edad)
Humano_experimental.enamorarse()
print(Humano_experimental.enamorado, Humano_experimental.edad)




        

















