import os
import sys, traceback

tabela = []
tabelaNova1 = []
tabelaNova2 = []
tabelaNova3 = []
tabelaNova4 = []
ultimoIntervalo = []
amostraTabela = []

def exibirMenuPrincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################ESTATÍSTICA E PROBABILIDADE###################")
    print("1 - Cadastrar ou adicionar valores a Tabela existente")
    print("2 - Listar Tabela")
    print("3 - Mostrar Rol da Tabela")
    print("4 - Mostrar o Intervalo de classes da Tabela")
    print("5 - Media")
    print("6 - Media Ponderada")
    print("7 - Porcentagem")
    print("8 - Quartil")
    print("9 - Mediana")
    print("10 - Moda")
    print("11 - Decil")
    print("12 - Percentil")
    print("13 - Variância (população e amostra)")
    print("14 - Desvio padrão (população e amostra)")
    print("15 - Coeficiente de variação.")
    print("16 - Erro Padrão")
    print("17 - Distribuição binomial.")
    print("18 - Distribuição de Poisson.")
    print("0 - Sair")
    try:
        opcao = int(input("Escolha uma opcao: "))
    except Exception:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        exibirMenuPrincipal()
    if opcao == 0:
        print("Finalizado!")
        os.system("pause")
        sys.exit(0)
    elif opcao == 1:
        cadastro()
    elif opcao == 2:
        listarTabela()
    elif opcao == 3:
        rol(1)
    elif opcao == 4:
        intervaloClasses()
    elif opcao == 5:
        media()
    elif opcao == 6:
        mediaPonderada()
    elif opcao == 7:
        porcentagem()
    elif opcao == 8:
        quartil()
    elif opcao == 9:
        mediana(1,tabela)
    elif opcao == 10:
        moda()
    elif opcao == 11:
        decil()
    elif opcao == 12:
        percentil()
    elif opcao == 13:
        variancia(1)
    elif opcao == 14:
        desvioPadrao(1)
    elif opcao == 15:
        coeficienteDeVariacao()
    elif opcao == 16:
        erroPadrao()
    elif opcao == 17:
        distribuicaoBinomial()
    elif opcao == 18:
        distribuicaoPoisson()
    else:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        exibirMenuPrincipal()

def cadastro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################CADASTRO###################")
    try:
        valor = float(input("Digite um Valor (0 - Finaliza): "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        cadastro() 
    while (valor != 0):
        tabela.append(valor) 
        try:
            valor = float(input("Digite um Valor (0 - Finaliza): "))
        except Exception:
            print("Opção Invalida!")
            os.system("pause")
            cadastro()       
    exibirMenuPrincipal()

def listarTabela():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Tabela###################")
    i = 1
    for elemento in tabela:
        print ("%i° Valor: %i" %(i,elemento))
        i += 1
    os.system("pause") 

    exibirMenuPrincipal()
        
def rol(x):
    for j in range (len(tabela)-1):
        aux1 = False
        for k in range (len(tabela)-1):
            if(tabela[k] > tabela[k+1]):
                aux = tabela[k]
                tabela[k] = tabela[k+1]
                tabela[k+1] = aux
                aux1 = True
        if(aux1 == False):
            break
    if(x==1):
        listarTabela()

def semiIntervaloClasses(x):
    if(x==1):
        try:
            espaco = int(input("Digite o espaço do intervalo de classes: "))
        except Exception:
            print("Opção Invalida!")
            os.system("pause")
            semiIntervaloClasses()
    elif(x==3):
        try:
            espaco = int(input("Digite o espaço do intervalo de classes: "))
        except Exception:
            print("Opção Invalida!")
            os.system("pause")
            semiIntervaloClasses()
    j = 1
    i = 0
    soma = 0
    rol(2)
    for i in range(0,len(tabela)-1,1):
        fI = 0
        if(tabela[i] == tabela[i+1]):
            j += 1
        if(((j > 1) and (tabela[i] != tabela[i+1])) or ((j > 1) and (tabela[i] == tabela[i+1]) and ((i+1) == (len(tabela)-1)))):
            tabelaNova1.append(j)
            tabelaNova3.append(tabela[i]) 
            j = 1
        elif(j == 1):
            tabelaNova1.append(1)
            tabelaNova3.append(tabela[i])  
        if((i+1) == (len(tabela)-1) and (j==1)):
            tabelaNova1.append(1) 
            if(tabela[i] != tabela[i+1]):
                tabelaNova3.append(tabela[i+1]) 
    i = 0
    if(x==3):
        for i in range(0,len(tabelaNova1),1):
            soma += tabelaNova1[i]
            if((i+1)%espaco == 0):
                tabelaNova2.append(soma)
                soma = 0
            elif(i+1 == (len(tabelaNova1))):
                if(soma-1 > 0):
                    tabelaNova2.append(soma-1)
        soma = tabela[0]
        ultimoIntervalo.append(soma)
        condicao = tabela[(len(tabela)-1)]
        for elemento in tabelaNova2: 
            soma += espaco
            if(soma>=condicao):
                ultimoIntervalo.append(soma)
                break
        fI=0
        for i in range(0,len(tabela),1):
            fI += tabelaNova1[i]
            print("%i"%fI)
            tabelaNova4.append(fI)
        return espaco
    if(x==1):
        for i in range(0,len(tabelaNova1),1):
            soma += tabelaNova1[i]
            if((i+1)%espaco == 0):
                tabelaNova2.append(soma)
                soma = 0
            elif(i+1 == (len(tabelaNova1))):
                if(soma-1 > 0):
                    tabelaNova2.append(soma-1)
        soma = tabela[0]
        for elemento in tabelaNova2: 
            print ("\nClasse: %i |------- %i | Frequência: %i" %(soma,(soma+espaco),elemento))
            soma += espaco

def intervaloClasses():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Tabela###################")
    semiIntervaloClasses(1)
    os.system("pause")    
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()
    exibirMenuPrincipal()

def media():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Media###################") 
    media = 0
    for i in tabela:
        media += i
    media = media/len(tabela)
    print("Media = %.2f"%media)
    os.system("pause")
    exibirMenuPrincipal()

def mediaPonderada():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Media###################") 
    semiIntervaloClasses(0)
    media = 0
    divisor = 0
    i = 0
    for k in tabelaNova3:
        media += (k*tabelaNova1[i])
        divisor += tabelaNova1[i]
        i += 1
    print("Média Ponderada: %.2f"%(media/divisor))
    os.system("pause")    
    exibirMenuPrincipal()

def porcentagem():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Porcentagem###################") 
    print("1 - Maior")
    print("2 - Menor")
    print("3 - Igual")
    print("4 - Entre dois valores")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagem()    
    if(opcao == 1):
        porcentagemMaior()
    if(opcao == 2):
        porcentagemMenor()
    if(opcao == 3):
        porcentagemIgual()
    if(opcao == 4):
        porcentagemEntre()
    else:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        porcentagem() 

def porcentagemMaior():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Porcentagem###################") 
    try:
        valor = float(input("Digite o Valor: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemMaior() 
    semiIntervaloClasses(0)
    porcentagens = []
    i = 0
    nExiste = True
    total = sum(tabelaNova1)
    k = 0
    j = 0
    for i in tabelaNova3:
        if(valor == i):    
            for frequencia in tabelaNova1:
                if(((frequencia*100) / total) > ((tabelaNova1[j]*100)/total)):
                    print("Valor: %i"%tabelaNova3[k]) 
                    print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                    print("Frequência: %i\n"%frequencia)
                    nExiste = False
                k+=1
        if(valor == i):
            break
        j += 1
    if(nExiste):
        print("Não existe porcentagem  maior que %.2f na tabela!"%valor)
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()   
    exibirMenuPrincipal()

def porcentagemIgual():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Porcentagem###################") 
    try:
        valor = float(input("Digite o Valor: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemMaior() 
    semiIntervaloClasses(0)
    porcentagens = []
    i = 0
    nExiste = True
    total = sum(tabelaNova1)
    k = 0
    j = 0
    for i in tabelaNova3:
        if(valor == i):    
            for frequencia in tabelaNova1:
                if(((frequencia*100) / total) == ((tabelaNova1[j]*100)/total) and (k != j)):
                    print("Valor: %i"%tabelaNova3[k]) 
                    print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                    print("Frequência: %i\n"%frequencia)
                    nExiste = False
                k+=1
        if(valor == i):
            break
        j += 1
    if(nExiste):
        print("Não existe porcentagem  igual a %.2f na tabela!"%valor)
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()   
    exibirMenuPrincipal()

def porcentagemMenor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Porcentagem###################") 
    try:
        valor = float(input("Valor da Porcentagem: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemMenor() 
    semiIntervaloClasses(0)
    porcentagens = []
    i = 0
    nExiste = True
    total = sum(tabelaNova1)
    k = 0
    j = 0
    for i in tabelaNova3:
        if(valor == i):    
            for frequencia in tabelaNova1:
                if(((frequencia*100) / total) < ((tabelaNova1[j]*100)/total)):
                    print("Valor: %i"%tabelaNova3[k]) 
                    print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                    print("Frequência: %i\n"%frequencia)
                    nExiste = False
                k+=1
        if(valor == i):
            break
        j += 1
    if(nExiste):
        print("Não existe porcentagem  menor que %.2f na tabela!"%valor)
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()   
    exibirMenuPrincipal()

def porcentagemEntre():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Porcentagem###################") 
    try:
        valor1 = int(input("Primeiro valor do Intervalo: "))
    except Exception:
        print("Opção Invalida! Seu Vacilão")
        os.system("pause")
        porcentagemEntre()
    try:
        valor2 = int(input("Ultima valor do Intervalo: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemEntre() 
    semiIntervaloClasses(0)
    porcentagens = []
    nExiste = True
    total = 0
    k = 0
    j = 0
    nExiste = True
    print("1 - Maior")
    print("2 - Menor")
    print("3 - Igual")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemEntre()    
    if(opcao != 1 and opcao != 2 and opcao != 3):
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        porcentagemEntre()
    try:
        valor = int(input("Digite o valor: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        porcentagemEntre()    
    for i in tabela:
        if(i >= valor1 and i <= valor2):
            total += 1
    for i in range(0,len(tabelaNova3),1):
        if(valor >= valor1 and valor <= valor2):    
            if(valor == tabelaNova3[i]):
                for frequencia in tabelaNova1:
                    if(opcao == 1):               
                        if(((frequencia*100) / total) > ((tabelaNova1[j]*100)/total) and (tabelaNova3[j]>=valor1) and (tabelaNova3[j]<=valor2)):
                            print("Valor: %i"%tabelaNova3[k]) 
                            print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                            print("Frequência: %i\n"%frequencia)
                            nExiste = False
                        k+=1
                    elif(opcao == 2):                 
                        if(((frequencia*100) / total) < ((tabelaNova1[j]*100)/total) and (tabelaNova3[j]>=valor1) and (tabelaNova3[j]<=valor2)):
                            print("Valor: %i"%tabelaNova3[k]) 
                            print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                            print("Frequência: %i\n"%frequencia)
                            nExiste = False
                        k+=1
                    else:                 
                        if(((frequencia*100) / total) == ((tabelaNova1[j]*100)/total) and (k != i) and (tabelaNova3[j]>=valor1) and (tabelaNova3[j]<=valor2)):
                            print("Valor: %i"%tabelaNova3[k]) 
                            print("Porcentagem: %.2f porcento"%((frequencia*100)/total))
                            print("Frequência: %i\n"%frequencia)
                            nExiste = False
                        k+=1
            j += 1
    if(nExiste and opcao == 1):
        print("Não existe porcentagem maior que %.2f na tabela!"%valor)
    elif(nExiste and opcao == 2):
        print("Não existe porcentagem menor que %.2f na tabela!"%valor)
    elif(nExiste and opcao == 3):
        print("Não existe porcentagem igual a %.2f na tabela!"%valor)
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()    
    exibirMenuPrincipal()

def quartil(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Quartil###################")   
    print("1 - Primeiro Quarti")
    print("2 - Segundo Quartil")
    print("3 - Terceiro Quartil")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        quartil()
    if(opcao == 1):
        primeiroQuartil()
    if(opcao == 2):
        segundoQuartil()
    if(opcao == 3):
        terceiroQuartil()
    else:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        exibirMenuPrincipal()

def primeiroQuartil():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Quartil###################")
    rol(2)
    p = 0
    k = 0
    quartilTabela = []
    tamanho  = len(tabela) 
    if((tamanho%2) == 0):
        p = tamanho/2
    else:
        p = (tamanho+1)/2
    for i in tabela:
        if(k < p):
            quartilTabela.append(i)
        else:
            break
        k += 1
    print("Terceiro Quartil: %.2f"%mediana(2,quartilTabela)) 
    os.system("pause")  
    exibirMenuPrincipal()

def segundoQuartil():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Quartil###################")
    print("Segundo Quartil: %.2f"%mediana(2,tabela)) 
    os.system("pause")  
    exibirMenuPrincipal()

def terceiroQuartil():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Quartil###################")
    rol(2)
    p = 0
    k = 0
    comecou = False
    quartilTabela = []
    tamanho  = len(tabela) 
    if((tamanho%2) == 0):
        p = tamanho/2
    else:
        p = (tamanho+1)/2
    for i in tabela:
        if(p == k):
            comecou = True
            quartilTabela.append(i)
        elif(comecou):
            quartilTabela.append(i)
        k += 1
    print("Terceiro Quartil: %.2f"%mediana(2,quartilTabela)) 
    os.system("pause")  
    exibirMenuPrincipal()

def mediana(x1,x2):
    rol(2)
    if(x1==1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("###################Mediana###################")
    p1 = 0
    p2 = 0
    i = 0
    j = 0
    tamanho  = len(x2) 
    if((tamanho%2) == 0):
        p1 = (tamanho/2)-1 
        p2 = (tamanho/2)
        for i in x2:
            if(j == p1):
                valorQuartil = i
            if(j == p2):
                valorQuartil += i
                valorQuartil = valorQuartil/2
                break
            j += 1
    elif(tamanho!=1):
        p1 = (tamanho-1)/2
        for i in x2:
            if(j == p1):
                valorQuartil = i
                break
            j += 1
    else:
        valorQuartil = x2[0]
    if(x1==1):
        print("Mediana: %.2f"%valorQuartil) 
        os.system("pause")  
        exibirMenuPrincipal()
    else:
        return (valorQuartil)

def moda():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Moda###################")
    semiIntervaloClasses(2)
    moda = []
    j = 0
    maior = max(tabelaNova1)
    for i in range (len(tabelaNova1)):
        if((tabelaNova1[i]==maior) and (maior>1)):
            moda.append(tabelaNova3[i])
    if(len(moda) >= 3):
        print("Multimodal")
        for i in moda:
            print("%i"%i)
    elif(len(moda) == 2):
        print("Bimodal")
        for i in moda:
            print("%i"%i)
    elif(len(moda) == 1):
        print("%i"%moda[0])
    else:
        print("Amodal!")
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear()    
    exibirMenuPrincipal()

def decil():
    os.system('cls' if os.name == 'nt' else 'clear')
    rol(2)
    print("###################Dercil###################")
    print("1 - Primeiro Decil")
    print("2 - Segundo Decil")
    print("3 - Terceiro Decil")
    print("4 - Quarto Decil")
    print("5 - Quinto Decil")
    print("6 - Sexto Decil")
    print("7 - Setimo Decil")
    print("8 - Oitavo Decil")
    print("9 - Nono Decil")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        decil()
    os.system('cls' if os.name == 'nt' else 'clear')   
    valorDecil = (opcao/10)*(len(tabela))
    j = 1
    if(valorDecil%2==0):
        for i in tabela:
            if(j==valorDecil):
                print("Decil: %i"%i)
                break
            j += 1
    elif(len(tabela)%10==0):
        valorDecil = int(float(valorDecil))
        somaDecil = 0
        for i in tabela:
            if(j==valorDecil):
                print("Decil: %i"%i)
                break
            j += 1
    else:
        valorDecil = int(float(valorDecil))
        somaDecil = 0
        ok = False
        for i in tabela:
            if(j==valorDecil and ok==False):
                valorDecil += 1
                somaDecil = i
                ok = True
            if(j==valorDecil and ok):
                somaDecil += i
                somaDecil = somaDecil/2
                print("Decil: %.2f"%somaDecil)
                break
            j += 1       
    os.system("pause")  
    exibirMenuPrincipal()

def percentil():
    os.system('cls' if os.name == 'nt' else 'clear')
    semiIntervaloClasses(0)
    print("###################Percentil###################")
    print("1 - Percetil de 10 porcento")
    print("2 - Percetil de 90 porcento")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        percentil()
    os.system('cls' if os.name == 'nt' else 'clear')
    espaco = semiIntervaloClasses(3)
    if(opcao == 1):
        total = sum(tabelaNova2)
        l = tabela[0]
        fi = tabelaNova2[0]
        x = l + ((((opcao*10)*(total/100))*espaco)/fi)
        #x = l+fi+total
        print("Percil de 10 porcento: %i"%x)
    elif(opcao == 2):
        total = sum(tabelaNova2)
        l = ultimoIntervalo[1]
        fI = (round(((len(tabelaNova4))*90)/100))-1
        fI = tabelaNova4[fI]
        fi = (round(((len(tabelaNova4))*90)/100))-1
        fi = tabelaNova2[fi]
        x = l + ((((90*(total/100))-fI)*espaco)/fi)
        print("l = 9 = %i"%l)
        print("total/100 = 0,1 = %f"%(total/100))
        print("fI =  = %i"%fI)
        print("espaco = 2 = %i"%espaco)
        print("fi = 1 = %i"%fi)
        print("Percil de 90 porcento: %i"%x)
        for i in tabelaNova2:
            print("tabela2: %i"%i) 
    else:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        percentil()
    os.system("pause")
    tabelaNova1.clear()
    tabelaNova2.clear()
    tabelaNova3.clear() 
    tabelaNova4.clear() 
    ultimoIntervalo.clear() 
    exibirMenuPrincipal()

def variancia(x):
    if(x==2 or x==4):
        opcao = 1
    elif(x==3):
        opcao = 2
    elif(x==1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("###################Variancia###################")
        print("1 - População")
        print("2 - Amostra")
        try:
            opcao = int(input("Digite uma Opção: "))
        except Exception:
            print("Opção Invalida!")
            os.system("pause")
            variancia()
        os.system('cls' if os.name == 'nt' else 'clear')
    if(opcao == 1):
        populacao = 0
        media = sum(tabela)/len(tabela)
        for i in tabela:
            populacao += (i-media)**2
        populacao = populacao/len(tabela)
        if(x==1):
            print("População: %.2f"%populacao)
        elif(x==2):
            return (populacao ** 0.5)
        elif(x==4):
            return ((populacao/media)*100)
    elif(opcao == 2):
        amostraTabela.clear()
        print("Digite uma pequena Amostra da Tabela!");
        try:
            valor = float(input("Digite um Valor (0 - Finaliza): "))
        except Exception:
            print("Opção Invalida!")
            os.system("pause")
            variancia() 
        while (valor != 0):
            amostraTabela.append(valor) 
            try:
                valor = float(input("Digite um Valor (0 - Finaliza): "))
            except Exception:
                print("Opção Invalida!")
                os.system("pause")
                variancia()  
        amostra = 0
        media = sum(amostraTabela)/len(amostraTabela)
        for i in amostraTabela:
            amostra += (i-media)**2
        amostra = amostra/len(amostraTabela)
        if(x==1):
            print("Amostra: %.2f"%amostra)
        elif(x==3):
            return (amostra ** 0.5)
    else:
        print("Opção Invalida! Tente Novamente!")
        os.system("pause")
        variancia()
    os.system("pause")
    exibirMenuPrincipal()

def desvioPadrao(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Desvio Padrão###################")
    print("1 - População")
    print("2 - Amostra")
    try:
        opcao = int(input("Digite uma Opção: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        variancia()
    os.system('cls' if os.name == 'nt' else 'clear')
    if(opcao==1):
        print("Desvio Padrão de População: %.2f"%variancia(2))
    elif(opcao==2):
        print("Desvio Padrão de Amostra: %.2f"%variancia(3))
    os.system("pause")
    exibirMenuPrincipal()

def coeficienteDeVariacao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Coeficiente de variação.###################")
    print("O Coeficiente de variação é de %.2f porcento."%variancia(4))
    os.system("pause")
    exibirMenuPrincipal()

def erroPadrao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Erro Padrão###################")
    erroPadrao = (variancia(3)/((len(amostraTabela))**0.5))
    print("Erro padrão: %.2f porcento."%erroPadrao)
    os.system("pause")
    exibirMenuPrincipal()    

def distribuicaoBinomial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Distribuição Binomial.###################")
    try:
        quantTeste = int(input("Digite a quantidade de testes: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        distribuicaoBinomial()
    try:
        quantAlternativa = int(input("Digite quantas alternativas cada teste tem: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        distribuicaoBinomial()
    try:
        testesAcertados = int(input("Digite quantos testes deseja-se acertar para calcular a probabilidade: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        distribuicaoBinomial()
    calculo1 = 1
    calculo2 = 1
    for i in range(quantTeste,testesAcertados,-1):
        calculo1 = calculo1 * i
    for i in range(quantTeste-testesAcertados,1,-1):
        calculo2 = calculo2 * i
    calculo1 = calculo1/calculo2
    quantAlternativa = 1/quantAlternativa
    calculo1 = (calculo1*(quantAlternativa**testesAcertados)*((1-quantAlternativa)**(quantTeste-testesAcertados)))*100
    print("probabilidade vai ser: %.4f porcento!"%calculo1)
    os.system("pause")
    exibirMenuPrincipal()    

def distribuicaoPoisson():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################Distribuição Poisson.###################")
    print("Exemplo: ")
    print("Supondo que a media de pessoas que adquirem seguro em um banco é de x/hora,\n" 
          "calcule qual a probabilidade em uma determinada hora serem vendidos y seguros.")
    try:
        quantVendidos = int(input("Digite a quantidade de seguros vendidos: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        distribuicaoPoisson()
    try:
        media = float(input("Digite a media(em horas) de seguros vendidos: "))
    except Exception:
        print("Opção Invalida!")
        os.system("pause")
        distribuicaoPoisson()
    e = 2.71828
    fatorial = 1
    for i in range(quantVendidos,1,-1):
        fatorial = fatorial * i
    calculo = ((e**(-media))*(media**quantVendidos))/fatorial
    print("Distribuição de Poisson é %.2f porcento"%(calculo*100))
    os.system("pause")
    exibirMenuPrincipal()
exibirMenuPrincipal()