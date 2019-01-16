'''
Created on 25 de ago de 2016

@author: Erivan
'''

class CBanco(object):
    
    def __init__(self):
        self.mListaProp = [];
        
    def PagarValorvolta(self, obj):
        obj.mDinheiro += 100;
        
    def HipotecarCasa(self, obj, casa):
        if obj.RemoverProp(casa):
            obj.AdicionarDinheiro(casa.mValorHipoBanco);
            #adiciona o id do banco a prop
            casa.mIdDono = -2;
            return True;
        
        return False;
        