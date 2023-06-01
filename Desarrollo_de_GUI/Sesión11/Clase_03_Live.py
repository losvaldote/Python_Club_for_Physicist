# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO BASE
"""
#%% 

## IMPORTAMOS los paquetes necesarias.
import sys, cv2
from PyQt5 import QtWidgets
import pyqtgraph as pg
import numpy as np
#%%

## GENEREMOS la clase que defina la GUI
class MyApp(QtWidgets.QWidget):
    ## CREAMOS el constructor de la clase
    def __init__(self):
        ## HEREDAMOS los atributos y métodos de la clase QWidget llamando su
        ##    constructor
        QtWidgets.QWidget.__init__(self)
        ## Hasta aqui generamos una subclase idéntica a la clase QWidget
        lay = QtWidgets.QVBoxLayout()
        self.setLayout(lay)
        
        x = np.arange(0, 30, 0.01)
        y1 = np.sin(x)
        y2 = np.cos(x)
        img_array = cv2.imread('test.jpg')
        
        
        self.plot_widget = pg.PlotWidget()
        self.plot_widget_2 = pg.PlotWidget()
        self.data_item_2 = pg.PlotDataItem()
        self.image_item = pg.ImageItem(img_array)
        
        self.plot_widget_2.setAspectLocked(True)
        
        self.data_item_1 = self.plot_widget.plot(x, y1)
        self.data_item_2.setData(x, y2)
        self.plot_widget.addItem(self.data_item_2)
        self.plot_widget_2.addItem(self.image.item)
        self.image_item.rotate(-90)
        
        lay.addWidget(self.plot_widget)
        lay.addWidget(self.plot_widget_2)
#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
