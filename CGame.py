'''
Created on 25 de ago de 2016

@author: Erivan
'''
from CTabuleiro import CTabuleiro
from CBanco import CBanco;
from CPlayer import CPlayer;
from builtins import input, str
import os


class CGame(object):
    
    def __init__(self):
        self.mOpcaoSelecionada = -1;
        self.mNumRodadas = 0;
        self.mTabuleiro = CTabuleiro();
        self.mBanco = CBanco();
        self.mListaPlayers = [];
        self.mPlayerAtual = 0;
        #Controla o numero do jogadores reais os outros sao NPC
        self.mNumPlayers = 0;
        self.mAtualId = -1; #id do player atual
    
    #roda td o jogo   
    def Rodar(self):
        self.InicarJogo();
        os.system('cls');
       
        while True:
            
            
            print("O que fazer?\n1) Continuar \n2) Estatistica \n3)Sair");
            
            #pega a opcao
            self.mOpcaoSelecionada = int(input());
            
            #testa se deve sair
            if self.mOpcaoSelecionada == 2:
                self.mPlayerAtual.ImprimirEstatistica();
                continue;
            elif self.mOpcaoSelecionada == 3:
                break;
        
            #rola os dados e anda ate a casa
            self.RolarDado();
            
            #casa atal
            casa = self.mTabuleiro.mListaCasas[self.mPlayerAtual.mCasaAtual];
            
            #testa se a prop tem dono
            #se nao tem dono
            if self.PropTemDono(casa) == False or self.SouDonoProp(casa):
                self.ComprarProp(casa);
            else: #se a prop ja tiver dono
                #tenta pagar
                #se for o banco manda o obj como -1
                if self.PagarValorProp(self.mListaPlayers[casa.mIdDono] if not self.PropDoBanco(casa) else -1, casa) == False:
                    #tem alguma prop
                    if len(self.mPlayerAtual.mListaProp) == 0:
                        self.mPlayerAtual.mVivo = False; #finaliza esse player
                    else:
                        valor = self.PegarValorProp(casa); #valor da estadia
                        #se nao tem dinheiro para pagar tenta hipotecar
                        while self.mPlayerAtual.mDinheiro < valor:
                            self.HipotecarProp();
                        
    
            
            self.ProximaRodada();
            
            
        self.FinalizarJogo();
    
    def InicarJogo(self):
        print("\t\t\t\tBanco Imobiliario");
        print("\n\nDigite o numero de jogadores:\n");
        
        while True:
            #pega a opcao
            self.mOpcaoSelecionada = int(input());
            
            #ao digitar -1o jogo acaba
            if self.mOpcaoSelecionada == -1:
                self.mSair = True;
                break;
            elif self.mOpcaoSelecionada == 0 or self.mOpcaoSelecionada > 4:
                print("\nTente de novo");
                continue;
            
            #Cria os players
            self.mNumPlayers = self.mOpcaoSelecionada;
            
            for i in range(0, self.mOpcaoSelecionada):
                print("\nDigite o nome do jogador ", str(i), ":\n")
                nome = input();
                #cria e coloca na lista
                obj = CPlayer(i, nome);
                self.mListaPlayers.append(obj);
                
            
            print("\nInicio do jogo...\n\n");
            
            #coloca o primeiro player no atual
            self.ProximaRodada();

            self.mSair = False;
            
            break;
    
    def RolarDado(self):
        print("\nJogador " + self.mPlayerAtual.mNome + " rolando os dados...");
        self.mPlayerAtual.RolarDados();
        
        print("\nValor Dado eh " + str(self.mPlayerAtual.mValorDado));
        
        print("\nAndando " + str(self.mPlayerAtual.mValorDado) + " casas...");
        
        #anda as casas
        self.mPlayerAtual.mCasaAtual += self.mPlayerAtual.mValorDado;
        
        #testa se deu uma volta
        if self.mPlayerAtual.mCasaAtual > self.mTabuleiro.mNumCasas - 1:
            #Pega quanto passou do valor
            valor = self.mPlayerAtual.mCasaAtual % self.mTabuleiro.mNumCasas - 1;
            self.mPlayerAtual.mCasaAtual = valor;
            
            self.mBanco.PagarValorvolta(self.mPlayerAtual);
            
            print("\nVolta completa");
            print("\nJogador " + self.mPlayerAtual.mNome + " ganhou mais R$ 100,00");
    
    def ProximaRodada(self):
        numVivos = 0;
        #testa se tem alguem vivo
        for obj in self.mListaPlayers:
            if obj.mVivo:
                numVivos += 1;
                
        if numVivos <= 1:
            print("Vitoria do jogador", self.mPlayerAtual.mNome);
            self.FinalizarJogo();
            
        self.mAtualId += 1; 
        if self.mAtualId >= self.mNumPlayers:
            self.mAtualId = 0;
            
        #novo player
        self.mPlayerAtual = self.mListaPlayers[self.mAtualId];
        while self.mPlayerAtual.mVivo == False:
            self.mAtualId += 1; 
            if self.mAtualId >= self.mNumPlayers:
                self.mAtualId = 0;
                
            #novo player
            self.mPlayerAtual = self.mListaPlayers[self.mAtualId];
            
        print("\nVez do jogador " + self.mPlayerAtual.mNome); 
    
    def ComprarProp(self, casa):
        #limita a qtd de prop
        if casa.mNumCasas >= 4:
            return False;
        
        valor = 0.00;
        
        #testa se tem alguma prop
        if casa.mNumCasas == 0:
            valor = casa.mValorProp;
        elif casa.mNumCasas == 1: 
            valor = casa.mValorUmaCasa;
        elif casa.mNumCasas == 2: 
            valor = casa.mValorDuasCasas;
        elif casa.mNumCasas == 3: 
            valor = casa.mValorUmHotel;
        
        #testa se tem alguma prop
        if casa.mNumCasas == 0:
            print("Dseja comprar a propriedade", casa.mNome, "por R$ ", valor);
        elif casa.mNumCasas > 0: 
            print("Dseja construir na prorpiedade", casa.mNome, "por R$ ", valor);
        
        print("1) Sim \n2) Nao");
        
        self.mOpcaoSelecionada = int(input());
        
        if self.mOpcaoSelecionada == 2:
            return False;
        
        print("primeiro if");
        
        #compra a prop para o player atual
        if self.mPlayerAtual.RemoverValor(valor) == False:
            print("O jogador", self.mPlayerAtual.mNome, "nao tem dinheiro suficiente para comprar a propriedade");
            return False;
        
        print("segundo if");
        self.mPlayerAtual.AdicionarProp(casa);
        
        casa.mNumCasas += 1;
        
        print("O jogador", self.mPlayerAtual.mNome, " Concluiu a operacao com sucesso");
        print("ultimo if");
        return True;
    
    def SouDonoProp(self, casa):
        if casa.mIdDono == self.mPlayerAtual.mId:
            return True;
        
        return False;
    
    def PropTemDono(self, casa):
        if casa.mIdDono == -1:
            return False;
        
        return True;
    
    def PropDoBanco(self, casa):
        if casa.mIdDono == -2:
            return True;
        
        return False;
    
    def ConstruirProp(self):
        pass;
    
    def HipotecarProp(self):
        pro = 0;
        
        print("\nEcolha a propriedade q deseja vender.\n\n")
        
        self.mPlayerAtual.ImprimirProp();
        
        pro = int(input());
        
        if pro == -1 or pro > len(self.mPlayerAtual.mListaProp):
            return False;
        
        #o banco paga o valor
        if self.mBanco.HipotecarCasa(self.mPlayerAtual, self.mPlayerAtual.mListaProp[pro]) == False:
            return False;
        
        return True;
    
    def PagarValorProp(self, paraObj, casa):
        valor = self.PegarValorProp(casa);
        
        if self.mPlayerAtual.PagarValor(paraObj, valor) == False:
            print("O jogador ", self.mPlayerAtual.mNome, "nao tem dinheiro para pagar R$ ", str(valor), " ao jogador ", paraObj.mNome);
            return False;
        
        print("O jogador ", self.mPlayerAtual.mNome, " pagou R$ ", str(valor), " ao jogador ", paraObj.mNome);
        return True;
    
    def PegarValorProp(self, casa):
        valor = 0.00;
        
        if casa.mNumCasas == 1:
            valor = casa.mValorHipoProp;
        elif casa.mNumCasas == 2:
            valor = casa.mValorHipoUmaCasa;   
        elif casa.mNumCasas == 3:
            valor = casa.mValorHipoDuasCasas;
        elif casa.mNumCasas == 4:
            valor = casa.mValorHipoUmaHotel;
            
        return valor;    
        
        
    def DesistirJogo(self):
        print("Deseja desitir do jogo?");
        print("1) Sim \n2) Nao");
        
        self.mOpcaoSelecionada = int(input());
        
        if self.mOpcaoSelecionada == 1:
            #remove da lista
            self.mListaPlayers.remove(self.mPlayerAtual);
            self.mPlayerAtual = -1;
            return True;
        
        return False;
    
    def FinalizarJogo(self):
        print("Obrigado por jogar");