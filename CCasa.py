'''
Created on 25 de ago de 2016

@author: Erivan
'''

class CCasa(object):
    
    def __init__(self):
        self.mNome = "";
        self.mId = -1;
        self.mIdDono = -1;
        self.mNumCasas = 0;
        #compra do terreno e as casas
        self.mValorProp = 100.0;
        self.mValorUmaCasa = 10.0;
        self.mValorDuasCasas = 20.0;
        self.mValorUmHotel = 30.0;
        
        self.mValorHipoProp = 40.0;
        self.mValorHipoUmaCasa = 50.0;
        self.mValorHipoDuasCasas = 60.0;
        self.mValorHipoUmaHotel = 70.0;
        self.mValorHipoBanco = 80.0; #venda ao banco
        
        