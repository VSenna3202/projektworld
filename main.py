'''
 ============================================================================
 Name        : WorldProjekt
 Author      : VSenna, Kl3t1n, GuiRibeiro
 Version     : Indev 1
 Copyright   : Arranjarás para a cabeça.
 Description : Console Rpg                 
 ============================================================================
 '''

import os
import random as r
import math as m
import enemy
import testes
import armas


# decl var
Fp = 1
Dp = 2
Lp = 10
Mp = 0
opc = str
esc = True
hero_stats = {'força': Fp, 'Dext': Dp, 'Vida': Lp, 'Magia': Mp}
hero_inv = (10, 12)


def menu():
    print(32 * '-')
    print(f"\n               menu\n")
    print(32 * '-')

def inventory():
    print(hero_inv)


def game_core():
    print("Menu // Sair // Inventario // Stats\n")
    nav_opc = str(input())
    if nav_opc == 'menu':
        menu()
    elif nav_opc == 'sair':
        sair()

    elif nav_opc == 'inventario':
        inventory()

    elif nav_opc == 'stats':
        champion()
    else:
        print("Valor Inválido")


#para sair
def sair():
    opc = str(input("Digite sim para continuar ou sair para sair\n"))
    if (opc == 'sim' or 's'):
        esc = True
        os.system('cls')
        print('')

    elif (opc == 'sair' or 'n'):
        os.system('cls')
        esc = False
        print('Saindo')

    else:
        os.system('cls')
        print("Comando inválido")


def champion():
    print(f'{hero_stats}')



#def hunt():
  


while esc == True:
    game_core()

