import datetime
import datetime as dt
from datetime import datetime
import random
from random import randint

#dicionário contendo dados do investidor
cpf = { "cadastro_cpf" : 1, #12345678900
       "Senha" : 1, #123456
       "Nome" : "Ravi",
       "CPF" : "123.456.789-00",
}
keys_cpf = cpf.keys()
keys_cpf = list(keys_cpf)




#obter horário atual
def horario():
    horario_extrato = dt.datetime.now()
    horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
    print(horario_extrato_convertido)

def menu():
    opcoes = [
" --------- MENU ---------",
" 1. Consultar saldo",
" 2. Consultar extrato",
" 3. Depositar",
" 4. Sacar",
" 5. Comprar criptomoedas",
" 6. Vender criptomoedas",
" 7. Atualizar cotação",
" 8. Sair",
" ------------------------ ",
]
    for chave in opcoes:
        print(chave)

def login():
    horario()
    print("Exchange de Criptomoedas")
    while True:
        login_cpf = int(input("Digite seu CPF (sem traços ou pontos): "))
        login_senha = int(input("Digite sua senha (6 dígitos): "))
        if login_cpf == cpf["cadastro_cpf"] and login_senha == cpf["Senha"]:
                print("")
                print("Login efetuado com sucesso.")
                print("Bem-vindo {}.".format(cpf["Nome"]))
                menu()
                break
        else:
                print("Login inválido")

login()

def tentativa_senha():
    tentativas = 3
    while True:
        saldo_senha = int(input("Digite sua senha: "))
        if saldo_senha == cpf["Senha"]:
            break
        else:
            if tentativas > 1:
                print("Senha inválida. Você possui {} tentativas restantes.".format(tentativas))
                tentativas -= 1
            elif tentativas == 1:
                print("Senha inválida. Você possui {} tentativa restante.".format(tentativas))
                tentativas -= 1
            else:
                print("Programa finalizado pelo limite de tentativas excedidas.")
                quit()

def saldo():
    print("Para consultar o saldo atual, informe sua senha.")
    tentativa_senha()

    print("")
    for n in range(2,4): #printa nome e cpf
        print("{}: {}".format(keys_cpf[n], cpf[keys_cpf[n]]))
    
    arquivo_saldo = open("saldo_atual.txt", "r")
    saldo_linhas = arquivo_saldo.readlines() #printa as 4 linhas do arquivo "saldo_atual.txt", que possui: {reais, btc, eth, xrp}
    print("Reais: {:.2f}".format(float(saldo_linhas[0])))
    print("Bitcoin: {:.8f}".format(float(saldo_linhas[1])))
    print("Ethereum: {:.7f}".format(float(saldo_linhas[2])))
    print("Ripple: {:.4f}".format(float(saldo_linhas[3])))
    arquivo_saldo.close()

def extrato():
    print("Para consultar o extrato, informe sua senha.")
    tentativa_senha()
    print("")
    print("Extrato:")
    arquivo_extrato = open("extrato.txt", "r")
    linhas = arquivo_extrato.readlines()
    if len(linhas) == 0:
        print("Nenhum extrato efetuado.")
    else:
        for linha in linhas:
            print(linha.strip())

def depositar():
    while True:
        # confere os valores antes do deposito
        arquivo_saldo = open("saldo_atual.txt", "r")
        saldo_linhas = arquivo_saldo.readlines()
        reais = float(saldo_linhas[0])
        bitcoin = float(saldo_linhas[1])
        ethereum = float(saldo_linhas[2])
        ripple = float(saldo_linhas[3])
        arquivo_saldo.close()

        valor_deposito = float(input("Valor do depósito: "))

        if valor_deposito < 0:
            print("Digite um valor válido. Caso queira cancelar, digite '0'.")
        elif valor_deposito == 0:
            print("Depósito cancelado.")
            break
        else:
            # adiciona o deposito aos reais & escreve os valores não alterados de volta 
            reais_atualizado = float(valor_deposito) + float(reais)

            ##horario do extrato
            horario_extrato = dt.datetime.now()
            horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
            print(horario_extrato_convertido)

            arquivo_saldo = open("saldo_atual.txt", "w")
            arquivo_saldo.write("%s\n%s\n%s\n%s" % (float(reais_atualizado), float(bitcoin), float(ethereum), float(ripple)))
            arquivo_saldo.close()

            #registrar o deposito no extrato.txt
            cotacao = "0.0"
            arquivo_extrato = open("extrato.txt", "a")
            arquivo_extrato.write("%s + %6f CT: %9f TX: 0.00 REAL: %7f BTC: %10f ETH: %9f XRP: %7f\n" % (horario_extrato_convertido, float(valor_deposito), float(cotacao), 
                                                                                                        float(reais_atualizado), float(bitcoin), float(ethereum), float(ripple)))
            arquivo_extrato.close()

            print("Depósito de {} REAL adicionado à conta.".format(valor_deposito))
            saldo()
            break

def sacar():
    print("Para sacar, informe sua senha.")
    tentativa_senha()
    while True:
        arquivo_saldo = open("saldo_atual.txt", "r")
        saldo_linhas = arquivo_saldo.readlines()
        reais = float(saldo_linhas[0])
        bitcoin = float(saldo_linhas[1])
        ethereum = float(saldo_linhas[2])
        ripple = float(saldo_linhas[3])
        arquivo_saldo.close()

        valor_saque = float(input("Valor do saque: "))

        if float(valor_saque) > float(reais):
            print("O saldo total deve permanecer positivo. Digite '0' para voltar ao menu ou insira um valor adequado.")
        elif valor_saque == 0:
            print("Saque cancelado.")
            break
        else:
            reais_atualizado = reais - valor_saque

            horario_extrato = dt.datetime.now()
            horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
            print(horario_extrato_convertido)
            
            #atualiza o saldo_atual.txt
            arquivo_saldo = open("saldo_atual.txt", "w")
            arquivo_saldo.write(str("%s\n" % (reais_atualizado)))
            arquivo_saldo.write(str("%s\n" % (bitcoin)))
            arquivo_saldo.write(str("%s\n" % (ethereum)))
            arquivo_saldo.write(str("%s\n" % (ripple)))
            arquivo_saldo.close()

            tipo = "REAL"
            cotacao = "0.0"
            taxa = "0.00"
            #registra o saque no extrato.txt
            arquivo_extrato = open("extrato.txt", "a")
            arquivo_extrato.write("%s - %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_saque),
                                                 tipo,str(cotacao), str(taxa), str(reais_atualizado), str(bitcoin), str(ethereum), str(ripple)))
            arquivo_extrato.close()

            print("Saque de {} REAL removido da conta.".format(valor_saque))
            saldo()
            break

#acao = 5
def comprar_criptomoedas():   
    print("Para comprar criptomoedas, insira sua senha.")
    tentativa_senha()

    print("")
    #printar cotacoes moedas
    print("Cotações atuais:")
    arquivo_cotacao = open("cotacao.txt", "r")
    cotacao_linhas = arquivo_cotacao.readlines()
    cotacao_bitcoin = float(cotacao_linhas[0])
    cotacao_ethereum = float(cotacao_linhas[1])
    cotacao_ripple = float(cotacao_linhas[2])
    print ("BTC: {}".format(float(cotacao_bitcoin)))
    print ("ETH: {}".format(float(cotacao_ethereum)))
    print ("XRP: {}".format(float(cotacao_ripple)))
    print("")

    arquivo_saldo = open("saldo_atual.txt", "r")
    saldo_linhas = arquivo_saldo.readlines()
    reais = float(saldo_linhas[0])
    bitcoin = float(saldo_linhas[1])
    ethereum = float(saldo_linhas[2])
    ripple = float(saldo_linhas[3])
    
    lista_criptomoedas = ["1. Bitcoin (BTC) - taxa de compra: 2%", "2. Ethereum (ETH) - taxa de compra: 1%", "3. Ripple (XRP) - taxa de compra: 1%"]
    for criptomoedas in lista_criptomoedas:
        print(criptomoedas)
    while True:

        escolha_criptomoeda = int(input("Dígito da criptomoeda desejada: "))
        if escolha_criptomoeda == 1:
            print("")
            print("Bitcoin selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_deposito = float(input("Digite o valor em reais da criptomoeda desejada: "))
        
            if valor_deposito == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_deposito < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif (float(valor_deposito) + (valor_deposito)*2/100) > float(reais):
                taxa_compra = 2/100
                saldo_atual = reais

                print("Valor compra + taxa (2%): {:.2f} reais".format(float(valor_deposito) + (valor_deposito * taxa_compra)))
                print("Saldo atual: {:.2f} reais".format(saldo_atual))
                print("Saldo insuficiente.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()


                #subtrai os reais equivalentes ao btc + taxa(2% na compra).
                reais -= valor_deposito
                taxa = (valor_deposito)*2/100
                reais -= taxa

                bitcoin = valor_deposito/cotacao_bitcoin + bitcoin
                bitcoin = "{:.8f}".format(bitcoin)
                print("{:.8f} BTC comprado com sucesso.".format(valor_deposito/cotacao_bitcoin))

                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))

                # adiciona a compra ao extrato.txt
                tipo = "BTC"
                taxa_bitcoin = "0.02"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s + %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_deposito),
                tipo, str(cotacao_bitcoin), str(taxa_bitcoin), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break
        elif escolha_criptomoeda == 2:
            print("")
            print("Ethereum selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_deposito = float(input("Digite o valor em reais da criptomoeda desejada: "))
        
            if valor_deposito == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_deposito < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif (float(valor_deposito) + (valor_deposito)*1/100) > float(reais):
                taxa_compra = 1/100
                saldo_atual = reais

                print("Valor compra + taxa (1%): {:.2f} reais".format(float(valor_deposito) + (valor_deposito * taxa_compra)))
                print("Saldo atual: {:.2f} reais".format(saldo_atual))
                print("Saldo insuficiente.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()

                #somar reais equivalentes e subtrair taxa.
                reais -= valor_deposito
                taxa = (valor_deposito)*1/100
                reais -= taxa

                #adiciona no .txt a criptomoeda
                ethereum_atualizado = valor_deposito/cotacao_ethereum + ethereum
                ethereum = "{:.7f}".format(ethereum_atualizado)
                print("{:.7f} ETH comprado com sucesso.".format(valor_deposito/cotacao_ethereum))

                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))

                # adiciona a compra ao extrato.txt
                tipo = "ETH"
                taxa_ethereum = "0.01"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s + %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_deposito),
                tipo, str(cotacao_ethereum), str(taxa_ethereum), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break
        elif escolha_criptomoeda == 3:
            print("")
            print("Ripple selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_deposito = float(input("Digite o valor em reais da criptomoeda desejada: "))
        
            if valor_deposito == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_deposito < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif (float(valor_deposito) + (valor_deposito)*1/100) > float(reais):
                taxa_compra = 1/100
                saldo_atual = reais

                print("Valor compra + taxa (1%): {:.2f} reais".format(float(valor_deposito) + (valor_deposito * taxa_compra)))
                print("Saldo atual: {:.2f} reais".format(saldo_atual))
                print("Saldo insuficiente.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()


                #subtrai reais equivalentes e subtrair taxa.
                reais -= valor_deposito
                taxa = (valor_deposito)*1/100
                reais -= taxa

                #adiciona no .txt a criptomoeda
                ripple = valor_deposito/cotacao_ripple + ripple
                ripple = "{:.4f}".format(ripple)
                print("{:.4f} XRP comprado com sucesso.".format(valor_deposito/cotacao_ripple))
                
                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))

                # adiciona a compra ao extrato.txt
                tipo = "XRP"
                taxa_ripple = "0.01"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s + %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_deposito),
                tipo, str(cotacao_ripple), str(taxa_ripple), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break
#acao = 6
def vender_criptomoedas():  
    print("Para vender criptomoedas, insira sua senha.")
    tentativa_senha()

    #printar cotacoes moedas
    print("Cotações atuais:")
    arquivo_cotacao = open("cotacao.txt", "r")
    cotacao_linhas = arquivo_cotacao.readlines()
    cotacao_bitcoin = float(cotacao_linhas[0])
    cotacao_ethereum = float(cotacao_linhas[1])
    cotacao_ripple = float(cotacao_linhas[2])
    print ("BTC: {}".format(float(cotacao_bitcoin)))
    print ("ETH: {}".format(float(cotacao_ethereum)))
    print ("XRP: {}".format(float(cotacao_ripple)))
    print("")

    arquivo_saldo = open("saldo_atual.txt", "r")
    saldo_linhas = arquivo_saldo.readlines()
    reais = float(saldo_linhas[0])
    bitcoin = float(saldo_linhas[1])
    ethereum = float(saldo_linhas[2])
    ripple = float(saldo_linhas[3])
    
    #escolher criptomoeda
    lista_criptomoedas = ["1. Bitcoin (BTC) - taxa de venda: 3%", "2. Ethereum (ETH) - taxa de venda: 2%", "3. Ripple (XRP) - taxa de venda: 1%"]
    for criptomoedas in lista_criptomoedas:
        print(criptomoedas)
    while True:

        escolha_criptomoeda = int(input("Dígito da criptomoeda desejada: "))
        if escolha_criptomoeda == 1:
            print("")
            print("Bitcoin selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_venda = float(input("Digite o valor em reais da criptomoeda para venda: "))
      
            if valor_venda == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_venda < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif valor_venda/cotacao_bitcoin > bitcoin:
                taxa_venda = 3/100

                print("Valor inserido + taxa: {:.2f} reais".format(float(valor_venda) + (valor_venda*taxa_venda)))
                print("Saldo atual de BTC convertido: {:.2f} reais".format(bitcoin*cotacao_bitcoin))
                print("O valor inserido é maior do que o saldo disponível.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                ##horario de extrato
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()

                #subtrai no .txt a criptomoeda
                venda_bitcoin = "{:.8f}".format(valor_venda/cotacao_bitcoin)
                bitcoin = bitcoin - float(venda_bitcoin)
                print("{:.8f} BTC vendido com sucesso.".format(valor_venda/cotacao_bitcoin))

                #somar reais equivalentes e subtrair taxa.
                reais += valor_venda
                taxa = (valor_venda)*3/100
                reais -= taxa
                reais = "{:.2f}".format(reais)
                print("{:.2f} REAL adicionado à conta.".format(valor_venda))

                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))

                # adiciona a venda ao extrato.txt
                tipo = "BTC"
                taxa_bitcoin = "0.03"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s - %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_venda),
                tipo, str(cotacao_bitcoin), str(taxa_bitcoin), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break
        elif escolha_criptomoeda == 2:
            print("")
            print("Ethereum selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_venda = float(input("Digite o valor em reais da criptomoeda para venda: "))
      
            if valor_venda == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_venda < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif valor_venda/cotacao_ethereum > ethereum:
                taxa_venda = 2/100

                print("Valor inserido + taxa: {:.2f} reais".format(float(valor_venda) + (valor_venda*taxa_venda)))
                print("Saldo atual de ETH convertido: {:.2f} reais".format(ethereum*cotacao_ethereum))
                print("O valor inserido é maior do que o saldo disponível.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                ##horario de extrato
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()

                #subtrai no .txt o eth a criptomoeda
                venda_ethereum = "{:.7f}".format(valor_venda/cotacao_ethereum)
                ethereum = ethereum - float(venda_ethereum)
                print("{:.7f} ETH vendido com sucesso.".format(valor_venda/cotacao_ethereum))

                #somar reais equivalentes e subtrair taxa.
                reais += valor_venda
                taxa = (valor_venda)*2/100
                reais -= taxa
                reais = "{:.2f}".format(reais)
                print("{:.2f} REAL adicionado à conta.".format(valor_venda))


                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))

                # adiciona a venda ao extrato.txt
                tipo = "ETH"
                taxa_ethereum = "0.02"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s - %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_venda),
                tipo, str(cotacao_ethereum), str(taxa_ethereum), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break
        elif escolha_criptomoeda == 3:
            print("")
            print("Ripple selecionado.")
            print("Caso deseje cancelar a operação, digite '0'")
            valor_venda = float(input("Digite o valor em reais da criptomoeda para venda: "))
      
            if valor_venda == 0:
                arquivo_saldo.close()
                arquivo_cotacao.close()
                print("Operação cancelada.")
                break
            elif valor_venda < 0:
                print("Por favor, digite um valor válido. Caso deseje cancelar a operação, digite '0'")
            elif valor_venda/cotacao_ripple > ripple:
                taxa_venda = 1/100

                print("Valor inserido + taxa: {:.2f} reais".format(float(valor_venda) + (valor_venda*taxa_venda)))
                print("Saldo atual de XRP convertido: {:.2f} reais".format(ripple*cotacao_ripple))
                print("O valor inserido é maior do que o saldo disponível.")

                arquivo_cotacao.close()
                arquivo_saldo.close()
                break
            else:
                ##horario de extrato
                horario_extrato = dt.datetime.now()
                horario_extrato_convertido = horario_extrato.strftime("%d-%m-%Y %H:%M")
                print(horario_extrato_convertido)

                arquivo_saldo = open("saldo_atual.txt", "r")
                saldo_linhas = arquivo_saldo.readlines()
                reais = float(saldo_linhas[0])
                bitcoin = float(saldo_linhas[1])
                ethereum = float(saldo_linhas[2])
                ripple = float(saldo_linhas[3])
                arquivo_saldo.close()

                #subtrai no .txt a criptomoeda
                venda_ripple = "{:.4f}".format(valor_venda/cotacao_ripple)
                ripple = ripple - float(venda_ripple)
                print("{:.4f} XRP vendido com sucesso.".format(valor_venda/cotacao_ripple))

                #somar reais equivalentes e subtrair taxa.
                reais += valor_venda
                taxa = (valor_venda)*1/100
                reais -= taxa
                reais = "{:.2f}".format(reais)
                print("{:.2f} REAL adicionado à conta.".format(valor_venda))


                # atualiza os valores no saldo_atual.txt
                arquivo_saldo = open("saldo_atual.txt", "w")
                arquivo_saldo.write(str("%s\n" % (reais)))
                arquivo_saldo.write(str("%s\n" % (bitcoin)))
                arquivo_saldo.write(str("%s\n" % (ethereum)))
                arquivo_saldo.write(str("%s\n" % (ripple)))
                # adiciona a venda ao extrato.txt
                tipo = "XRP"
                taxa_ripple = "0.01"
                arquivo_extrato = open("extrato.txt","a")
                arquivo_extrato.write("%s - %6s %4s CT: %9s TX: %3s REAL: %7s BTC: %10s ETH: %9s XRP: %7s\n" % (horario_extrato_convertido, str(valor_venda),
                tipo, str(cotacao_ripple), str(taxa_ripple), str(reais), str(bitcoin), str(ethereum), str(ripple)))
            
                arquivo_extrato.close()
                arquivo_saldo.close()
                arquivo_cotacao.close()
                break


#acao = 7
def atualizar_cotacao():   
    print("Atualizar cotação")
    #printar cotacoes moedas
    print("Cotações atuais:")
    arquivo_cotacao = open("cotacao.txt", "r")
    cotacao_linhas = arquivo_cotacao.readlines()
    cotacao_bitcoin = float(cotacao_linhas[0])
    cotacao_ethereum = float(cotacao_linhas[1])
    cotacao_ripple = float(cotacao_linhas[2])
    print ("BTC: {}".format(float(cotacao_bitcoin)))
    print ("ETH: {}".format(float(cotacao_ethereum)))
    print ("XRP: {}".format(float(cotacao_ripple)))
    print("")
    while True:
        cotacao_original_ripple = 2.64
        cotacao_original_bitcoin = 347815.60
        cotacao_original_ethereum = 19387.17

        print("Digite '1' para atualizar as cotações atuais. Digite '0' para sair.")
        digito = int(input(""))
        
        if digito == 1:

            #bitcoin
            valor_atualizacao_bitcoin = cotacao_original_bitcoin * randint(1,5)/100
            sorteio_bitcoin = randint(1,2)
            if sorteio_bitcoin == 1:
                cotacao_bitcoin_atualizada = cotacao_original_bitcoin + valor_atualizacao_bitcoin
            elif sorteio_bitcoin == 2:
                cotacao_bitcoin_atualizada = cotacao_original_bitcoin - valor_atualizacao_bitcoin
            print("BTC: {:.2f}".format(cotacao_bitcoin_atualizada))

            #ethereum
            valor_atualizacao_ethereum = cotacao_original_ethereum * randint(1,5)/100
            sorteio_ethereum = randint(1,2)
            if sorteio_ethereum == 1:
                cotacao_ethereum_atualizada = cotacao_original_ethereum + valor_atualizacao_ethereum
            elif sorteio_ethereum == 2:
                cotacao_ethereum_atualizada = cotacao_original_ethereum - valor_atualizacao_ethereum
            print("ETH: {:.2f}".format(cotacao_ethereum_atualizada))

            ##ripple
            ##gera o valor que ira diminuir/aumentar a cotacao original do ripple(2.64)
            valor_atualizacao_ripple = cotacao_original_ripple * randint(1,5)/100
            # print(valor_atualizacao_ripple)
            ## sorteia entre 1 e 2 se a cotacao irá aumentar ou diminuir. 1 aumenta a cotacao, 2 diminui a cotacao.
            sorteio_ripple = randint(1,2)
            if sorteio_ripple == 1:
                cotacao_ripple_atualizada = cotacao_original_ripple + valor_atualizacao_ripple
            elif sorteio_ripple == 2:
                cotacao_ripple_atualizada = cotacao_original_ripple - valor_atualizacao_ripple
            print("XRP: {:.2f}".format(cotacao_ripple_atualizada))

            #mantem as cotacoes no arquivo cotacao.txt para serem as mesmas na compra/venda de criptomoedas
            arquivo_cotacao = open("cotacao.txt", "w")
            arquivo_cotacao.write("%.2f\n" % (float(cotacao_bitcoin_atualizada)))
            arquivo_cotacao.write("%.2f\n" % (float(cotacao_ethereum_atualizada)))
            arquivo_cotacao.write("%.2f\n" % (float(cotacao_ripple_atualizada)))
            arquivo_cotacao.close()

        elif digito == 0:
            break
        else:
            print("Insira um dígito válido.")

#acao = 8
def sair():
    print("Operação finalizada.")
    quit()

#aparece no final de cada acao.
def mensagem():
    print("")
    print("Você retornou ao menu.")
    print("Digite '0' para conferir as opções do menu novamente. Digite '8' para finalizar a operação.")

#enquanto o programa nao for finalizado com "8", vai rodar isso:
while True:
    acao = int(input(""))
    if acao == 1:
        saldo()
        mensagem()
    elif acao == 2:
        extrato()
        mensagem()
    elif acao == 3:
        depositar()
        mensagem()
    elif acao == 4:
        sacar()
        mensagem()
    elif acao == 5:
        comprar_criptomoedas()
        mensagem()
    elif acao == 6:
        vender_criptomoedas()
        mensagem()
    elif acao == 7:
        atualizar_cotacao()
        mensagem()
    elif acao == 8:
        sair()
    elif acao == 0:
        menu()
    else:
        print("Digite uma operação válida.")