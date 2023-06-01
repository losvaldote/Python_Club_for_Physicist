# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO BASE
"""

# Codigo para hacer un conversor de temperatura.
#%% 

## IMPORTAMOS los paquetes necesarios.
import sys
from PyQt5 import QtWidgets, QtCore

#%%

## GENEREMOS la clase que defina la GUI
# Nombre de la clase MyApp
class MyApp(QtWidgets.QWidget): # Hereda QWidget
                                # La herencia se da en class ...
    ## CREAMOS el constructor de la clase
    def __init__(self):
        ## HEREDAMOS los atributos y métodos de la clase QWidget llamando su
        ##    constructor
        QtWidgets.QWidget.__init__(self)
        ## Hasta aqui generamos una subclase idéntica a la clase QWidget
        
        self.label = QtWidgets.QLabel("Hola como estas",self) # Ya le pertenece a la widget
        #self.label.setGeometry(100, 100, 100, 20) # Posicion fija del texto en la ventana
        # No se recomienda usar setGeometry
        
        # Se genera la layout
        lay_1 = QtWidgets.QVBoxLayout()
        
        # Se asigna la layout a la widget
        self.setLayout(lay_1)
        
        # Se asigna el label a la layout
        lay_1.addWidget(self.label)
        # Con esta linea se ajusta hacia arriba y hacia abajo 
        # cuando agrandamos la ventana pero no hacia la derecha
        
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        # Esta linea asigna la posicion del texto siempre en el centro
        # aun cuando se cambie el tamanio de la ventana.
        # Se impone un tamanio minimo de la ventana.
        
        # Vamos a poner un boton
        self.btn_1 = QtWidgets.QPushButton("Botón 1")
        # Se agrega el boton a la layout
        lay_1.addWidget(self.btn_1)
        # Hacemos que el boton se quede marcado o no
        #self.btn_1.setCheckable(True)
       
        self.spin = QtWidgets.QSpinBox()
        self.spin.setRange(-100, 100)
        self.spin.setPrefix("Temp = ")
        self.spin.setSuffix(" ºC")
        self.spin.setSingleStep(10)
        self.spin.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        lay_1.addWidget(self.spin)
        # A la layout no le pones self porque no lo vamos a editar
        # aunque si puede llevarlo
       
        self.Dspin = QtWidgets.QDoubleSpinBox()
        self.Dspin.setRange(-200, 300)
        self.Dspin.setPrefix("Temp = ")
        self.Dspin.setSuffix(" ºF")
        self.Dspin.setSingleStep(2.5)
        self.Dspin.setDecimals(1)
        self.Dspin.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        lay_1.addWidget(self.Dspin)
        
        
        self.ch = QtWidgets.QCheckBox("Seleccioname :3")
        lay_1.addWidget(self.ch)
        self.ch.setCheckState(1)
       
        # Vamos a pasar la senial del boton
        self.btn_1.clicked.connect(self.btn_1_clicked)
        self.spin.valueChanged.connect(self.spin_changed)
        self.Dspin.valueChanged.connect(self.Dspin_changed)
        self.ch.stateChanged.connect(self.ch_check)
        
        self.spin_changed(0)
        
    # Vamos a crear los metodos
    
    #def btn_1_clicked(self, state):
    def btn_1_clicked(self):
        # Definiendo metodo para el click del boton
        print('Botón 1 clickeado')
        #print(state)
        # Esto lo va a mostrar en la consola
        
    def spin_changed(self, value):
        fahr = 9.0/5.0 * value + 32.0
        self.Dspin.setValue(fahr)
    
    def Dspin_changed(self, value):
        cels = (value -32) * 5.0/9.0
        self.spin.setValue(int(cels))
        # Esto es ciclico por eso no puedo dejar el 100
    
    def ch_check(self, state):
        if state :
            print("Seleccionado")
        else:
            print("Deseleccionado")
        
#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

# Se genera una ventana vacia