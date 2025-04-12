import random
from random import randint
import sys

def get_dados():
    arquivo_investidor = open("investidor.txt", "r")
    linhas_investidor = arquivo_investidor.readlines()
    cadastro = int(linhas_investidor[0])
    senha = int(linhas_investidor[1])
    nome = str(linhas_investidor[2])
    cpf = str(linhas_investidor[3])
    return cadastro, senha, nome, cpf

def login():
    cadastro, senha, nome, cpf = get_dados()
    
    while True:
        login_cadastro = int(input("CPF (sem traços ou pontos): "))
        login_senha = tentativa_senha()
        
        # login_senha = int(input("Senha: "))
        if login_senha == senha and login_cadastro == cadastro:
            print("\nUsuário encontrado!\nBoas vindas {}CPF: {}".format(nome.capitalize(), cpf))
            menu()
            break
        else:
            print("Usuário não encontrado!")

def tentativa_senha():
    cadastro, senha, nome, cpf = get_dados()
    while True:
        senha_tentativa = int(input("Senha: "))
        if senha_tentativa == int(senha):
            # print("Senha correta!")
            return senha_tentativa
        else:
            print("Senha incorreta.")

def saldo():
    print("Para consultar o saldo atual, informe sua senha.")
    tentativa_senha()

    cadastro, senha, nome, cpf = get_dados()
    print("\n{}CPF: {}\n".format(nome.capitalize(), cpf))
            
    arquivo_saldo = open("saldo_atual.txt", "r")
    saldo_linhas = arquivo_saldo.readlines()
    real = float(saldo_linhas[0])
    btc = float(saldo_linhas[1])
    eth = float(saldo_linhas[2])
    xrp = float(saldo_linhas[3])
    arquivo_saldo.close()
    
    nomes_cripto = ["Reais", "Bitcoin", "Ethereum", "Ripple"]
    valores_cripto = [real, btc, eth, xrp]
    siglas_cripto = ["R$", "BTC", "ETH", "XRP"]

    for i in range(4):
        print(nomes_cripto[i], valores_cripto[i], siglas_cripto[i])
    return real, btc, eth, xrp 

def nova_linha_extrato(tipo, valor, cotacao, real, btc, eth, xrp):
    arquivo_extrato = open("extrato.txt", "a")
    print("%s + %6f CT: %9f TX: 0.00 REAL: %7f BTC: %10f ETH: %9f XRP: %7f\n" % (tipo, valor, cotacao, real, btc, eth, xrp)) 
    arquivo_extrato.write("%s + %6f CT: %9f TX: 0.00 REAL: %7f BTC: %10f ETH: %9f XRP: %7f\n" % (tipo, valor, cotacao, real, btc, eth, xrp)) 
    arquivo_extrato.close()

def overwrite_saldo(real, btc, eth, xrp):
    arquivo_saldo = open("saldo_atual.txt", "w")
    arquivo_saldo.write("%s\n%s\n%s\n%s\n" % (real, btc, eth, xrp))

def extrato():
    arquivo_extrato = open("extrato.txt", "r")
    extrato_linhas = arquivo_extrato.readlines()
    if len(extrato_linhas) == 0:
        print("Nenhum extrato efetuado.")
    else:
        for linha in extrato_linhas:
            print(linha.strip())

def depositar():
    real, btc, eth, xrp = saldo()
    # try:
    
    float(real)
    valor = float(input("\nValor do depósito: "))
    
    # except
    #horario, escrever extrato, somar e escrever no saldo.txt

    real += valor
    cotacao = 0
    tipo = "REAL"

    overwrite_saldo(real, btc, eth, xrp)
    nova_linha_extrato(tipo, valor, cotacao, real, btc, eth, xrp)
    

def sacar():
    real, btc, eth, xrp = saldo()
    real = float(real)
    valor = float(input("valor saque: "))
    real += valor
    tipo = "REAL"
    cotacao = 0
    overwrite_saldo(real, btc, eth, xrp)
    # nova_linha_extrato(real, btc, eth, xrp, cotacao)
    nova_linha_extrato(tipo, valor, cotacao, real, btc, eth, xrp)


def cotacao_atual():
    arquivo_cotacao = open("cotacao.txt", "r")
    cotacao_linhas = arquivo_cotacao.readlines()
    ct_bitcoin = cotacao_linhas[0]
    ct_ethereum = cotacao_linhas[1]
    ct_ripple = cotacao_linhas[2]
    print("cotacao atual :")
    print("bitcoin: %s", ct_bitcoin)
    print("ethereum: %s", ct_ethereum)
    print("ripple: %s", ct_ripple)
    return ct_bitcoin, ct_ethereum, ct_ripple

def comprar_criptomoedas():
    cotacao_atual()

def vender_criptomoedas():
    cotacao_atual()

def atualizar_cotacao():
    ct_btc, ct_eth, ct_xrp = cotacao_atual()
    ct_original_xrp = 2.64
    ct_original_btc = 347815.6
    ct_original_eth = 19387.17
    cotacoes_originais = [347815.6, 19387.17, 2.64]
    novas_cotacoes = [0,0,0]
    digito = int(input("Digite 1 para aualizar as cotações atuais. Digite 0 para sair."))
    
    random_aumento_ou_diminuicao = [0, 0, 0]
    
    if digito == 1:

        #random se vai aumentar a cotacao original ou diminuir (1 a 5%)

        for i in range(3):
            x = randint(1,2) # 1 aumenta, 2 diminui
            random_aumento_ou_diminuicao[i] = x
        
        for j in range(3):
            y = randint(1,5) # porcentagem de 1 a 5%
            if random_aumento_ou_diminuicao[i] == 1:
                att = cotacoes_originais[i] * y/100
            
            print(cotacoes_originais[i])
            print(y)
            print(y/100)

            novas_cotacoes[i] = att
            print(novas_cotacoes[i])


def menu():
    opcoes = [
"\n----------------------",
" 1. Consultar saldo",
" 2. Consultar extrato",
" 3. Depositar",
" 4. Sacar",
" 5. Comprar criptomoedas",
" 6. Vender criptomoedas",
" 7. Atualizar cotação",
" 8. Sair",
"------------------------\n",
]
    for chave in opcoes:
        print(chave)


# def mensagem():
#     print("\nVocê retornou ao menu.")


login()
##switch case?
while True:
    acao = int(input(""))
    if acao == 1:
        # print("Saldo")
        saldo()
    elif acao == 2:
        # print("Consultar extrato")
        extrato()
    elif acao == 3:
        # print("Realizar depósito")
        depositar()
    elif acao == 4:
        # print("Realizar saque")
        sacar()
    elif acao == 5:
        # print("Comprar criptomoedas")
        comprar_criptomoedas()
    elif acao == 6:
        # print("Vender criptomoedas")
        vender_criptomoedas()
    elif acao == 7:
        # print("Atualizar cotações")
        atualizar_cotacao()
    elif acao == 8:
        print("Programa finalizado.")
        sys.exit()
    elif acao == 0:
        menu()
    else:
        print("Dígito inválido")
    menu()
    # mensagem()