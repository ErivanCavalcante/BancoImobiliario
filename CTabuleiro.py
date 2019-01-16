'''
Created on 25 de ago de 2016

@author: Erivan
'''
from CCasa import CCasa

class CTabuleiro(object):
    
    def __init__(self):
        self.mListaCasas = [];
        self.mNumCasas = 120;
        
        self.CarregarCasas();
        
    def PegaCasa(self, pos):
        if pos < len(self.mListaCasas):
            return self.mListaCasas[pos];
        
    def CarregarCasas(self):
        for i in range(7):
            casa = CCasa();
            casa.mNome = "Casa" + str(i);
            self.mListaCasas.append(casa);
             
        #no fim do carrregamento
        self.mNumCasas = len(self.mListaCasas);
            