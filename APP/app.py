import os, sys
from colaborador import Colaborador
from caminhao import Caminhao
from moto import Moto
from carro import Carro

def menu(nome_menu, *opcoes):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"+{'-'*30}+\n|{nome_menu:^30}|\n+{'-'*30}+")
    for opcao in opcoes:
        print(f"|{opcao:<30}|\n+{'-'*30}+")
    try:
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    except:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu(nome_menu, *opcoes)

def menu_principal():
    op = menu("Menu Principal", "1. Colaborador", "2. Veículo", "3. Sair")
    if op == 1:
        menu_colaborador()
    elif op == 2:
        menu_veiculo()
    elif op == 3:
        exit()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_principal()

def menu_colaborador():
    op = menu("Menu Colaborador", "1. Cadastrar", "2. Voltar")
    if op == 1:
        colaborador = Colaborador()
        colaborador.adicionar_colaborador()
        colaborador.apresentar_colaborador()
        input("Pressione ENTER para continuar...")
        menu_colaborador()
    elif op == 2:
        menu_principal()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_colaborador()

def menu_veiculo():
    op = menu("Menu Veículo", "1. Cadastrar", "2. Alocar","3. Devolver", "4. Voltar")
    if op == 1:
        op = menu("Menu Veículo", "1. Carro", "2. Moto", "3. Caminhão", "4. Voltar")
        if op == 1:
            veiculo = Carro()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 2:
            veiculo = Moto()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 3:
            veiculo = Caminhao()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 4:
            menu_veiculo()  
        else:
            print("Opção inválida!")
            input("Você precisa digitar um número. Pressione ENTER para continuar...")
            menu_veiculo()
    elif op == 2:
        print("Alocar")
    elif op == 3:
        print("Devolver")
    elif op == 4:
        menu_principal()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_veiculo()

menu_principal()