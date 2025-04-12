import random
from random import randint


def get_dados():
    arquivo_investidor = open("investidor.txt", "r")
    linhas_investidor = arquivo_investidor.readlines()
    cadastro = int(linhas_investidor[0])
    senha = str(linhas_investidor[1])
    nome = str(linhas_investidor[2])
    cpf = str(linhas_investidor[3])
    return cadastro, senha, nome, cpf

def login():
    # arquivo_investidor = open("investidor.txt", "r")
    # linhas_investidor = arquivo_investidor.readlines()
    # cadastro = int(linhas_investidor[0])
    # senha = str(linhas_investidor[1])
    # nome = str(linhas_investidor[2])
    cadastro, senha, nome, cpf = get_dados()
    
    while True:
        #cpf = str(linhas_investidor[3])
        login_cadastro = int(input("CPF(sem traços ou pontos): "))
        login_senha = input("Senha: ")
        if login_senha == senha and login_cadastro == cadastro:
            print("\nlogado!\nboas vindas {}".format(nome))
            break
        else:
            print("usuario n encontrado")

def tentativa_senha():
    senha = get_dados()
    # arquivo_investidor = open("investidor.txt", "r")
    # linhas_investidor = arquivo_investidor.readlines()
    # cadastro = int(linhas_investidor[0])
    # arquivo_senha = str(linhas_investidor[1])
    while True:
        senha_tentativa = int(input("senha: "))
        if senha_tentativa == senha:
            print("senha correta")
            break
        else:
            print("errado")
def saldo():
    print("para consultar o saldo, informe sua senha: ")
    tentativa_senha()
    #printar dados usuario
    #get_dados()
    arquivo_saldo = open("saldo_atual.txt", "r")
    saldo_linhas = arquivo_saldo.readlines()
    real = float(saldo_linhas[0])
    btc = float(saldo_linhas[1])
    eth = float(saldo_linhas[2])
    xrp = float(saldo_linhas[3])
    arquivo_saldo.close()
    
    nomes_cripto = ["real", "btc", "eth", "xrp"]
    valores_cripto = [real, btc, eth, xrp]
    for i in range(4):
        print(nomes_cripto[i], valores_cripto[i])
    return real, btc, eth, xrp 

def nova_linha_extrato(real, btc, eth, xrp):
    arquivo_extrato = open("extrato.txt", "a")
    arquivo_extrato.write(real, btc, eth, xrp)
    arquivo_extrato.close()

def overwrite_saldo(real, btc, eth, xrp, cotacao):
    arquivo_saldo = open("saldo_atual.txt", "w")
    arquivo_saldo.write("%s\n%s\n%s\n%s\n" % (float(real, btc, eth, xrp)))

def depositar():
    real, btc, eth, xrp = saldo()
    # try:
    
    real = float(real)
    valor_deposito = float(input("valor deposito: "))
    # except
    
    #horario, escrever extrato, somar e escrever no saldo.txt

    real += valor_deposito
    cotacao = 0
    overwrite_saldo(real, btc, eth, xrp)
    nova_linha_extrato(real, btc, eth, xrp, cotacao)

def sacar():
    real, btc, eth, xrp = saldo()
    real = float(real)
    valor_saque = float(input("valor saque: "))
    real += valor_saque
    cotacao = 0
    overwrite_saldo(real, btc, eth, xrp)
    nova_linha_extrato(real, btc, eth, xrp, cotacao)

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

##switch case?
while True:
    acao = int(input(""))
    if acao == 1:
        saldo()
        menu()
    if acao == 7:
        atualizar_cotacao()