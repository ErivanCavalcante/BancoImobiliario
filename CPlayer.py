'''
Created on 25 de ago de 2016

@author: Erivan
'''
import random
from CCasa import CCasa

class CPlayer(object):
    
    def __init__(self, _id, nome):
        self.mId = _id;
        self.mNome = nome;
        self.mValorDado = 0;
        self.mCasaAtual = 0; #primeira casa
        self.mDinheiro = 5000;
        self.mListaProp = [];
        self.mVivo = True;
        
    def RolarDados(self):
        self.mValorDado = random.randint(1, 6);
        
    def AdicionarDinheiro(self, valor):
        self.mDinheiro += valor;
        
    def RemoverValor(self, valor):
        if self.mDinheiro < valor:
            return False;
        
        self.mDinheiro -= valor;
        
        return True;
        
    def PagarValor(self, paraObj, valor):
        if self.mDinheiro < valor:
            return False;
        
        self.mDinheiro -= valor;
        
        if paraObj != -1:
            paraObj.AdicionarDinheiro(valor);
        
        return True;
        
    def ImprimirProp(self):
        i = 0;
        
        for prop in self.mListaProp:
            if isinstance(prop, CCasa):
                print(str(i) + ") " + prop.mNome + "\n");
                i += 1; 
            
    
    def AdicionarProp(self, prop):
        #Testa se ja existe na lista
        if self.mListaProp.count(prop) > 0:
            return False;
        
        self.mListaProp.append(prop); 
        prop.mIdDono = self.mId;
        
        return True;
    
    def RemoverProp(self, prop):
        #Testa se ja existe na lista
        if self.mListaProp.count(prop) == 0:
            print("Count");
            return False;
        
        if isinstance(prop, CCasa) == False:
            print("Prop");
            return False;
        
            
        self.mListaProp.remove(prop);
        prop.mIdDono = -1;
        
        return True;
    
    def ImprimirEstatistica(self):
        print("Nome =", self.mNome);
        print("Valor Dado =", self.mValorDado);
        print("Casa Atual =", self.mCasaAtual);
        print("Dinehiro =", self.mDinheiro);
        print("Propriedades =");
    
        for prop in self.mListaProp:
            if isinstance(prop, CCasa):
                print(prop.mNome, "Num Construcoes =", prop.mNumCasas - 1);