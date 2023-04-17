import pyttsx3

from tkinter import *
import itertools
import math
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime
from orbitalsim.presets import SolarSystem
from orbitalsim.presets import EarthMoon


import os
import time
import wikipedia
import wolframalpha
import webbrowser
import psutil
import random
from random import randrange
import speech_recognition as sr
import pygame
from random import randint

engine = pyttsx3.init()


def menu():
    mat = 0

    print('''           [opção 1]Telescópio.
               [opção 2]Espectrógrafos e detectores.
               [opção 3]A radiação eletromagnética e as leis da radiação.
               [opção 4]As linhas espectrais e o Efeito Doppler.
               [opção 5]Estrelas e suas maravilhas.
               [opção 6]Planetas,exoplanetas os seus satélites.
               [opção 7]Sair do curso.''')
    engine.say('''      [opção 1] Telescópio.
               [opção 2]Espectrógrafos e detectores.
               [opção 3]A radiação eletromagnética e as leis da radiação.
               [opção 4]Efeito Doppler.
               [opção 5]Estrelas e suas maravilhas.
               [opção 6]Planetas,exoplanetas e os seus satélites.
               [opção 7]Sair do curso.''')

    engine.runAndWait()
    engine.stop()
    engine.say("Qual opção você deseja?")
    engine.runAndWait()
    engine.stop()

    while mat != 7:
        mat = int(input("Qual opção  você deseja?"))
        if mat == 1:
            print("Telescópio")
            engine.say("telescópio")
            engine.runAndWait()
            engine.stop()
            engine.say("Quer continuar?(use s para sim e n para não")
            engine.runAndWait()
            engine.stop()
            astc =input("Quer continuar?(use 's' para sim e 'n' para não")
            if astc == "s":
                print(
                    "Antes vamos entender alguns conceitos, como a óptica adaptativa,óptica ativa e os espelhos esféricos.")
                print(
                    "A óptica ativa refere-se a uma tecnologia, empregada em telescópios refletores, cujo objetivo é corrigir as pequenas deformações causadas no espelho.")
                print(
                    "Óptica adptativa, é usada para diminuir o efeito da turbulência atmosférica na imagem.")
                print(
                    "Espelhos esféricos, em algumas situações, podem aumentar a imagem, como aqueles usados para segurança em mercados")

                print(
                    "Os telescópios, clássicos, foram inventados em 1608,mas como as atuais lunetas. A primeira luneta foi apontada para o céu em 1609. Antes disso a humanidade já olhava para o céu e questionava o que é aquilo que viam, entretanto era usado como a atual luneta.Sendo aprimorado por Galileu,ele mesmo resolveu experimentar e fabricar o seu próprio instrumento, que tinha um aumento de vinte vezes ")
                print(
                    "Newton, fascinado com o instrumento, criou um similar para igualar-se ao Galileu.")
                print(
                    "Eles,  as ferramentas ópticas, tinham características diferentes, como o de Galileu, que usava lentes refratoras, e Newton criadors do telescópio com lentes refletoras")
                print("Portanto, são assim que os telecópios são nomeados,pelas suas lentes o outros componentes.")
                print("vamos analisa-las")
                print(
                    "Telescópios refratores, são telescópios com tubos longos e relativamente finos, com uma lente objetiva na frente, que coleta e focaliza a luz.")
                print(
                    "Vantagens – os refratores são mais resistentes, precisam de pouca ou nenhuma manutenção, e seus tubos são selados, o que evita poeira e correntes de ar internas. Se as lentes forem de boa qualidade, proporcionarão imagens definidas e de alto contraste, o que é especialmente desejável para a Lua e os planetas.")
                print(
                    "Desvantagens – Em geral, os refratores possuem pequena abertura, tipicamente entre 6 e 10 centímetros. Para muitos propósitos astronômicos, isso é muito pouco. Os objetos escuros, como galáxias e nebulosas, aparecerão muito fracos, se você for capaz de detectá-los. O refrator inverte a imagem da esquerda para a direita, tornando difícil compará-la com os mapas celestes.")

                engine.say(
                    "Antes vamos entender alguns conceitos como a óptica adaptativa , óptica ativa e os espelhos esféricos.")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A óptica ativa refere-se a uma tecnologia, empregada em telescópios refletores, cujo objetivo é corrigir as pequenas deformações causadas no espelho, dentro dos telescópios  com mais de 5 metros de diâmetros")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Óptica adptativa, é usada para diminuir o efeito da turbulência atmosférica na imagem")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Espelhos esféricos, em algumas situações, podem aumentar a imagem, como aqueles usados para segurança em mercados")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os telescópios, clássicos, foram inventados em 1608,mas como a atual luneta")
                engine.runAndWait()
                engine.stop()
                engine.say(" A primeira luneta foi apontada para o céu em 1609 ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Antes disso a humanidade já olhava para o céu e questionava o que é aquilo que viam, entretanto era usado como a atual luneta")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Sendo aprimorado por Galileu,ele mesmo resolveu experimentar e fabricar o seu próprio instrumento, que tinha um aumento de vinte vezes ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Newton, fascinado com o instrumento, criou um similar para igualar-se ao Galileu")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Eles,  as ferramentas ópticas, tinham características diferentes, como o de Galileu, que usava lentes refratoras, e Newton criadors do telescópio com lentes refletoras")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Portanto, são assim que os telescópios são nomeados,pelas suas lentes e o outros componentes")
                engine.runAndWait()
                engine.stop()
                engine.say("vamos analisa-las")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Telescópios refratores, são telescópios com tubos longos e relativamente finos, com uma lente objetiva na frente, que coleta e focaliza a luz")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Vantagens – os refratores são mais resistentes, precisam de pouca ou nenhuma manutenção, e seus tubos são selados, o que evita poeira e correntes de ar internas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Se as lentes forem de boa qualidade, proporcionarão imagens definidas e de alto contraste, o que é especialmente desejável para a Lua e os planetas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Desvantagens – Em geral, os refratores possuem pequena abertura, tipicamente entre 6 e 10 centímetros")
                engine.runAndWait()
                engine.stop()
                engine.say("Para muitos propósitos astronômicos, isso é muito pouco ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os objetos escuros, como galáxias e nebulosas, aparecerão muito fracos, se você for capaz de detectá-los ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O refrator inverte a imagem da esquerda para a direita, tornando difícil compará-la com os mapas celestes")
                print("Vamos ver como é o esquema dele")
                engine.say("Vamos ver como é o esquema deles")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.google.com/imgres?imgurl=http%3A%2F%2Fastro.if.ufrgs.br%2Ftelesc%2Frefrator.gif&imgrefurl=http%3A%2F%2Fastro.if.ufrgs.br%2Ftelesc%2Fnode2.htm&tbnid=akd1-I_v-0ZqFM&vet=12ahUKEwj-1ZzNxLfsAhWCLbkGHUE7C7IQMygCegUIARC5AQ..i&docid=0GcOasETJwE5HM&w=598&h=198&q=telescopio%20refratores&ved=2ahUKEwj-1ZzNxLfsAhWCLbkGHUE7C7IQMygCegUIARC5AQ")
                print(
                    "A luz passa pelo bocal e chegando em uma lente, onde fica o foco da luz, que faz o processo de 'tratamento' e vai ao olho do observador, por causa do 'foco da imagem' ela fica invertida")
                engine.say(
                    "A luz passa pelo bocal e chegando em uma lente, onde fica o foco da luz, que faz o processo de 'tratamento' e vai ao olho do observador, por causa do 'foco da imagem' ela fica invertida")
                engine.runAndWait()
                engine.stop()
                print(
                    "Telescópios refletores usam um espelho grande e curvado, ao invés de lentes, para colher e focar a luz , você observa a imagem obtida através de uma ocular colocada em um lado do tubo próximo ao topo.")
                print("Vantagem:É simples o suficiente para ser construído em casa ")
                print("Como contém dois espelhos, a imagem que proporciona não é invertida ")
                print("Este telescópio possibilita a adoção de montagem mais estável")
                print(
                    "Desvantagens – refletores requerem mais cuidado e manutenção O tubo é aberto para o exterior, possibilitando acúmulo de poeira no espelhos  e os espelhos necessitam de ajustamentos ocasionais, para que sejam mantidos em alinhamento perfeito, em um procedimento simples mas um pouco tedioso")
                print(
                    "Curiosidade: Os telescópios servem como coletores de luz: Eles amplificam a pupila do olho humano")
                print(
                    " A quantidade de luz que eles são capazes de coletar é proporcional ao quadrado da abertura (um telescópio de 4 metros coleta 16 vezes mais do que um telescópio de 1 metro)")
                print(
                    " A capacidade de coletar luz é proporcional ao quadrado do diâmetro, (diâmetro = abertura)")
                print("Vamos ver como é o esquema deles")
                engine.say("Vamos ver como é o esquema deles")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.google.com/imgres?imgurl=http%3A%2F%2Fastro.if.ufrgs.br%2Ftelesc%2Frefletor.gif&imgrefurl=http%3A%2F%2Fastro.if.ufrgs.br%2Ftelesc%2Fnode2.htm&tbnid=n7IEV_S8Es58lM&vet=12ahUKEwi-19nQ27fsAhWFBbkGHQhhBZQQMygBegUIARCpAQ..i&docid=0GcOasETJwE5HM&w=348&h=216&q=telesc%C3%B3pio%20refletor&hl=pt-BR&ved=2ahUKEwi-19nQ27fsAhWFBbkGHQhhBZQQMygBegUIARCpAQ#imgrc=mUDtHptigT5vAM&imgdii=fyFyWsjbz_kLWM")
                print(
                    "A luz passa pelo bocal, vão ao espelho esférico M1, que reflete a luz parao espelho plano M2, mesmo tendo a base fixa no interior do telescópio, não atrapalha na observação")
                engine.say(
                    "A luz passa pelo bocal, vão ao espelho esférico M1, que reflete a luz parao espelho plano M2, mesmo tendo a base fixa no interior do telescópio, não atrapalha na observação")
                engine.runAndWait()
                engine.stop()
                print(
                    "Logo se percebeu que era preciso construir lentes ou espelho maiores ,pois era necessário coletar mais luz e um espelho maior produz uma nitidez melhor,Surgindo os telescópios Catadioptricos,compostos por lentes e espelhos ao mesmo tempo.")
                print(
                    "Vantagem:Proporciona uma portabilidade e conveniência muito maior que qualquer outro telescópio, para aberturas maiores")
                print(
                    "Desvantagem:Nunca parecerá tão definida quanto a formada por um bom refletor com a mesma abertura, especialmente quando se observa planetas seu custo é maior do que o de um refletor da mesma abertura e um espelho de ângulo reto geralmente é usado para proporcionar mais conforto para a observação, e isto significa que a imagem é invertida da esquerda para a direita, como num espelho")

                print(
                    "A qualidade científica de um telescópio é dada pela razão da área coletora, denominada de D, pela nitidez da imagem, simbolizado por R, ao quadrado"
                    "Logo:(D/R)²")
                engine.say(
                    "Logo se percebeu que era preciso construir lentes ou espelho maiores ,pois era necessário coletar mais luz e um espelho maior produz uma nitidez melhor")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Surgindo os telescópios Catadióptricos,compostos por lentes e espelhos ao mesmo tempo")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Vantagem:Proporciona uma portabilidade e conveniência muito maior que qualquer outro telescópio, para aberturas maiores")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Desvantagem:Nunca parecerá tão definida quanto a formada por um bom refletor com a mesma abertura, especialmente quando se observa planetas")
                engine.runAndWait()
                engine.stop()
                engine.say(" Seu custo é maior do que o de um refletor da mesma abertura ")
                engine.runAndWait()
                engine.stop()
                print("Vamos ver o e esquema")
                engine.say("Vamos ver o e esquema")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wixstatic.com%2Fmedia%2F73d37e_7f2219aca59a4af3978ab8e7d6196676.png%2Fv1%2Ffill%2Fw_320%2Ch_146%2Cal_c%2Cq_85%2F73d37e_7f2219aca59a4af3978ab8e7d6196676.webp&imgrefurl=https%3A%2F%2Fofficialwebsitebr.wixsite.com%2Fde-olho-no-universo%2Ftelescpios-&tbnid=lXuY_5WAGC-BKM&vet=12ahUKEwi4oLmp3bfsAhWGCrkGHeh5AKsQMygHegUIARChAQ..i&docid=gBB43fbNYsltyM&w=320&h=146&q=telesc%C3%B3pios%20Catadioptricos%20como%20funciona&hl=pt-BR&ved=2ahUKEwi4oLmp3bfsAhWGCrkGHeh5AKsQMygHegUIARChAQ#imgrc=W8zNR_UboArCmM&imgdii=uk0GxCXg5F18NM")
                print(
                    "A luz toma uma trajetória, que consiste passar por uma lenete corretora no bocal do telescópio, após isso um espelho esférico que direciona um outro espelhos planos, levando a luz para o observador")
                engine.runAndWait()
                engine.stop()
                engine.say("Vamos ver o e esquema")

                print("definindo alguns conceitos: ")
                print(
                    "Razão focal( simbolizado pelo  f menor): f= F/D, ou seja  A divisão da distância focal F pela abertura D ")
                print("Abertura, diâmetro do espelho ou lente é o D")
                print(
                    "Distância focal: a distância da lente (ou espelho) ao foco, sendo o  F da equação")
                engine.runAndWait()
                engine.stop()
                engine.say("definindo alguns conceitos: ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Razão focal( simbolizado pelo  f menor): f= F/D, ou seja  A divisão da distância focal F pela abertura D ")
                engine.runAndWait()
                engine.stop()
                engine.say("Abertura, diâmetro do espelho ou lente é o D")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Distância focal: a distância da lente (ou espelho) ao foco, sendo o  F da equação")
                engine.runAndWait()
                engine.stop()
                print("Vamos de exercícios")
                engine.say("Vamos de exercícios")

                respq = 0
                engine.say(
                    "Qual a razão focal de um telescópio com a lente de 200 milímetros e 1400 milímetros de distância focal?")
                engine.runAndWait()
                engine.stop()
                while respq != 7:

                    respq = int(input(
                        "Qual a razão focal de um telescópio com a lente de 200 milímetros e 1400 milímetros de distância focal?"))
                    if respq == 7:
                        print("Você acertou")
                        engine.say(
                            "Você acertou")
                        engine.runAndWait()
                        engine.stop()

                    else:
                        print("Você errou...Tente novamente")

                        engine.say("Você errou...Tente novamente")
                        engine.runAndWait()
                        engine.stop()
                respq1 = 0
                engine.say(
                    "Um telescópio tem 4 metros de diâmentro, na sua abertura, e suas imagens tem a classificação 2 de nitidez,Qual é a qualidade dessa ferramenta?")
                engine.runAndWait()
                engine.stop()
                while respq1 != 4:
                    respq1 = int(input(
                        "Um telescópio tem 4 metros de diâmentro, na sua abertura, e suas imagens tem a classificação 2 de nitidezQual é a qualidade dessa ferramenta?"))
                    if respq1 == 4:
                        print("Você acertou")
                        engine.say(
                            "Você acertou")
                        engine.runAndWait()
                        engine.stop()
                    else:
                        print("Você errou...Tente novamente")
                        engine.say("Você errou...Tente novamente")
                        engine.runAndWait()
                        engine.stop()
                print("Terminamos essa parte do curso")
                engine.say("Terminamos essa parte do curso")
                engine.runAndWait()
                engine.stop()
                menu()
            if astc == "n":
                print("Tudo bem...Vou te redicionar para os temas")
                engine.say("Tudo bem...Vou te redicionar para os temas")
                engine.runAndWait()
                engine.stop()
                menu()
            else:
                print("Opção não aceitável")
                engine.say("Opção não aceitável")
                engine.runAndWait()
                engine.stop()



        if mat == 2:
            print("Espectrógrafos e Detectores")
            engine.say("Espectrógrafos e Detectores")
            engine.say("Quer continuar?(use s para sim e n para não")
            engine.runAndWait()
            engine.stop()
            astc = input("Quer continuar?(use 's' para sim e 'n' para não")
            if astc == "s":
                print(
                    "São extremamente importantes para um astrofísico. Os telescópios  também são importantes, pois coletam a luz, mas não analisam a luz para obter informações. Tudo que se sabe sobre estrelas, nebulosas e galáxias veio através da radiação eletromagnética.Por exemplo, quando você olha para uma flor, os dados da flor são captados pelo seu olho, mas o olho não consegue interpretar o que está vendo e sim o seu cérebro.")
                print(
                    "O que é um espectro? Já ouviu falar que Isaac Newton conseguiu mostrar que a luz branca é composta por arco-íris? Luz vermelha, amarela, verde, azul e lilás.")
                print(
                    "Caso não se lembre vou abrir uma aba no navegador para refrescar tua memória")
                engine.say("São extremamente importantes para um astrofísico ")
                engine.runAndWait()
                engine.stop()
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os telescópios também são importantes, pois coletam a luz, mas não analisam a luz para obter informações")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Tudo que se sabe sobre estrelas, nebulosas e galáxias veio através da radiação eletromagnética ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Por exemplo, quando você olha para uma flor, os dados da flor são captados pelo seu olho, mas o olho não consegue interpretar o que está vendo e sim o seu cérebro")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O que é um espectro? Já ouviu falar que Isaac Newton conseguiu mostrar que a luz branca é composta por arco-íris? Luz vermelha, amarela, verde, azul e lilás")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Caso não se lembre vou abrir uma aba no navegador para refrescar tua memória")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fproec.ufabc.edu.br%2Fgec%2Fwp-content%2Fuploads%2F2018%2F07%2Fprism.jpg&imgrefurl=https%3A%2F%2Fproec.ufabc.edu.br%2Fgec%2Fo-que-que-a-ciencia-tem%2Farco-iris-de-sons-o-que-seria%2F&tbnid=uFR2NQdpF8zfxM&vet=12ahUKEwihvI-npLfsAhWaIrkGHX_cC6UQMygCegUIARCpAQ..i&docid=YqIXPurg2lJELM&w=1920&h=1080&q=newton%20prisma%20f%C3%ADsica&ved=2ahUKEwihvI-npLfsAhWaIrkGHX_cC6UQMygCegUIARCpAQ')
                print("Viu?")
                print(
                    " Isso é feito por um prisma, é a maneira primitiva de se produzir um espectro, decompor a luz e tentar extrair informação dela. É claro que o prisma é um instrumento muito simples e para otimizar isso, precisa construir sistemas mais complexos.")
                print(
                    "O primeiro detector que foi  usado para observar o céu foi o olho humano.Não é um detector ruim, tendo uma eficiência quântica bastante razoável. ")
                print(
                    "(Eficiência quântica é a porcentagem de fótons que incidem, que são efetivamente registrados. Então de cada 100 fótons que incidem no seu olho, você registra 1,então a eficiência quântica do seu olho é 1%.Isso parece ser baixa, mas uma placa fotográfica também registra 1%.)")
                print(
                    "Sendo que a invenção da primeira placa fotográfica foi um ganho muito grande na história da astronomia. Não pela eficiência, já que é a mesma do olho, mas pelo fato do  o olho  integrar a luz durante uma fração de segundos.Contrário da fotografia, na qual  você pode expor uma chapa fotográfica no telescópio, por horas e se quiser uma noite inteira. Para observar os objetos muito mais fracos do que seria possível usando apenas o olho humano no telescópio, por mais tempo.")
                print("Hoje não se usa mais placa fotográfica e nem olho humano.")
                print(
                    "'Se você vai em um telescópio moderno e me perguntar onde que põe o olho para observar, vou dizer que não existe lugar para você colocar o olho para observar. Isso não existe mais. É tudo feito por computadores e você fica em uma sala distante do telescópio. Se o telescópio estiver no Chile, o observador pode estar aqui no Brasil, não precisa viajar. É tudo remoto, tudo por computador.'-  João Steiner,2014 ")
                print("Voltando ao assunto")
                print("Então se tiver um detector, você vai colocar ele em um espectrógrafo. ")
                print(
                    "Imagine que você tenha um espectrógrafo, tem apenas um elemento de expressão que é o prisma, que dispersa a luz e ela é registrada.")
                print("Veja como eles são e os dados obtidos")
                engine.say("Viu?")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Isso é feito por um prisma, é a maneira primitiva de se produzir um espectro, decompor a luz e tentar extrair informação dela")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " É claro que o prisma é um instrumento muito simples e para otimizar isso, é precisa construir sistemas mais complexos")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O primeiro detector que foi  usado para observar o céu foi o olho humano")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Não é um detector ruim, tendo uma eficiência quântica bastante razoável ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Eficiência quântica é a porcentagem de fótons que incidem, que são efetivamente registrados ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Então de cada 100 fótons que incidem no seu olho, você registra 1,logo a eficiência quântica do seu olho é 1%")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Isso parece ser baixa, mas uma placa fotográfica também registra 1%")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Sendo que a invenção da primeira placa fotográfica foi um ganho muito grande na história da astronomia ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Não pela eficiência, já que é a mesma do olho, mas pelo fato do  o olho  integrar a luz durante uma fração de segundos")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Contrário da fotografia, na qual  você pode expor uma chapa fotográfica no telescópio, por horas e se quiser uma noite inteira ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Para observar os objetos muito mais fracos do que seria possível usando apenas o olho humano no telescópio, por mais tempo")
                engine.runAndWait()
                engine.stop()
                engine.say("Hoje não se usa mais placa fotográfica e nem olho humano")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "'Se você vai em um telescópio moderno e me perguntar onde que põe o olho para observar, vou dizer que não existe lugar para você colocar o olho para observar, isso não existe mais, É tudo feito por computadores e você fica em uma sala distante do telescópio, Se o telescópio estiver no Chile, o observador pode estar aqui no Brasil, não precisa viajar, É tudo remoto, tudo por computador' João Steiner,2014 ")
                engine.runAndWait()
                engine.stop()
                engine.say("Voltando ao assunto")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Então se tiver um detector, você vai colocar ele em um espectrógrafo ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Imagine que você tenha um espectrógrafo, tem apenas um elemento de expressão que é o prisma, que dispersa a luz e ela é registrada")
                engine.runAndWait()
                engine.stop()
                engine.say("Veja como eles são e os dados obtidos")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F3%2F37%2FEspectr%25C3%25B3grafo.gif%2F220px-Espectr%25C3%25B3grafo.gif&imgrefurl=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FEspectr%25C3%25B3grafo&tbnid=avGUSbB8LSZi4M&vet=12ahUKEwixg_G4trfsAhVxBbkGHS35CH4QMygAegUIARCRAQ..i&docid=affGCMZ3AClooM&w=220&h=169&q=Espectr%C3%B3grafos&ved=2ahUKEwixg_G4trfsAhVxBbkGHS35CH4QMygAegUIARCRAQ#imgrc=avGUSbB8LSZi4M&imgdii=wRIMwyYtsI9acM')
                print("Isso são os componentes do espectrofotômetro.")
                print("Eles são assim, por dentro do:")
                engine.say("Isso são os componentes do Espectrofotômetro")
                engine.runAndWait()
                engine.stop()
                engine.say("Eles são assim, por dentro do espectrofotômetro")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.inovacaotecnologica.com.br%2Fnoticias%2Fimagens%2F010130160628-espectrografo-steles.jpg&imgrefurl=https%3A%2F%2Fwww.inovacaotecnologica.com.br%2Fnoticias%2Fnoticia.php%3Fartigo%3Despectrografo-brasileiro%26id%3D010130160628&tbnid=gGEIo6Sk19n6vM&vet=12ahUKEwixg_G4trfsAhVxBbkGHS35CH4QMygCegUIARCWAQ..i&docid=oJps3-D9wAzttM&w=550&h=419&q=Espectr%C3%B3grafos&ved=2ahUKEwixg_G4trfsAhVxBbkGHS35CH4QMygCegUIARCWAQ")
                print("Seus dados são analisádos dessa forma.")
                engine.say("Seus dados são analisádos dessa forma")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fnoirlab.edu%2Fpublic%2Fmedia%2Farchives%2Fimages%2Fpublicationjpg%2Fnoao-sun.jpg&imgrefurl=https%3A%2F%2Fnoirlab.edu%2Fpublic%2Fimages%2Fnoao-sun%2F&tbnid=pL7drMtcg_UwuM&vet=12ahUKEwiu0ZjiuLfsAhWFBbkGHQhhBZQQMygBegQIARB8..i&docid=QO8WhB2KCoxAbM&w=4000&h=2668&q=high%20resolution%20solar%20spectrum&ved=2ahUKEwiu0ZjiuLfsAhWFBbkGHQhhBZQQMygBegQIARB8")
                print(
                    "Por ser muito teórico, não quero força-lo a resolver exercícios, só quero que guarde e pense nisso.")
                engine.say(
                    "Por ser muita teórico, não quero força-lo a resolver exercícios, só quero que guarde e pense nisso")
                engine.runAndWait()
                engine.stop()
                print("Terminamos essa parte do curso")
                engine.say("Terminamos essa parte do curso")
                engine.runAndWait()
                engine.stop()
                menu()
            if astc == "n":
                print("Tudo bem...Vou te redicionar para os temas")
                engine.say("Tudo bem...Vou te redicionar para os temas")
                engine.runAndWait()
                engine.stop()
                menu()
            else:
                print("Opção não aceitável")
                engine.say("Opção não aceitável")
                engine.runAndWait()
                engine.stop()



        if mat == 3:
            print("Espectrógrafos e Detectores")
            engine.say("Espectrógrafos e Detectores")
            engine.say("Quer continuar?(use s para sim e n para não")
            engine.runAndWait()
            engine.stop()
            astc = input("Quer continuar?(use 's' para sim e 'n' para não")
            if astc == "s":
                print("A radiação eletromagnética e as leis da radiação.")
                engine.say("A radiação eletromagnética e as leis da radiação")
                engine.runAndWait()
                engine.stop()
                print("Conceitos iniciais:")
                print(
                    "A carga elétrica,uma propriedade das partículas elementares que compõem o átomo.")
                print(
                    "A oscilação,movimento de um corpo suspenso similar ao do pêndulo de um relógio; balanço.")
                print(
                    "A frequência,uma grandeza física que indica o número de ocorrências de um evento em um determinado intervalo de tempo.")
                print(
                    "O comprimento de onda é a separação de dois picos, dois máximos ou dois mínimos, denominados de Λ ou lâmbda ")
                print(
                    "O espectro eletromagnético é emitido sempre que estiver uma carga elétrica oscilando e dependendo de como essa carga oscila, ela vai emitir uma onda eletromagnética com a mesma frequência da oscilação da carga elétrica. Essa frequência pode variar muito e dependendo da frequência, é classificado essa onda eletromagnética em faixas do espectro eletromagnético.Tais faixas podem ser tanto ondas longas de rádio, ondas de rádio AM, FM, ondas curtas, micro-ondas, infravermelho.")
                print(
                    "A luz visível é uma faixa bem estreita e pode ser ampliada nas cores do arco-íris, depois vem o ultravioleta, raio x e raios gama.Como já dito, tal oscilação ou movimento, é feito pelo fóton, pequena partícula que compõe a luz, sendo assim ele 'vibra' e emite radiação eletromagnética.")
                print("Levando a Leis de Kirchhoff :")
                print(
                    "1) Um corpo opaco quente, sólido, líquido ou gasoso, emite um espectro contínuo.")
                print(
                    "2) Um gás transparente produz um espectro de linhas brilhantes (de emissão). O número posição e as linhas dependem dos elementos químicos presentes no gás.")
                print(
                    "3) Se um espectro contínuo passar por um gás à temperatura mais baixa, o gás frio causa a presença de linhas escuras (absorção). O número posição e as linhas dependem dos elementos químicos presentes no gás.")
                print("Para entender melhor vamos ver como ela se comporta:")
                engine.say("Conceitos iniciais:")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A carga elétrica,uma propriedade das partículas elementares que compõem o átomo")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A oscilação,movimento de um corpo suspenso similar ao do pêndulo de um relógio; balanço")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A frequência,uma grandeza física que indica o número de ocorrências de um evento em um determinado intervalo de tempo")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O comprimento de onda é a separação de dois picos, dois máximos ou dois mínimos, denominados de  lâmbda ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O espectro eletromagnético é emitido sempre que estiver uma carga elétrica oscilando e dependendo de como essa carga oscila, ela vai emitir uma onda eletromagnética com a mesma frequência da oscilação da carga elétrica. Essa frequência pode variar muito e dependendo da frequência, é classificado essa onda eletromagnética em faixas do espectro eletromagnético.Tais faixas podem ser tanto ondas longas de rádio, ondas de rádio AM, FM, ondas curtas, micro-ondas, infravermelho.")
                engine.runAndWait()
                engine.stop()
                engine.say("Levando a Leis de Kirchhoff ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "1) Um corpo opaco quente, sólido, líquido ou gasoso, emite um espectro contínuo")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "2) Um gás transparente produz um espectro de linhas brilhantes (de emissão)")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " O número posição e as linhas dependem dos elementos químicos presentes no gás")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "3) Se um espectro contínuo passar por um gás à temperatura mais baixa, o gás frio causa a presença de linhas escuras (absorção)")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " O número posição e as linhas dependem dos elementos químicos presentes no gás")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A luz visível é uma faixa bem estreita e pode ser ampliada nas cores do arco-íris, depois vem o ultravioleta, raio x e raios gama")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Como já dito, tal oscilação ou movimento, é feito pelo fóton, pequena partícula que compõe a luz, sendo assim ele 'vibra' e emite radiação eletromagnética")
                engine.runAndWait()
                engine.stop()
                engine.say("Para entender melhor vamosver como ela se comporta:")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.infoescola.com/wp-content/uploads/2010/01/radiacao-eletromagnetica-2.jpg")
                print(
                    "O campo elétrico oscila perpendicularmente ao campo magnético, e a direção de propagação é dada pelo vetor de Poynting")
                print(
                    "O vetor de Poynting é sempre perpendicular aos vetores E e B. A figura a seguir mostra o campo elétrico oscilando no eixo z e o campo magnético no eixo x de um sistema cartesiano.")
                print(
                    "Consequentemente, o vetor de Poynting estará no eixo y deste sistema de coordenadas, sempre coincidindo com a direção de propagação da onda.")
                engine.say(
                    "O campo elétrico oscila perpendicularmente ao campo magnético, e a direção de propagação é dada pelo vetor de Poynting")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O vetor de Poynting é sempre perpendicular aos vetores E e B, A figura a seguir mostra o campo elétrico oscilando no eixo z e o campo magnético no eixo x de um sistema cartesiano")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Consequentemente, o vetor de Poynting estará no eixo y deste sistema de coordenadas, sempre coincidindo com a direção de propagação da onda")
                engine.runAndWait()
                engine.stop()
                print("outros exemplos:")
                print(
                    "Ondas longas de rádio podem ter 1km de comprimento, já a micro-ondas tem 1 centésimo de km, ou seja, alguns milímetros.")
                print(
                    "(Essas ondas do espectro magnético são emitidas por corpos: antena de rádio, nosso corpo ou átomos.)")
                print(
                    "Para o corpo emitir radiação, ele precisa estar a uma certa temperatura. Por exemplo: para emitir ondas de rádio, é preciso estar a 10Kelvin (10k), ou seja -263,15 Cº, para emitir a luz visível é preciso estar entre 1000 a 10000Kelvin (1000K), também 727 Cº até 9727 Cº. ")
                print(
                    "Se você pegar um ferro e aquecer ele bastante, quando chegar a cerca de 1000 Cº graus ele ficará vermelho. Se conseguir subir mais a temperatura até 10000 Cº, ele vai ficar azul. Portanto o comprimento de onda depende da temperatura")
                print(
                    "Sendo assim,Se você tiver uma carga elétrica que oscila v(lê-se: mi) vezes por segundo, ela vai emitir uma onda magnética com frequência v  ou também chamada de Hertz. ")
                print("A fórmula seria:")
                print("f = v/Λ")
                print("f:Frequência")
                print("v: velocidade de fase ou mi")
                print("Λ:comprimento de onda ou lâmbda")
                engine.say("outros exemplos:")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Ondas longas de rádio podem ter 1km de comprimento, já a micro-ondas tem 1 centésimo de km, ou seja, alguns milímetros")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "(Essas ondas do espectro magnético são emitidas por corpos: antena de rádio, nosso corpo ou átomos)")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Para o corpo emitir radiação, ele precisa estar a uma certa temperatura")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Por exemplo: para emitir ondas de rádio, é preciso estar a dez Kelvin , ou seja duzentos e setenta e três graus celsius negativo, para emitir a luz visível é preciso estar entre mil a dez mil  Kelvin, também setecentos e vintesete  graus celsius até nove setecentos e vintesete graus celsius ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Se você pegar um ferro e aquecer ele bastante, quando chegar a cerca de mil graus celsius graus ele ficará vermelho. Se conseguir subir mais a temperatura até dez mil graus celsius, ele vai ficar azul. Portanto o comprimento de onda depende da temperatura")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Sendo assim,Se você tiver uma carga elétrica que oscila v(lê-se: mi) vezes por segundo, ela vai emitir uma onda magnética com frequência v  ou também chamada de Hertz")
                engine.runAndWait()
                engine.stop()
                engine.say("A fórmula seria:")
                engine.runAndWait()
                engine.stop()
                engine.say("f = v/Λ")
                engine.runAndWait()
                engine.stop()
                engine.say("f= Frequência")
                engine.runAndWait()
                engine.stop()
                engine.say("mi = velocidade de fase ")
                engine.runAndWait()
                engine.stop()
                engine.say("lâmbda:comprimento de onda")
                engine.runAndWait()
                engine.stop()
                print("Vamos de exercício")
                engine.say("Vamos de exercício")
                engine.runAndWait()
                engine.stop()

                respq22 = 0
                while respq22 != 2:
                    engine.say(
                        "uma onda mecânica que se propaga com velocidade de 20 metros por segundo.Sabendo que  o comprimento de tal onda é 40 centímetro, A frequência em hertz é...?")
                    engine.runAndWait()
                    engine.stop()
                    respq22 = int(input(
                        "uma onda mecânica que se propaga com velocidade de 20 m/s.Sabendo que  o comprimento de tal onda é 40 cm, A frequência em HZ é...?"))
                    if respq22 == 2:
                        print("Você acertou")
                    else:
                        print("Você errou...Tente novamente")
                print("Terminamos essa parte do curso")
                engine.say("Terminamos essa parte do curso")
                engine.runAndWait()
                engine.stop()
                menu()
            if astc == "n":
                print("Tudo bem...Vou te redicionar para os temas")
                engine.say("Tudo bem...Vou te redicionar para os temas")
                engine.runAndWait()
                engine.stop()
                menu()
            else:
                print("Opção não aceitável")
                engine.say("Opção não aceitável")
                engine.runAndWait()
                engine.stop()

        if mat == 4:
                print(" Efeito Doppler. ")
                engine.say(" Efeito Doppler")
                engine.runAndWait()
                engine.stop()
                engine.say("Quer continuar?(use s para sim e n para não")
                engine.runAndWait()
                engine.stop()
                astc = input("Quer continuar?(use 's' para sim e 'n' para não")
                if astc == "s":
                    print(
                        "O efeito Doppler é um fenômeno ondulatório caracterizado pela mudança do comprimento de onda ou da frequência de uma onda emitida por uma fonte que se movimenta em relação a um observador.")
                    print(
                        "Esse fenômeno acontece pelo fato de que a velocidade de propagação de uma onda, seja ela qual for, depende exclusivamente do meio pelo qual essa onda propaga-se. Assim, mesmo que a fonte das ondas ou o observador mova-se, a velocidade de propagação da onda não será alterada.")
                    print(
                        "Um exemplo típico do efeito Doppler é o caso de uma ambulância com a sirene ligada, durante a aproximação ou afastamento de um observador. Quando ela aproxima-se do observador, o som é mais agudo; e, quando a ambulância afasta-se, o som é mais grave. Esse é um fenômeno característico de qualquer propagação ondulatória, e ele é muito mais presente no cotidiano do que pensamos.")
                    print(
                        "O efeito Doppler não ocorre somente com o som. Como foi dito, esse fenômeno é característico de propagações ondulatórias, ou seja, é possível observar esse fenômeno com qualquer tipo de onda. Dessa forma, podemos observar o efeito Doppler com a luz, que também é uma onda. Para esse caso, o fenômeno do efeito Doppler manifesta-se na mudança de cor que é percebida pelo observador. Uma pessoa que se aproxima de um sinal de trânsito que está vermelho, por exemplo, percebe a coloração vermelha mais intensa se ela estiver parada, pois a frequência de onda luminosa é maior do que quando o observador está em movimento.")
                    print(
                        "O uso efeito Doppler está na possibilidade de medir a velocidade de objetos por meio de ondas que são emitidas por aparelhos baseados em radiofrequência ou lasers, como os radares. Na Astronomia, esse fenômeno é usado para medir a velocidade relativa das estrelas e de outros objetos celestes em relação ao planeta Terra. Na medicina, o efeito Doppler é utilizado nos exames de ecocardiograma para medir a direção e a velocidade do fluxo sanguíneo ou do tecido cardíaco.")
                    print("Vamos ver tal fórmula:")
                    print("Fo: (V/ V -+ Vf).Ff")
                    print(
                        "*Sendo o sinal negativo utilizado no caso onde a fonte se aproxima e positivo no caso em que a fonte se afasta.")
                    print("Fo: frequência  aparente percebida pelo observador.")
                    print("Ff: frequência real emitida.")
                    print("Vo: velocidade do observador.")
                    print("Vf: velocidade da fonte.")
                    print("V : velocidade da onda sonora.")
                    engine.say(
                        "O efeito Doppler é um fenômeno ondulatório caracterizado pela mudança do comprimento de onda ou da frequência de uma onda emitida por uma fonte que se movimenta em relação a um observador")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        "Esse fenômeno acontece pelo fato de que a velocidade de propagação de uma onda, seja ela qual for, depende exclusivamente do meio pelo qual essa onda propaga-se ")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        "Assim, mesmo que a fonte das ondas ou o observador mova-se, a velocidade de propagação da onda não será alterada")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        "Um exemplo típico do efeito Doppler é o caso de uma ambulância com a sirene ligada, durante a aproximação ou afastamento de um observador")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Quando ela aproxima-se do observador, o som é mais agudo e, quando a ambulância afasta-se, o som é mais grave")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Esse é um fenômeno característico de qualquer propagação ondulatória, e ele é muito mais presente no cotidiano do que pensamos")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("O efeito Doppler não ocorre somente com o som")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Como foi dito, esse fenômeno é característico de propagações ondulatórias, ou seja, é possível observar esse fenômeno com qualquer tipo de onda")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Dessa forma, podemos observar o efeito Doppler com a luz, que também é uma onda")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Para esse caso, o fenômeno do efeito Doppler manifesta-se na mudança de cor que é percebida pelo observador. Uma pessoa que se aproxima de um sinal de trânsito que está vermelho, por exemplo, percebe a coloração vermelha mais intensa se ela estiver parada, pois a frequência de onda luminosa é maior do que quando o observador está em movimento")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        "O uso efeito Doppler está na possibilidade de medir a velocidade de objetos por meio de ondas que são emitidas por aparelhos baseados em radiofrequência ou lasers, como os radares")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Na Astronomia, esse fenômeno é usado para medir a velocidade relativa das estrelas e de outros objetos celestes em relação ao planeta Terra")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Na medicina, o efeito Doppler é utilizado nos exames de ecocardiograma para medir a direção e a velocidade do fluxo sanguíneo ou do tecido cardíaco")

                    engine.runAndWait()
                    engine.stop()
                    print("vamos ver como é, por meio de uma ilustração.")
                    engine.say("vamos ver como é, por meio de uma ilustração.")
                    engine.runAndWait()
                    engine.stop()
                    webbrowser.open(
                        "https://www.infoescola.com/wp-content/uploads/2007/11/efeito-doppler-658148101.jpg")
                    print(
                        "Isso é em ondas mecâncias, logo conforme a fonte de som ou luz se aproxima, a frequência percebida aumenta e ao se afastar do observador, a frequência diminui")
                    print(
                        " Quando ela aproxima-se do observador, o som é mais agudo e, quando a ambulância afasta-se, o som é mais grave")
                    engine.say(
                        "Isso é em ondas mecâncias, logo conforme a fonte de som ou luz se aproxima, a frequência percebida aumenta e ao se afastar do observador, a frequência diminui")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        " Quando ela aproxima-se do observador, o som é mais agudo e, quando a ambulância afasta-se, o som é mais grave")
                    engine.runAndWait()
                    engine.stop()
                    webbrowser.open(
                        "https://fisicaevestibular.com.br/novo/wp-content/uploads/migracao/ondulatoria/doppler/i_2920a23e17065423_html_9db6fb76.png")
                    print(
                        "Assim, a frequência da luz aumenta  quando a distância da fonte estiver diminuindo ao observador, sendo assim a cor da luz tende para o azul. Quando diminuia distância observador-fonte estiver aumentando.a cor da luz tende para o vermelho.")
                    engine.say(
                        "Assim, a frequência da luz aumenta  quando a distância da fonte estiver diminuindo ao observador, sendo assim a cor da luz tende para o azul. Quando diminuia distância observador-fonte estiver aumentando.a cor da luz tende para o vermelho.")
                    engine.runAndWait()
                    engine.stop()
                    print("Vamos ver tal fórmula:")
                    print("Fo: (V +- Vo/ V -+ Vf).Ff")
                    print(
                        "*Sendo o sinal negativo utilizado no caso onde a fonte se aproxima e positivo no caso em que a fonte se afasta.")
                    print("Fo: frequência  aparente percebida pelo observador.")
                    print("Ff: frequência real emitida.")
                    print("Vo: velocidade do observador.")
                    print("Vf: velocidade da fonte.")
                    print("V : velocidade da onda sonora.")
                    engine.say("Vamos ver tal fórmula:")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Fo: (V +- Vo/ V -+ Vf).Ff")
                    engine.runAndWait()
                    engine.stop()
                    engine.say(
                        "*Sendo o sinal negativo utilizado no caso onde a fonte se aproxima e positivo no caso em que a fonte se afasta.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Fo: frequência  aparente percebida pelo observador.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Ff: frequência real emitida.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Vo: velocidade do observador.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Vf: velocidade da fonte.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("V : velocidade da onda sonora.")
                    engine.runAndWait()
                    engine.stop()
                    respq5 = 0
                    while respq5 != 1.100:

                        engine.say(
                            "Uma pessoa parada na beira de uma estrada vê um automóvel aproximar-se com velocidade 0,1 da velocidade do som no ar. O automóvel está buzinando, e a sua buzina, por especificação do fabricante, emite um som puro de 990 Hz.")
                        engine.runAndWait()
                        engine.stop()
                        engine.say("O som ouvido pelo observador terá uma frequência de:...?")
                        engine.runAndWait()
                        engine.stop()
                        resp = int(input(
                            "Uma pessoa parada na beira de uma estrada vê um automóvel aproximar-se com velocidade 0,1 da velocidade do som no ar. O automóvel está buzinando, e a sua buzina, por especificação do fabricante, emite um som puro de 990 Hz."
                            "O som ouvido pelo observador terá uma frequência de:...?"))
                        if respq5 == 1.100:
                            print("Você acertou")
                        else:
                            print("Você errou...Tente novamente")
                    print("Terminamos essa parte do curso")
                    engine.say("Terminamos essa parte do curso")
                    engine.runAndWait()
                    engine.stop()
                    menu()
                if astc == "n":
                    print("Tudo bem...Vou te redicionar para os temas")
                    engine.say("Tudo bem...Vou te redicionar para os temas")
                    engine.runAndWait()
                    engine.stop()
                    menu()
                else:
                    print("Opção não aceitável")
                    engine.say("Opção não aceitável")
                    engine.runAndWait()
                    engine.stop()



        if mat == 5:
            print("Estrelas e suas maravilhas")
            engine.say("Estrelas e suas maravilhas")
            engine.runAndWait()
            engine.stop()
            engine.runAndWait()
            engine.stop()
            engine.say("Quer continuar?(use s para sim e n para não")
            engine.runAndWait()
            engine.stop()
            astc = input("Quer continuar?(use 's' para sim e 'n' para não")
            if astc == "s":
                print(
                    "Estrelas são imensas esferas de gás constituídas basicamente de hidrogênio e hélio. Elas brilham porque produzem energia através de reações nucleares,pois sua forte gravidade faz com que os átomos se uniem e matém uma forma quase esférica.")
                engine.say(
                    "Estrelas são imensas esferas de gás constituídas basicamente de hidrogênio e hélio. Elas brilham porque produzem energia através de reações nucleares,pois sua forte gravidade faz com que os átomos se uniem e matém uma forma quase esférica.")
                engine.runAndWait()
                engine.stop()
                print(
                    "As nebulosas ou nuvens moleculares são grandes aglomerados de gás e de poeiras existentes na galáxia, onde se formam as estrelas. Assim como as galáxias em geral, as nuvens moleculares são feitas quase que inteiramente de hidrogênio e hélio. Turbulências, como as causadas por uma explosão de supernovas nas proximidades, provocam crescentes adensamentos em algumas regiões da nebulosa formando glóbulos de gás frio que acabam colapsando sob seu próprio peso. Cada glóbulo dará origem a uma estrela.")
                print(
                    "À medida que o glóbulo colapsa, forma-se um disco em rotação com a protoestrela no centro; jatos bipolares de gás e poeira são gerados pelo disco rotante e pelo vento estelar da protoestrela. A pressão no centro da estrela aumenta até o ponto em que ela balança a força gravitacional, alcançando o equilíbrio hidrostático que faz parar o colapso.")
                print(
                    "No interior da protoestrela o núcleo continua aglomerando matéria das camadas externas a ele, ficando mais denso e mais quente. Quando a temperatura do núcleo fica alta o suficiente para iniciar as reações termonucleares a protoestrela passa a ser chamada de estrela, iniciando a fase de sua vida chamada sequência principal.")
                print(
                    "(Importante: A massa mínima que a protoestrela precisa ter para seu núcleo atingir a temperatura alta o suficiente para acender as reações nucleares e formar uma estrela é de aproximadamente 10% da massa do Sol. Se a massa for menor do que isso ela será uma anã marrom, objeto com massa maior do que a de um planeta, porém menor do que a de uma estrela, não podendo manter fusão termonuclear.)")

                engine.say(
                    "As nebulosas ou nuvens moleculares são grandes aglomerados de gás e de poeiras existentes na galáxia, onde se formam as estrelas ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Assim como as galáxias em geral, as nuvens moleculares são feitas quase que inteiramente de hidrogênio e hélio")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Turbulências, como as causadas por uma explosão de supernovas nas proximidades, provocam crescentes adensamentos em algumas regiões da nebulosa formando glóbulos de gás frio que acabam colapsando sob seu próprio peso")
                engine.runAndWait()
                engine.stop()
                engine.say(" Cada glóbulo dará origem a uma estrela")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "À medida que o glóbulo colapsa, forma-se um disco em rotação com a protoestrela no centro; jatos bipolares de gás e poeira são gerados pelo disco rotante e pelo vento estelar da protoestrela. A pressão no centro da estrela aumenta até o ponto em que ela balança a força gravitacional, alcançando o equilíbrio hidrostático que faz parar o colapso")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "No interior da protoestrela o núcleo continua aglomerando matéria das camadas externas a ele, ficando mais denso e mais quente")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Quando a temperatura do núcleo fica alta o suficiente para iniciar as reações termonucleares a protoestrela passa a ser chamada de estrela, iniciando a fase de sua vida chamada sequência principal")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Importante A massa mínima que a protoestrela precisa ter para seu núcleo atingir a temperatura alta o suficiente para acender as reações nucleares e formar uma estrela é de aproximadamente 10% da massa do Sol")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Se a massa for menor do que isso ela será uma anã marrom, objeto com massa maior do que a de um planeta, porém menor do que a de uma estrela, não podendo manter fusão termonuclear")
                print("Vou mostrar uma nebulosa, precisamente a nebulosa Carina")
                engine.say("Vou mostrar uma nebulosa, precisamente a nebulosa Carina")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://cdnbr3.img.sputniknews.com/img/1558/63/15586382_0:70:1280:762_1000x541_80_0_0_7ea78322e49b843e536d11519ac7e7a1.jpg")
                print("Bonita, não é mesmo?")
                engine.say("Bonita, não é mesmo?")
                engine.runAndWait()
                engine.stop()
                print("Vou mostrar uma prtoestrela.")
                engine.say("Vou mostrar uma prtoestrela")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Protostar_Herbig-Haro_46_47.jpg")
                print("A protoestrela é aquela 'mancha' verde.")
                engine.say("A protoestrela é aquela 'mancha' verde")
                engine.runAndWait()
                engine.stop()
                print(
                    "última foto que quero mostra, nessa parte do curso, é o conceito artístico de uma estrela anã marrom. ")
                engine.say(
                    "última foto que quero mostra, nessa parte do curso, é o conceito artístico de uma estrela anã marrom")

                webbrowser.open(
                    "https://upload.wikimedia.org/wikipedia/commons/e/e0/Artist%E2%80%99s_conception_of_a_brown_dwarf_like_2MASSJ22282889-431026.jpg")
                print("Voltndo ao curso.")
                engine.say("Voltndo ao curso")
                engine.runAndWait()
                engine.stop()
                print("Estágio Intermediário – vida de uma estrela")
                engine.say("Estágio Intermediário – vida de uma estrela")
                engine.runAndWait()
                engine.stop()
                print(
                    "A sequência principal é etapa mais longa da vida da estrela, quando ela está fundindo hidrogênio em hélio no núcleo e brilhando estavelmente, em equilíbrio hidrostático. Durante esse tempo as estrelas mantêm uma relação homogênea entre a luminosidade e a temperatura, determinada pela sua massa. As estrelas mais quentes (mais massivas) são as mais luminosas e as mais frias (as menos massivas) são menos luminosas.")
                print(
                    "A massa de uma estrela define a sua temperatura, a sua cor, o seu tamanho, a sua luminosidade e o seu tempo de vida na sequência principal. Quanto maior a massa, mais quente, mais azul e mais luminosa será a estrela, e menor será o seu tempo de vida.")
                print(
                    "Quando as estrelas consomem o hidrogênio no núcleo, que corresponde a aproximadamente 10% da sua massa total, elas saem da sequência principal. A geração de energia passa a se dar, então, em uma camada externa a este núcleo, onde a temperatura e a densidade são suficientes para continuar mantendo as reações nucleares. Como nenhuma energia é gerada no núcleo nesta fase, ele se contrai rapidamente, e a luminosidade da estrela aumenta um pouco. As camadas externas se reajustam ao aumento de luminosidade expandindo-se e como a área superficial aumenta, sua temperatura diminui. Desta forma, a luminosidade aumenta e a estrela torna-se mais vermelha, tornando-se uma gigante vermelha.")
                print(
                    "(Curiosidade: Quando o Sol atingir essa fase, daqui a 5 bilhões de anos, engolirá Mercúrio, Vênus e a Terra, chegando próximo à órbita de Marte.)")

                engine.say(
                    "A sequência principal é etapa mais longa da vida da estrela, quando ela está fundindo hidrogênio em hélio no núcleo e brilhando estavelmente, em equilíbrio hidrostático")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Durante esse tempo as estrelas mantêm uma relação homogênea entre a luminosidade e a temperatura, determinada pela sua massa")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " As estrelas mais quentes (mais massivas) são as mais luminosas e as mais frias (as menos massivas) são menos luminosas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A massa de uma estrela define a sua temperatura, a sua cor, o seu tamanho, a sua luminosidade e o seu tempo de vida na sequência principal")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Quanto maior a massa, mais quente, mais azul e mais luminosa será a estrela, e menor será o seu tempo de vida")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Quando as estrelas consomem o hidrogênio no núcleo, que corresponde a aproximadamente 10% da sua massa total, elas saem da sequência principal")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " A geração de energia passa a se dar, então, em uma camada externa a este núcleo, onde a temperatura e a densidade são suficientes para continuar mantendo as reações nucleares")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Como nenhuma energia é gerada no núcleo nesta fase, ele se contrai rapidamente, e a luminosidade da estrela aumenta um pouco. As camadas externas se reajustam ao aumento de luminosidade expandindo-se  como a área superficial aumenta, sua temperatura diminui")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Desta forma, a luminosidade aumenta e a estrela torna-se mais vermelha, tornando-se uma gigante vermelha")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Curiosidade Quando o Sol atingir essa fase, daqui a 5 bilhões de anos, engolirá Mercúrio, Vênus e a Terra, chegando próximo à órbita de Marte")

                print('Vou mostrar como é uma estrela, anã amarela, no estágio intermediário')
                engine.runAndWait()
                engine.stop()
                engine.say(
                    'Vou mostrar como é uma estrela, anã amarela, no estágio intermediário')
                webbrowser.open(
                    "https://qph.fs.quoracdn.net/main-qimg-9cf08b6bec033e140dfbc7d87a72324f")
                print("Estágio Final – morte de uma estrela")
                engine.say("Estágio Final – morte de uma estrela")
                engine.runAndWait()
                engine.stop()
                print(
                    "A morte de uma estrela vai depender de sua massa. Se ela tiver menos de dez vezes a massa do Sol, quando tiver “queimado” todo o hélio do núcleo ela ejetará uma nebulosa planetária (sim, aquela lá do inicio, que começou essa história toda) e o núcleo remanescente será uma Anã Branca. As Anãs Brancas podem ter tamanhos comparáveis aos da Terra, porém com massas próximas às do Sol. Uma anã branca é, portanto, o núcleo daquilo que era uma estrela gigante vermelha.")
                engine.runAndWait()
                engine.stop()
                print(
                    "Porém, se a estrela tiver uma massa maior que dez vezes a do Sol, ela terá uma morte catastrófica. Sem produção de energia, a pressão cai bruscamente e as camadas externas começam a despencar em direção ao centro da estrela, ali encontram-se com o núcleo sólido de ferro e quicam, sendo ejetadas para o espaço a altas velocidades: É o que chamamos de Supernova.")
                print(
                    "Uma supernova, ao contrário do que o nome parece indicar, não é uma estrela nova, mas sim uma explosão espetacular de uma estrela que terminou a sua vida. Esta explosão espalha os elementos constituintes da estrela pelo espaço, ao mesmo tempo que permite a formação de elementos mais pesados que o ferro. Estes elementos serão depois a semente de formação de mais estrelas em algum lugar na imensidão do espaço, completando, assim, um grande ciclo cósmico.")
                print(
                    "O destino do núcleo que sobra após a explosão da supernova é, novamente, ditado pela massa. Estrelas muito pequenas e extremamente densas que são fontes pulsantes de ondas de rádio, formam uma estrela de nêutrons. As estrelas com massa muito maior que a do Sol, após a fase das supernovas, originam buracos negros, objetos tão densos que atraem tudo, incluindo a própria luz.")
                engine.say(
                    "A morte de uma estrela vai depender de sua massa. Se ela tiver menos de dez vezes a massa do Sol, quando tiver “queimado” todo o hélio do núcleo ela ejetará uma nebulosa planetária (sim, aquela lá do inicio, que começou essa história toda) e o núcleo remanescente será uma Anã Branca. As Anãs Brancas podem ter tamanhos comparáveis aos da Terra, porém com massas próximas às do Sol. Uma anã branca é, portanto, o núcleo daquilo que era uma estrela gigante vermelha.")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Porém, se a estrela tiver uma massa maior que dez vezes a do Sol, ela terá uma morte catastrófica. Sem produção de energia, a pressão cai bruscamente e as camadas externas começam a despencar em direção ao centro da estrela, ali encontram-se com o núcleo sólido de ferro e quicam, sendo ejetadas para o espaço a altas velocidades: É o que chamamos de Supernova.")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Uma supernova, ao contrário do que o nome parece indicar, não é uma estrela nova, mas sim uma explosão espetacular de uma estrela que terminou a sua vida. Esta explosão espalha os elementos constituintes da estrela pelo espaço, ao mesmo tempo que permite a formação de elementos mais pesados que o ferro. Estes elementos serão depois a semente de formação de mais estrelas em algum lugar na imensidão do espaço, completando, assim, um grande ciclo cósmico.")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O destino do núcleo que sobra após a explosão da supernova é, novamente, ditado pela massa. Estrelas muito pequenas e extremamente densas que são fontes pulsantes de ondas de rádio, formam uma estrela de nêutrons. As estrelas com massa muito maior que a do Sol, após a fase das supernovas, originam buracos negros, objetos tão densos que atraem tudo, incluindo a própria luz.")
                engine.runAndWait()
                engine.stop()
                print("Vamos ver outras  fotos dessas maravilhas astronômicas")
                engine.say(
                    "Vamos ver outras  fotos dessas maravilhas astronômicas, começando pela supernova")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://www.revistaplaneta.com.br/wp-content/uploads/sites/3/2019/10/supernova.jpg")
                print(
                    "Em seguida, uma estrela de nêtrons e  a imagem de um buraco,mas tal imagem é uma concepção artística feita com base de uma foto, que também aparecerá aqui")
                engine.say(
                    "Em seguida, uma estrela de nêtrons e  a imagem de um buraco,mas tal imagem é uma concepção artística feita com base de uma foto, que também aparecerá aqui")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Vela_Pulsar_jet_seen_by_Chandra_Observatory.ogv/258px--Vela_Pulsar_jet_seen_by_Chandra_Observatory.ogv.jpg")
                print("A ilustração")
                engine.say("A ilustração")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8QEg8PDw8PDQ8NDQ0NDQ0NDw8NDQ0NFREWFhURExUYHSggGBolGxUVITEhJSkrLjAuFx8zODMsNygtLisBCgoKDg0OFxAQGC0dHR0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSstKy0tLSstLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALgBEgMBEQACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAAAQIDBAcIBgX/xAA8EAACAQMABgcFBgYCAwAAAAAAAQIDBBEFBhIhMUEiNFFhcXSzEzJSgZEHFCMzQnJiobHB0fBj4RWCkv/EABoBAQADAQEBAAAAAAAAAAAAAAABAgMEBQb/xAApEQEAAgICAgEEAgMAAwAAAAAAAQIDEQQSITFBBRMiUTJhFHGRNKHh/9oADAMBAAIRAxEAPwDRoAAAAAAAADSCdGQtoNgmUSVAAwAhIAAAGgDQwDQBoAASAgEoIAAAAAAAAAAAADofVfqVj5K19KIHPAAAAAAAANIJiDZC0gBMlEkFTCQQkYAeAaGAnRqITFT2SE9SwTtGhgGiwEaGAjREqgBAAAAAAAAAAAAAdD6r9SsfJWvpRA54AAAAAAGBJENIjwTCsgJDCJNRCeowE6GAjRqJG1oqmqbI7Na4plNUyNtIxHsEbT9tCUWW2ytWUNlk7hTpYtljcKzW0FvJV1JBAyDZEoAQQAAAAAAAAAAAdD6r9SsfJWvpRA54AAABgICUQtEJMqtPpFEoiPKTRC0wlCBEyvXH8mxCZRxklXW5W06LZSbab0wTK9UVHiU7bdUYYpH5I737qJ8R7U/K38IXQtG97ZWckfDopw7T5sujQj2N+BTvLpjBSPjYdNfCOxOOsfCuUV2InbK1Y/SuUe5FoY2rE/CqUF2F4lhbHCmUC0S5rY1UololhaqJKmgSggAAAAAAAAAAA6H1X6lY+StfSiBzwAAAAAATRDSDZCZ9HBCU1hOMcldta03K+UcIpvcuq1elWPjJp6cmptOoZVC3MrX07sHFmWc6Sgu98jDt2l6cY4x1VwtnN5fAv3irCOPOSdy+rozQ9Sr+XDorjVlugvnzZy5uRWn8pdlMMVjwzLrR1GgunL2k+zkvkY0z3yeo1DSaRHtgSoVanuQljuWEdHetfcs5ifhVPRlRe9KEfGSyWjNWfTOcNp+WPO0/5IvwyXi/9KTx5/bHnb/xJmkXYW48/tTOlJF4tDmvivVS32otDnmZj3CLSZb0ztEWVSgWiWFqaVtFmUwAggAAAAAAAAADofVfqVj5K19KIHPAAAwAACdLEirWIJhEpwREy1pVl2tPJle2nfxsW52V1xwhT0jk+Z1Cdrb5IvfS/G42/Mvq2tDOcLdHi+/sOTJd61KREeGZ/wCNk+lJPL4LsMvvx6Xmvy9jq7qHKUVWuk4U/ehQ4SqL4pv9K7jj5HN6+Ke3NfPXt1qyNM3SWKFvFRS6CUI/yhFHHhrNp73nbqr4jcsW31WlFe0uNmjnf+J+JVfhDl8za/KiPEM/uxadV8sXSFShTWEpTx+qtPZj8orcWxxkvLX081eX0H7uwv2QTPQx4pj2pN4fMqyT4t//ADg6YY2tDHnHs/waQ57Rv0qbaLeGFrWhCU88UWiGVrxPuFM6fNF4lzXx/NVWe0sxmfiUZImGdoVksiJQAAAAAAAAAOh9V+pWPkrX0ogc8AADCQEGiFo9rEireI2XMlX5XRRSXRWrPoLCMLeZetgr1qgqeWT21DOMXe76EKLWzCKzOo0ljjvMJt7tPqHdFesREPZaD0JlqOM7GFj4qj5nkcnk/wDttEREblsnVzVGnBxq1Yqc+MIy4J/EznpF7y8jmc7e6UfR0zaVa79jR6FNfmVXzfcZWru2oZcbJTFHe/mWEtG29jFygk6jW+vNZl/6i951pvXJfk28+I/Tyd596vJuNvFpN4lWnl/TtLYq0r+V/P8AT0u1MNdenmtMUNHWbarTlf3C96EZ9CL7JNbl4Hp44z5f4/jCn3Y9y8xd6yy3qlSo28eSp04t4/c8s7sfE1/KZmXNfmVj0+ZV0xVfGcvrg6IwRDltzlDvW+Lz47y321P8vY9qmOq/3olFxzwJUmIn0rkiYY2iVUi8MbefaLRLKYVyRZlMIkqkEAAAAAAAAOh9V+pWPkrX0ogc8AADCQQQaCY9siEdxSZddI8IwW8mfSlI/JfRjl+BnMuvFXdmXS3mNvD0cXnwztF26nLHZvMc19Q6cVY3Mvt6qWnta9Sq1mNGL2exPtOPm5ft44rHuVscdrTZtz7PtFKUHWktzk9nPPvPOx4vuX3Pw8/6lyZp+FXvKdHi+1Y8Ee5x+Hqszb5eFayipBPd+mO997POzY481r6hesy89daOld1Hno0oPHYmcGPBfNk8enp4+RXj08fylrf7RNdoUdqw0fJRjDoV7mPGbXGEHyXaz1+PwqxO5a0rOvu5fc+oakuLltvvPWpSIcufkzLFlVNYq4bZZlDbJ0p3PaI0mLGpYGlotMLoVfqUmremXa5PPiV9OmJ7wqqQJrLHJRSmXc8T8FJEqTCtlmUgIIAAAAAAAOh9V+pWPkrX0ogc8AAAA0EwaITHtmUluMre3o4q/igljJLPrrbJt49HJnafOnbx66xzZk2Mc7T7mZZZ06+JG9yzLCtsOT/hZlkr206a/MPb6paPl926Pv3VSMIvufE8bmX7Z4j9LxMUrMt4aIso0aVKjFYUIxT79x3cSkTMV/6+V5GSb3m0vpHuzHjTmU1YbsLmebycH49K/PtpWfLxP2o6f+42bp0ns1blOmmnhxhza7+X1M4xxiiuOvuff+ndwcX3cne3qrmq+r5b8T0MdNQ05mfywG8m2nl2tMkSqQABJMhaJSIW9LqUytodWK/lfPtM4dd43G2LUiaw4MkaJBWPKE0WhleESVCAAAAAAADofVfqVj5K19KIHPAAAwAJhKJErV9s2jwMbPTw+hVjuYrPlOWuqzLIsI7UXHnjcZZZ1O3Tw/yxzV9TQlrte0XNI5uTkiNS6+NTrEww5pxck+3BtHmEzOplu7UK1UqVhLG5La+eGfOZv/In/bLlZNY7R/TY1jV2pVF8DSPV+mTvLb+ngZa6iGee65yZWYj5HPn22aSdS72M9GlDCXL/AHieXgt9zLe/96h9Dx6xi4v9y1HVlls9Wsah4WS3a0oEswAAADAkiGkekqbIlbHPlmN7kYvS34hTMvDmupiXc8exIFoVssxkggAAAAAAHQ+q/UrHyVr6UQOeAABhIAlAiV6e2XSZlaHoYpZE45izKJ1LsyV7Y5LR1XYnF8k1nwJzV7Vljw79balsHROjFirVp704KW7luPAz55nVJe5Gnm9YrLZxWgs06nHHKXNHpcXJv8J9w5uRExG4bi+yKsq1lBZ6dCbiu7B5fKxzGazzubbWp+JhsHR6XSlwbbUvFHd9Mr+c2eVm+IZx7rBXWeIyfZFv+RlmnrjtMfpavm0OZPtRbdxt/HSWf3RbTPI+l23Sf9vo+VHXBER+mvGe4+bn2QQAAAAaAlErLSpxCa+2TtbkZ6dvbxCE+JaGd58qmWYT7DBMoSJZWRJVAAAAAAB0Pqv1Kx8la+lEDngAAZCQBOlxIlpj9shGcuyviWbbvKwY28PTwTFq6UShh/M0idw5LU63bM+y7SClKpb1N6lDo5PB+pYorMXelNpmkTHwjeWEaNavZV/yLhuVCo+EJ9hWuSbUjJX+VfboiYvX/bP+zavW0ddSoVFmhWko7XJN8JGmbNTJ1yR7cfL4vbFMfpuxNQxJe7J7/nzOjFaMV4vX+MvnZ3Phlo9uJ2yKSK3r2rMEND/bFq+4zdSCzFuUsdmeOO48DhXjDltjl9Hin/I42vmGmqsGnhn0MTuHg5aTW0xKBLIgABgOKC9YTSKtIgkFY9rclW+/BVBCLz5hCRZnYmFZKRMK29IEqAAAAAAA6H1X6lY+StfSiBzwAAMhIJJSgyJWpOpZRm7vcbW0J4ZS8bdGDJqWRVSe8yidO3JWLRt9PVe+dGtGSeORz83F3xytxreestk3tWje08vDlFceaZ87WcmC7urTS/QS2cRq/iQWFt8ZRXeVy2ibbjwjLE9Z6tp6Pkp0o4kqkXHGVvyj1OLE3xTWPT5TNE1yeY1LMtnhY44+uD1OBlm1es/DC8Lmego89rXoeFzSlGSTwnjdnB839QxdcnekvR4PInFbz6lzzrZqfVoTk4xzHO5redfE+oVtERb29TkcWuaO1XjqtrKPFHrRkiXj5eJenwpdNltuecUwWwTtH25SjTI7LxiS2SNr9dEwrJRRKIjyl2EL+5g63EQZfEqyWfsMIlFkqSiSqAAAAAADofVfqVj5K19KIHPAAAyEmEkiUemTRlncZ2jTtw23Gkk8MrrcLRbrLKhPKMph348m6rLaolJPg00Reu6tMV47eXo3dVbecZrLp1En3HnfaplrqfcPRmZh9G01mlQmpPp0p793FM578GMlfHiYJt+3vdXtPv8AOs6sZReHWt5PovvS/Szjrky8S3mNTDk5HGpmjUveaM1gpVXFSTpSnhLa3xcvhz2nscT6jiyW/KOtnicjhXxf3D7Z7DhfI0xUcE3htPs4r6HzX1HdMk79S7ONTtLXWsUvabWxNZ+GTT/kzy8UxFvT6XjxqumstMaNq7TbpxffE+gwZ6a9rZKb+HwK1q1xWDurkefk4+5Y7pYNOzlnDpXKJO2VqxCqTLxDntZDGSWcVmT4BbWkqSy8kT4Tijc7QqvLJhTL5siSqQVJkqyiSqAAAAAADofVfqVj5K19KIHPAABJoheYIlUyEpw3ES0p4ldLfvKQ6bflGyhNoTCtckwn7T5MjTX7vy9XoLTFGpT+7XO5L8up8Pczy+Tx70t9zF/x7HF5Vbx1t7Z89AqSapTjPO/Zzv8AFdphXlzHm0adc13Gnyo0ruyqKcNuOHxWcNdjOnvh5FdT5c/W9J8eYe61Y14i5R9ovZzWG0/ck1/Rnk5+DfFPanmE5KVy103PorSNO4pxqQaaaWcNPDPd43LjLTc+JfM58FsV+ssTWGjOdOUqUmqlJNuC37a5rBx/UafdruP5Va8O9aXjt6lqXTmmoSzGWFJccxa3nk4ePeZ7PqKxFY8PE6RrRlwf0lj+x7OKsx7gs+LVf+5OuHLk8MWpUNoq4cmSWPLLNIcdtySh2jasUj5RlJExCtrRHpVvZb0w3Np0yEsIpPmXVEdaqWWc8oslSQDSDJZyRKAAAAAAAdD6r9SsfJWvpRA54AALEVbR5gpRJ2rNUSWaUWVlpWV0JFZh0UslKHNERK9qfMIOJO2c12UW0yfCsTak7h9Sz0nNYTk1j3Wnhx8DmyYInzp63H53xZ9+11lqJbNTFSPDPP5nBk4Nd7r4ejXN+znf0JPaUI58MERiyRGttItX4e21D1yp0JqnJuMJ7sN5T7vE5bY8uG3ePMfLm5fGjPT+21Z3CqxjOjNbbX4U37lT/jn2MvfLGasTE/lDwIpOO3W8NV6+W+06lSFFxqx31rfH4kVzqRX64963rvW8y49Z76mdPd42TVNTO4/bVlzdZfD6Hs0x6MnI18MOpVNoq4b5tqZVC8Q5rZYQ9oT1Z/dQlItEM7XlBJsncQyis2llU6SjvZnNtu3HiikblXUkTEM8lvKtl2MygGZhKDLM5IIAAAAAAB0Pqv1Kx8la+lEDngAAaYTErYvJRvE7KVMmJRbGhjBLPUwkmRpeLLqcykw6Md1rhneiu2844nzCtxLbZTVHYJ2pNFtOs4+BWaxLbHmtRmUqsXzwY2rMPSxZqX+V8Hjw7uJnMOqHu9Udd3b4pVp7VN7sy3pr+L/J5fI4dt9sf/Fc2GmWPPt7+tfW95BZarJb6coz2bmi/wCCfP8Ar4nD921fFo8uKuC+KfH/AMeC1m1SVRudOUJy5tJUKz/fB4jJ9+YvxPQ4/OiPFpdWu8a1p4S/0DcU2805NduzJL6vd9D1aZ6Wj24svGv8PmOzqfBL6M2jJX9uScF/0PuVTnFr93R/qT3hH+Pf9BWna/p/kj7i9eJM+1mwoldzLeKVxwoqzyXiHLlvtSy7nlCTJhnaUSVdmwIEqAAAAAAAAOh9V+pWPkrX0ogc8AAAA0yExK2Mysw3pdPCZHmGsxFkZUyYlnOLSOMEqamFlOs0VmramaY9shVEzPUw64yVsHFDaekBRXMbk6Vn2i6XYye37U+zrzWUlOS5kaheMl6/KyN1JdhWaQ1jlWj2zbHTNWk806jj3cjHJxqX/lG21OZL0NtrzXSSqxjVXf8A2OG/0uk/xnToryqHW1roz40XFvnCeCK8G9fVmv8Ak45fNutLUpcI1PnU/wCjqphtHuUTno+ZVuYco/V5ZvFJYWz0hi1bj5GkUcuTkfpjTqNmkVcV8kyrbLMZlW5FtMZttFslSZCBBMImSJQAAAAAAAA6H1X6lY+StfSiBzwAAADAaZCYlKMiJhrW2lkZlZhrXJ+000yPLTdZJ0ydonHtFwZO2c45j0cZtETELRkvVNVc8SvVrGXftJPsZC+4+JDTJJiUXEbUmslsk7V6yabXMeExNoP2jI0t9yQ6zHU+9KLm2TqFe1pJhWf7RciYhSbaVyZaIY2shklTYCADYJQQAAAAAAAAHQ+q/UrHyVr6UQOeAAAAAGQmDyEmmFolIhZJTZGl4vMJqoRprGXZ5RC24kmgrNYIlU8saT2kbbI0nvI2mNHaSywjyMEmjIT4gnInSJshKZOmU3VtltMpkiVQEAAAAEAAAAAAAAB0Pqv1Kx8la+lEDngAAAGAABCUkFoNMhaJMLABhMGmRpaLHkaTs9ojSe0DaGk94G0NHctoaR3JzJ0r3RyFNk2W0rMyi2SzmSCAAgABgIAAAAAAAAAA6H1X6lY+StfSiBzwAAAAAAMATCdmmRpOzyNLbPJGk7PIW2AjYyDYyDYyE7GQjZZGkbLJOkbLI0rsmyUbAQQAAAAAAAAAAAAAAAAHQ+q/UrHyVr6UQOeAAAAAAAAAAAAeQbGQnYyNJ7HtEaOwyNHYZB2LJKNgIIBgACAAAAAAAAAAAAAAAAAAOh9V+pWPkrX0ogf/2Q==")
                print("A foto ")
                engine.say("A foto ")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://s2.glbimg.com/p_jOM-508TmG6V_TzLz8cuzv_Og=/696x390/smart/filters:cover():strip_icc()/s02.video.glbimg.com/x720/7533957.jpg")
                print("Terminamos essa parte do curso")
                engine.say("Terminamos essa parte do curso")
                engine.runAndWait()
                engine.stop()
                menu()

            if astc == "n":
                print("Tudo bem...Vou te redicionar para os temas")
                engine.say("Tudo bem...Vou te redicionar para os temas")
                engine.runAndWait()
                engine.stop()
                menu()
            else:
                print("Opção não aceitável")
                engine.say("Opção não aceitável")
                engine.runAndWait()
                engine.stop()

        if mat == 6:
            print("Planetas,exoplanetas e os seus satélites")
            engine.say("Planetas,exoplanetas e os seus satélites")
            engine.say("Quer continuar?(use s para sim e n para não")
            engine.runAndWait()
            engine.stop()
            astc = input("Quer continuar?(use 's' para sim e 'n' para não")
            if astc == "s":
                engine.runAndWait()
                engine.stop()
                engine.runAndWait()
                engine.stop()
                engine.say("Quer continuar?(use s para sim e n para não")
                engine.runAndWait()
                engine.stop()
                astc = input("Quer continuar?(use 's' para sim e 'n' para não")
                if astc == "s":
                    print(
                        "Estrelas são imensas esferas de gás constituídas basicamente de hidrogênio e hélio. Elas brilham porque produzem energia através de reações nucleares,pois sua forte gravidade faz com que os átomos se uniem e matém uma forma quase esférica.")
                    engine.say(
                        "Estrelas são imensas esferas de gás constituídas basicamente de hidrogênio e hélio. Elas brilham porque produzem energia através de reações nucleares,pois sua forte gravidade faz com que os átomos se uniem e matém uma forma quase esférica.")
                    engine.runAndWait()
                    engine.stop()
                print(
                    "Os Planetas são corpos celestes sem luz e calor próprios, sólidos, arredondados e com gravidade própria, os quais giram em torno de uma estrela maior (órbita livre), que no caso do planeta Terra é o Sol. ")
                print(
                    "Como todos os demais corpos, os planetas e as estrelas atraem outros corpos para junto de si. O Sol, ao seguir sua órbita no espaço, atrai planetas que giram ao seu redor, enquanto os planetas atraem os seus respectivos satélites.")
                print(
                    "A velocidade com que os satélites giram em torno de seu planeta e os planetas ao redor do Sol, lhe confere uma força centrífuga, que os impulsiona para fora de sua órbita, essa força neutraliza a da gravidade que os atrai em direção ao Sol.")
                print(
                    "Como duas forças contrárias se anulam, os planetas e os satélites se mantêm numa órbita constante.Exoplanetas são planetas que orbitam em torno de outras estrelas, que não o Sol. Exoplanetas são muito difíceis de ver diretamente com telescópios, pois estão ocultos pelo brilho das estrelas que orbitam.")
                engine.say(
                    "Os Planetas são corpos celestes sem luz e calor próprios, sólidos, arredondados e com gravidade própria, os quais giram em torno de uma estrela maior (órbita livre), que no caso do planeta Terra é o Sol ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Como todos os demais corpos, os planetas e as estrelas atraem outros corpos para junto de si")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " O Sol, ao seguir sua órbita no espaço, atrai planetas que giram ao seu redor, enquanto os planetas atraem os seus respectivos satélites")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A velocidade com que os satélites giram em torno de seu planeta e os planetas ao redor do Sol, lhe confere uma força centrífuga, que os impulsiona para fora de sua órbita, essa força neutraliza a da gravidade que os atrai em direção ao Sol")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Como duas forças contrárias se anulam, os planetas e os satélites se mantêm numa órbita constante")
                engine.runAndWait()
                engine.stop()

                print("Por que Plutão não é mais considerado um planeta?")
                print(
                    "De acordo com a União Astronômica Internacional (IAU, na sigla em inglês), para um corpo celeste ser classificado como um planeta, ele precisa atender a três requisitos principais. Em primeiro lugar, precisa estar em uma órbita em torno do Sol, em segundo lugar, deve ter gravidade suficiente para puxar-se em uma forma esférica, e em terceiro lugar, ele precisa ter “limpado a vizinhança” da sua órbita.")
                print(
                    "Plutão orbita o Sol e também é de forma esférica, encaixando dois requisitos. No entanto, o planeta anão começa a ter problemas quando os astrônomos olham para a regra final.")
                print(
                    "Plutão — que era conhecido como o nono planeta do nosso Sistema Solar desde sua descoberta em 1930 pelo astrônomo americano Clyde Tombaugh até a sua desclassificação para planeta anão em 2006 — não limpa a sua vizinhança. Ou seja, o planeta anão é incapaz de consumir corpos menores ou jogá-los para longe usando sua gravidade.")

                engine.say("Por que Plutão não é mais considerado um planeta?")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "De acordo com a União Astronômica Internacional (IAU, na sigla em inglês), para um corpo celeste ser classificado como um planeta, ele precisa atender a três requisitos principais")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Em primeiro lugar, precisa estar em uma órbita em torno do Sol, em segundo lugar, deve ter gravidade suficiente para puxar-se em uma forma esférica, e em terceiro lugar, ele precisa ter 'limpado a vizinhança' da sua órbita")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Plutão orbita o Sol e também é de forma esférica, encaixando dois requisitos")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " No entanto, o planeta anão começa a ter problemas quando os astrônomos olham para a regra final")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Plutão — que era conhecido como o nono planeta do nosso Sistema Solar desde sua descoberta em 1930 pelo astrônomo americano Clyde Tombaugh até a sua desclassificação para planeta anão em 2006 — não limpa a sua vizinhança")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Ou seja, o planeta anão é incapaz de consumir corpos menores ou jogá-los para longe usando sua gravidade")
                engine.runAndWait()
                engine.stop()

                print(
                    "Exoplanetas são planetas que orbitam em torno de outras estrelas, que não o Sol. Exoplanetas são muito difíceis de ver diretamente com telescópios, pois estão ocultos pelo brilho das estrelas que orbitam.")
                print(
                    "Assim, os astrônomos usam outras maneiras de detectar e estudar esses planetas distantes. Eles procuram exoplanetas observando os efeitos que esses planetas têm sobre as estrelas que orbitam.")
                engine.say(
                    "Exoplanetas são planetas que orbitam em torno de outras estrelas, que não o Sol")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Exoplanetas são muito difíceis de ver diretamente com telescópios, pois estão ocultos pelo brilho das estrelas que orbitam")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Assim, os astrônomos usam outras maneiras de detectar e estudar esses planetas distantes")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Eles procuram exoplanetas observando os efeitos que esses planetas têm sobre as estrelas que orbitam")
                engine.runAndWait()
                engine.stop()
                print("Como estudiosos procuram exoplanetas?")
                engine.say("Como estudiosos procuram exoplanetas?")
                engine.runAndWait()
                engine.stop()
                print(
                    "Uma maneira de encontrar exoplanetas é procurar por estrelas “vacilantes”. Uma estrela que tem planetas não orbita perfeitamente em torno de seu centro. Dessa forma, de longe, essa órbita descentralizada faz com que a estrela pareça trêmula.")
                print(
                    "Centenas de planetas foram descobertos usando esse método. No entanto, apenas grandes planetas – como Júpiter, ou até maiores – podem ser vistos dessa maneira. Planetas menores, como a Terra, são muito mais difíceis de encontrar, porque criam apenas pequenas oscilações, mais difíceis de detectar.")
                print("Método de trânsito:")
                print(
                    "Em 2009, a NASA lançou uma espaçonave chamada Kepler para procurar exoplanetas. Kepler procurou planetas em uma ampla variedade de tamanhos e órbitas. Além disso,  esses planetas orbitam em torno de estrelas que variam de tamanho e temperatura.")
                print(
                    "Alguns dos planetas descobertos por Kepler são planetas rochosos, como a Terra, inclusive com zonas habitáveis, onde a vida pode ser possível. Contudo, o mais próximo deles se encontra a cerca de 12 anos-luz de distância do nosso planeta.")
                print(
                    "Os exoplanetas foram detectados usando o chamado método de trânsito. Dessa forma, quando um planeta passa na frente de sua estrela, isso é chamado de trânsito. À medida que o planeta transita diante da estrela, ele bloqueia um pouco da luz da mesma. Isso significa que uma estrela parecerá um pouco menos brilhante quando o planeta passar à sua frente.")
                print(
                    "Os astrônomos também podem observar como o brilho da estrela muda durante um trânsito, o que  pode ajudar a descobrir o tamanho do planeta. Assim, estudando o tempo entre trânsitos, os astrônomos também podem descobrir a que distância o planeta está de sua estrela.")
                print(
                    "Até agora, milhares de exoplanetas foram descobertos pela missão Kepler, provavelmente, mais serão encontradas pela missão TESS (Transiting Exoplanet Survey Satellite) da NASA, que observa o céu inteiro para localizar planetas que orbitam as estrelas mais próximas e brilhantes.")

                engine.say(
                    "Uma maneira de encontrar exoplanetas é procurar por estrelas “vacilantes”")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Uma estrela que tem planetas não orbita perfeitamente em torno de seu centro")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Dessa forma, de longe, essa órbita descentralizada faz com que a estrela pareça trêmula")
                engine.runAndWait()
                engine.stop()
                engine.say("Centenas de planetas foram descobertos usando esse método")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " No entanto, apenas grandes planetas – como Júpiter, ou até maiores – podem ser vistos dessa maneira")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Planetas menores, como a Terra, são muito mais difíceis de encontrar, porque criam apenas pequenas oscilações, mais difíceis de detectar")
                engine.runAndWait()
                engine.stop()
                engine.say("Método de trânsito:")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Em 2009, a NASA lançou uma espaçonave chamada Kepler para procurar exoplanetas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Kepler procurou planetas em uma ampla variedade de tamanhos e órbitas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Além disso,  esses planetas orbitam em torno de estrelas que variam de tamanho e temperatura")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Alguns dos planetas descobertos por Kepler são planetas rochosos, como a Terra, inclusive com zonas habitáveis, onde a vida pode ser possível")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Contudo, o mais próximo deles se encontra a cerca de 12 anos-luz de distância do nosso planeta")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os exoplanetas foram detectados usando o chamado método de trânsito")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Dessa forma, quando um planeta passa na frente de sua estrela, isso é chamado de trânsito")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " À medida que o planeta transita diante da estrela, ele bloqueia um pouco da luz da mesma")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Isso significa que uma estrela parecerá um pouco menos brilhante quando o planeta passar à sua frente")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os astrônomos também podem observar como o brilho da estrela muda durante um trânsito, o que  pode ajudar a descobrir o tamanho do planeta")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Assim, estudando o tempo entre trânsitos, os astrônomos também podem descobrir a que distância o planeta está de sua estrel")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Até agora, milhares de exoplanetas foram descobertos pela missão Kepler , provavelmente, mais serão encontradas pela missão TESS (Transiting Exoplanet Survey Satellite) da NASA, que observa o céu inteiro para localizar planetas que orbitam as estrelas mais próximas e brilhantes")
                print("Satélites, naturais e artificiais.  ")
                engine.say("Satélites, naturais e artificiais ")
                engine.runAndWait()
                engine.stop()
                print("Satélites naturais:Cometas, luas,anéis e poeira cósmica.")
                engine.say("Satélites naturais:Cometas, luas,anéis e poeira cósmica")
                engine.runAndWait()
                engine.stop()
                print(
                    "Os satélites naturais são corpos celestes que orbitam em torno de um planeta ou outro corpo maior.  ")
                print("Diferenciando cometas,asteróides e poeira cósmica.")
                print(
                    "Um asteroide é um corpo rochoso composto por minerais e metais que orbita no Sistema Solar. Já o cometa é uma bola de poeira e gelo,embora também contenha rocha em sua composição, são oriundos das regiões externas do Sistema Solar. ")
                print("Aproveitando, vou falar sobre Meteoritos, meteoros e meteoroides.")
                print(
                    "Meteoroides são pequenas pedras ou pedaços de metal que viajam pelo espaço. Os astrônomos os definem como corpos celestes que orbitam o Sol e têm menos de 10 metros. Rochas espaciais de tamanho maior - até mil quilômetros - ficam conhecidas como asteroides.")
                print(
                    "Meteoros são flashes de luz que ocorrem quando um meteoroide queima e se desintegra na atmosfera da Terra, criando o que é popularmente conhecido como estrela cadente. ")
                print(
                    "Os meteoritos são pedras que, diferentemente do meteoro, sobrevivem à entrada na atmosfera da Terra e chegam ao solo terrestre.")

                engine.say(
                    "Os satélites naturais são corpos celestes que orbitam em torno de um planeta ou outro corpo maior  ")
                engine.runAndWait()
                engine.stop()
                engine.say("Diferenciando cometas,asteróides e poeira cósmica")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Um asteroide é um corpo rochoso composto por minerais e metais que orbita no Sistema Solar")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Já o cometa é uma bola de poeira e gelo,embora também contenha rocha em sua composição, são oriundos das regiões externas do Sistema Solar ")
                engine.runAndWait()
                engine.stop()
                engine.say("Aproveitando, vou falar sobre Meteoritos, meteoros e meteoroides")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Meteoroides são pequenas pedras ou pedaços de metal que viajam pelo espaço")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os astrônomos os definem como corpos celestes que orbitam o Sol e têm menos de 10 metros ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Rochas espaciais de tamanho maior - até mil quilômetros - ficam conhecidas como asteroides")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Meteoros são flashes de luz que ocorrem quando um meteoroide queima e se desintegra na atmosfera da Terra, criando o que é popularmente conhecido como estrela cadente")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os meteoritos são pedras que, diferentemente do meteoro, sobrevivem à entrada na atmosfera da Terra e chegam ao solo terrestre")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Meteriotos são pedras que 'sobreviveram' à entrada na atmosfera terrestre e chega ao solo da Terra")

                print(
                    "Satélites artificiais:Satélites de comunicação , satélites científicos, satélites meteorológicos, Satélites de sensoriamento remoto de recursos terrestres e Satélites de uso militar. ")
                print(
                    "Um satélite de comunicação é um satélite artificial para fins de telecomunicações.")
                print(
                    "O satélite cria um canal de comunicação entre uma fonte transmissora e outra receptora de rádio em diferentes locais do planeta Terra.")
                print(
                    "Eles também são usados nas comunicações com navios e aviões, o que não pode ser feito por outras tecnologias, tais como a transmissão a cabo. A comunicação sem fio usa ondas eletromagnéticas para transportar sinais. Estas ondas requerem linhas de visão, e são, portanto, obstruídas pela curvatura da Terra. A finalidade de satélites de comunicações é retransmitir o sinal em torno da curva da Terra, permitindo a comunicação entre pontos amplamente separados. Satélites de comunicações usam uma ampla gama de frequências de rádio e micro-ondas. Para evitar interferências de sinal, as organizações internacionais têm regulamentos que estabelecem quais faixas de frequência ou bandas as organizações estão autorizadas a usar. Esta alocação de bandas minimiza o risco de interferência de sinal.")
                print(
                    "Os satélites científicos, variam de telescópios espacias até as estações orbitais, sendo essas As estações espaciais (ou estações orbitais) são espaçonaves capazes de suportar uma tripulação no espaço durante um período estendido de tempo, onde outras espaçonaves podem ancorar. As estações não possuem sistema de pouso e decolagem, por isso a carga e os tripulantes são transportados por outros veículos. As estações espaciais são utilizadas para estudar os efeitos causados pela longa permanência de seres humanos no espaço e servem como plataforma para diversos estudos que não seriam possíveis em outras naves ou na Terra.Contrário dos telescópios espaciais, que  não são tripulados e transportam um grande telescópio para luz visível e infravermelha).")
                print(
                    "Um satélite meterológico é primariamente usado para monitorar o tempo e o clima da Terra, embora monitorem também efeitos da atividade humana, como luzes das cidade, queimadas, níveis de poluição, além de auroras polares, tempestades de raios e poeira, superfícies cobertas por neve e gelo, desmatamento e correntes oceânicas, entre outros.")
                print(
                    "Os Satélites de sensoriamento remoto de recursos terrestres possibilita ma obtenção de informações sobre alvos na superfície terrestre (objetos, áreas, fenômenos), através do registro da interação da radiação eletromagnética com a superfície, realizado por sensores distantes, ou remotos. Geralmente estes sensores estão presentes em plataformas orbitais ou satélites, aviões e a nível de campo. ")
                print(
                    "Popularmente chamados de 'GPS' (Global Positioning System ou Sistema de Posicionamento Global)")
                print(
                    "Um satélite militar é um satélite artificial usado para um propósito militar, frequentemente destinado à coleta de informações de inteligência, tal como as comunicações por satélite usadas para fins militares, ou como uma arma militar.")
                print(
                    "Um satélite por si só não é nem militar nem civil. É o tipo de carga que ele transporta, que permite que se chegar a uma decisão referente ao seu caráter militar ou civil.Porém, mesmo a distinção  está confusa. ")
                print(
                    "Por exemplo, um satélite civil pode transportar transponders militares e vice-versa. Satélites civis comerciais também são conhecidos por executar tarefas militares incluindo possibilitar comunicações, imageamento etc. Ao mesmo tempo, os satélites militares como o GPS possuem mais usuários civis do que militares. A despeito das possibilidades acima, satélites que tenham utilizações puramente militares são conhecidos como satélites militares.")

                engine.say(
                    "Satélites artificiais:Satélites de comunicação , satélites científicos, satélites meteorológicos, Satélites de sensoriamento remoto de recursos terrestres e Satélites de uso militar ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Um satélite de comunicação é um satélite artificial para fins de telecomunicações")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "O satélite cria um canal de comunicação entre uma fonte transmissora e outra receptora de rádio em diferentes locais do planeta Terra")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Eles também são usados nas comunicações com navios e aviões, o que não pode ser feito por outras tecnologias, tais como a transmissão a cabo")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " A comunicação sem fio usa ondas eletromagnéticas para transportar sinais")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Estas ondas requerem linhas de visão, e são, portanto, obstruídas pela curvatura da Terra")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "A finalidade de satélites de comunicações é retransmitir o sinal em torno da curva da Terra, permitindo a comunicação entre pontos amplamente separados")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Satélites de comunicações usam uma ampla gama de frequências de rádio e micro-ondas")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Para evitar interferências de sinal, as organizações internacionais têm regulamentos que estabelecem quais faixas de frequência ou bandas as organizações estão autorizadas a usar")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Esta alocação de bandas minimiza o risco de interferência de sinal")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os satélites científicos, variam de telescópios espacias até as estações orbitais, sendo essas As estações espaciais (ou estações orbitais) são espaçonaves capazes de suportar uma tripulação no espaço durante um período estendido de tempo, onde outras espaçonaves podem ancorar")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "As estações não possuem sistema de pouso e decolagem, por isso a carga e os tripulantes são transportados por outros veículos")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "As estações espaciais são utilizadas para estudar os efeitos causados pela longa permanência de seres humanos no espaço e servem como plataforma para diversos estudos que não seriam possíveis em outras naves ou na Terra.Contrário dos telescópios espaciais, que  não são tripulados e transportam um grande telescópio para luz visível e infravermelha")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Um satélite meterológico é primariamente usado para monitorar o tempo e o clima da Terra, embora monitorem também efeitos da atividade humana, como luzes das cidade, queimadas, níveis de poluição, além de auroras polares, tempestades de raios e poeira, superfícies cobertas por neve e gelo), desmatamento e correntes oceânicas, entre outros")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Os Satélites de sensoriamento remoto de recursos terrestres possibilita ma obtenção de informações sobre alvos na superfície terrestre (objetos, áreas, fenômenos), através do registro da interação da radiação eletromagnética com a superfície, realizado por sensores distantes, ou remotos")
                engine.say(
                    " Geralmente estes sensores estão presentes em plataformas orbitais ou satélites, aviões e a nível de campo ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Popularmente chamados de 'GPS' (Global Positioning System ou Sistema de Posicionamento Global)")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Um satélite militar é um satélite artificial usado para um propósito militar, frequentemente destinado à coleta de informações de inteligência, tal como as comunicações por satélite usadas para fins militares, ou como uma arma militar")
                engine.runAndWait()
                engine.stop()
                engine.say("Um satélite por si só não é nem militar nem civil")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "É o tipo de carga que ele transporta, que permite que se chegar a uma decisão referente ao seu caráter militar ou civil")
                engine.runAndWait()
                engine.stop()
                engine.say("Porém, mesmo a distinção  está confusa ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Por exemplo, um satélite civil pode transportar transponders militares e vice-versa")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Satélites civis comerciais também são conhecidos por executar tarefas militares incluindo possibilitar comunicações, imageamento e dentre outros")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " Ao mesmo tempo, os satélites militares como o GPS possuem mais usuários civis do que militares")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    " A despeito das possibilidades acima, satélites que tenham utilizações puramente militares são conhecidos como satélites militares")

                print("Satélite artificial")
                engine.say("Satélite artificial")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRwEnzmu60WcYFFZkCmQGFkWOzKeHIEYLjjGg&usqp=CAU")
                print("Satélite naturais")
                engine.say("Satélite naturais")
                engine.runAndWait()
                engine.stop()
                webbrowser.open(
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ1QKaBT6EXPfGRxCz8SvGOEsw0uItY3RFqOg&usqp=CAU")
                engine.say("Satélite naturais")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Gostaria de usar um simulador sobre a relação da Terra com a Lua?(por favor responda somente com s para sim e n para não)")
                engine.runAndWait()
                engine.stop()
                sim = input(
                    "Gostaria de usar um simulador sobre a rotações do nosso sistema solar?(por favor responda somente com s para sim e n para não)")
                if simtl == "s":
                    engine.say(
                        "Gostaria de ver as rotações planetária no  nosso sistema solar ou do sitema Terra-Lua?(escolha entre  '1',sendo a simulação do sistema solar, e '2' acessar a simulação do sistema de rotação Terra-Lua)")
                    engine.runAndWait()
                    engine.stop()
                    menu()
                    os = input(
                        "Gostaria de ver as rotações planetária no  nosso sistema solar ou do sitema Terra-Lua?(escolha entre  '1',sendo a simulação do sistema solar, e '2' acessar a simulação do sistema de rotação Terra-Lua)")
                    if os == 1:
                        s = SolarSystem()
                        SolarSystem(
                            dimensions=(500, 700),
                            scale=250,
                            entity_scale=5,
                            sim_rate=3,
                            start_date='2020-07-12',
                            fullscreen=True)
                        s.start()
                        print("Terminamos essa parte do curso")
                        engine.say("Terminamos essa parte do curso")
                        engine.runAndWait()
                        engine.stop()
                        menu()
                    if os == 2:
                        s = EarthMoon()
                        EarthoMoon(
                            dimensions=(500, 700),
                            scale=250,
                            entity_scale=5,
                            sim_rate=3,
                            start_date='2020-07-12',
                            fullscreen=True)
                        s.start()
                        print("Terminamos essa parte do curso")
                        engine.say("Terminamos essa parte do curso")
                        engine.runAndWait()
                        engine.stop()
                        menu()
                    else:
                        print("Opção inválida")
                        engine.say("Opção inválida")
                        engine.runAndWait()
                        engine.stop()
                        menu()
                if simtl == "n":
                    print("Terminamos essa parte do curso")
                    engine.say("Terminamos essa parte do curso")
                    engine.runAndWait()
                    engine.stop()
                    menu()
                else:
                    print("Tente novamente(por favor responda somente com s para sim e n para não)")
                    engine.say("Tente novamente(por favor responda somente com s para sim e n para não)")
                    engine.runAndWait()
                    engine.stop()
                    menu()
            if astc == "n":
                print("Tudo bem...Vou te redicionar para os temas")
                engine.say("Tudo bem...Vou te redicionar para os temas")
                engine.runAndWait()
                engine.stop()
                menu()
            else:
                print("Opção não aceitável")
                engine.say("Opção não aceitável")
                engine.runAndWait()
                engine.stop()



        if mat == 7:
            print("O.k")
            engine.say("O.k")
            print("você será redirecionado ao menu principal ")
            engine.say("você será redirecionado ao menu principal ")
            menu_princ()


def menu_princ():
    option5 = 0
    while option5 != 6:
        engine = pyttsx3.init()

        print('''                [Opção 1]Calculadora.
                [Opção 2]Aprendendo sobre astronomia.
                [opção 3]Um conto além da Terra.
                [opção 4]Fale comigo.
                [opção 5]Simulações.
                [opção 5]Encerrar programa.''')
        engine.say('''[Opção 1] calculadora.
                [Opção2]Aprendendo sobre astronomia.
                [opção3]Um conto além da Terra.
                [opção 4]Fale comigo.
                [opção 5]Simulações.
                [opção 6]Encerrar programa.''')
        engine.runAndWait()
        engine.stop()

        engine.say("Qual opção você deseja?")
        engine.runAndWait()
        engine.stop()

        option5 = int(input('Qual opção você deseja?'))

        if option5 == 1:
            class Calculadora():
                def __init__(self, raiz):

                    self.input_ = "0"
                    self.soma = Celula()
                    caixa_texto = Texto(raiz, self.input_)

                    def novo_botao(text, row, column, function):
                        return Botao(raiz, text, row, column, function)

                    def input_numero(numero):
                        return lambda: self.Numero(numero)

                    buttons = {}

                    numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
                    for numero in range(1, 10):
                        buttons.update(
                            {str(numero): (*numbers_positions[numero - 1], input_numero(numero))})

                    buttons.update({"0": (5, 5, input_numero(0))})

                    buttons.update({
                        "pi()": (2, 1, self.Pi),
                        "x²": (2, 2, self.Pow),
                        "log10()": (2, 3, self.Log10),
                        "%": (2, 4, self.Percentual),
                        "raiz()": (2, 5, self.Raiz_Quadrada),
                        "clear": (2, 6, self.clear_),
                        "sen()": (3, 1, self.Seno),
                        "cos()": (4, 1, self.Cosseno),
                        "tg()": (5, 1, self.Tangente)
                    })

                    for button in buttons.keys():
                        novo_botao(button, *buttons[button])

                def clear_(self):
                    self.input_ = "0"
                    caixa_texto = Texto(raiz, self.input_)

                def Raiz_Quadrada(self):
                    temporario = math.sqrt(float(self.input_))
                    self.input_ = str(temporario)
                    caixa_texto = Texto(raiz, self.input_)

                def Seno(self):
                    temporario = ((int(self.input_)) * 2 * math.pi) / (360)
                    self.input_ = math.sin(temporario)
                    caixa_texto = Texto(raiz, self.input_)

                def Cosseno(self):
                    temporario = ((int(self.input_)) * 2 * math.pi) / (360)
                    self.input_ = math.cos(temporario)
                    caixa_texto = Texto(raiz, self.input_)

                def Tangente(self):
                    temporario = ((int(self.input_)) * 2 * math.pi) / (360)
                    self.input_ = math.tan(temporario)
                    caixa_texto = Texto(raiz, self.input_)

                def Log10(self):
                    temporario = math.log10(int(self.input_))
                    self.input_ = temporario
                    caixa_texto = Texto(raiz, self.input_)

                def Pi(self):
                    self.input_ = math.pi
                    caixa_texto = Texto(raiz, self.input_)

                def Pow(self):
                    self.input_ = math.pow(float(self.input_), 2)
                    caixa_texto = Texto(raiz, self.input_)

                def Percentual(self):
                    self.input_ = (float(self.input_) / 100)
                    caixa_texto = Texto(raiz, self.input_)

                def Igual(self):
                    self.soma._numero_B = self.input_
                    soma = self.soma
                    operacao = {"soma": soma.soma,
                                "subtracao": soma.subtracao,
                                "multiplicacao": soma.multiplicacao,
                                "divisao": soma.divisao}
                    v = operacao()
                    caixa_texto = Texto(raiz, v)
                    self.input_ = v

                def Soma(self):
                    self.soma._numero_A = self.input_
                    self.soma._sinal = "soma"
                    self.input_ = "0"

                def Multiplicacao(self):
                    self.soma._numero_A = self.input_
                    self.soma._sinal = "multiplicacao"
                    self.input_ = "0"

                def Divisao(self):
                    self.soma._numero_A = self.input_
                    self.soma._sinal = "divisao"
                    self.input_ = "0"
                    print(self.soma._numero_A)

                def Subtracao(self):
                    self.soma._numero_A = self.input_
                    self.soma._sinal = "subtracao"
                    self.input_ = "0"

                def Numero(self, numero):
                    self.input_ += str(numero)
                    caixa_texto = Texto(raiz, self.input_)

            class Botao():
                def __init__(self, frame, text_botao, linha, coluna, comando):
                    self.button = Button(frame, text=text_botao, fg="black", bg="grey", command=comando,
                                         font=("Arial", "20", "bold"))
                    self.button["width"] = 5
                    self.button["height"] = 1
                    self.button.grid(row=linha, column=coluna)

            class Celula():
                def __init__(self):
                    self._numero_A = None
                    self._numero_B = None
                    self._sinal = None

                def soma(self):
                    return float(self._numero_A) + float(self._numero_B)

                def subtracao(self):
                    return float(self._numero_A) - float(self._numero_B)

                def multiplicacao(self):
                    return float(self._numero_A) * float(self._numero_B)

                def divisao(self):
                    return float(self._numero_A) / float(self._numero_B)

            class Texto():
                def __init__(self, raiz, texto):
                    self.texto = Label(raiz, text=round(float(texto), 5), font=("Arial", "72", "bold"))
                    self.texto["height"] = 2
                    self.texto["width"] = 2
                    self.texto.grid(row=1, column=1, columnspan=6, sticky=W + E + N + S)

            raiz = Tk()
            raiz.title("Calculadora")
            raiz.geometry("570x452")
            m = Calculadora(raiz)
            raiz.mainloop()
            menu_princ()
        if option5 == 2:
            print("Vou iniciar as aulas  de astronomia")
            engine.say("Vou iniciar as aulas  de astronomia")
            menu()

        if option5 == 3:
            print("A história já vai começar!")
            engine.say("A história já vai começar!")
            engine.runAndWait()
            engine.stop()
            print(
                "A Terra mandou {} para Marte,com o intuito de inspecionar a colônia marciana. Contudo,por causa dos detritos espaciais, vindo de missões anteriores e outras espaçonaves; houve um impacto na sua nave, logo você teve que ejetar dela, por meio de um módulo de fuga, portanto terá que pousar em um vale marciano."
                "Cuidado com as paredes do vale, elas vão destruir o seu módulo de fuga. ".format(name))

            engine.say(
                "A Terra mandou {} para Marte,com o intuito de inspecionar a colônia marciana. Contudo,por causa dos detritos espaciais, vindo de missões anteriores e outras espaçonaves; houve um impacto na sua nave, logo você teve que ejetar dela, por meio de um módulo de fuga, portanto terá que pousar em um vale marciano."
                "Cuidado com as paredes do vale, elas vão destruir o seu módulo de fuga. ".format(name))
            engine.runAndWait()
            engine.stop()
            print(
                "Para controlar, use as setas para alternar entre as direções, mas chegue ao solo, o sistema de pouso vai te protejer do impacto da queda."
                "(observação, caso queira pular a interação aperte 'espaço'.)")
            engine.say(
                "Para controlar, use as setas para alternar entre as direções, mas chegue ao solo, o sistema de pouso vai te protejer do impacto da queda."
                "(observação, caso queira pular a interação aperte 'espaço'.)")
            engine.runAndWait()
            engine.stop()

            while True:
                try:
                    engine = pyttsx3.init()
                    space = (0, 0, 0)
                    Color_Mars = (196, 44, 0)
                    Color_Ship = (80, 80, 80)
                    Color_Base = (50, 58, 101)

                    pygame.init()
                    clock = pygame.time.Clock()
                    screen = pygame.display.set_mode((800, 600))
                    pygame.display.set_caption("Pouse o módulo")
                    font = pygame.font.SysFont(None, 15)

                    def navegation():
                        exit = True

                        pos_x = randrange(0, 800 - 10, 10)
                        pos_y = randrange(0, 50 - 10, 10)
                        pos_x1 = randrange(0, 800 - 10, 10)
                        pos_y1 = (530)

                        vel_x = 0
                        vel_y = 0

                        def rover(carXY):
                            for XY in carXY:
                                pygame.draw.rect(screen, 0, 0, 0, [XY[0], XY[1], 20, 20])

                        def sup(pos_x, pos_y):
                            pygame.draw.rect(screen, 255, 0, 0, [pos_x, pos_y, 20, 20])

                        def game():
                            exit = True
                            pos_x = randint(0, (800 - 20) / 10) * 10
                            pos_y = randint(0, (600 - 20) / 10) * 10
                            sup_x = randint(0, (800 - 20) / 10) * 10
                            sup_y = randint(0, (600 - 20) / 10) * 10
                            vel_x = 0
                            vel_y = 0
                            carXY = []
                            Cartrain = 1

                        while exit:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    exit = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT and vel_x != 10:
                                        vel_y = 0
                                        vel_x = -10
                                    if event.key == pygame.K_RIGHT and vel_x != -10:
                                        vel_y = 0
                                        vel_x = 10
                                    if event.key == pygame.K_UP and vel_y != 10:
                                        vel_x = 0
                                        vel_y = -10
                                    if event.key == pygame.K_DOWN and vel_y != -10:
                                        vel_x = 0
                                        vel_y = 10
                                    if event.key == pygame.K_SPACE:
                                        exit = False

                            screen.fill(space)

                            Mars = pygame.Surface((800, 50))

                            base = pygame.Surface((20, 50))

                            pos_x += vel_x
                            pos_y += vel_y + 3.7
                            pygame.draw.rect(screen, Color_Ship, [pos_x, pos_y, 20, 20])
                            Mars.fill(Color_Mars)
                            base.fill(Color_Base)
                            screen.blit(Mars, [0, 550])
                            pygame.display.update()

                            clock.tick(10)

                            if pos_x > 800:
                                exit = True
                                print("{} bateu no rochedo, infeliz morreu".format(nome))

                                engine.say("{} bateu no rochedo, infeliz morreu".format(nome))
                                engine.runAndWait()
                                engine.stop()
                                navegation()

                            if pos_x < 0:
                                exit = True
                                print("{} saiu da orbita marciana, infeliz perdemos o contato ")

                                engine.say("{} saiu da orbita marciana, infeliz perdemos o contato ")
                                engine.runAndWait()
                                engine.stop()
                                navegation()

                            if pos_y > 600:
                                pos_y = 0
                                exit = False
                                print("{}, você  pousou com sucesso, aguarde que a equipe de resgate  de Marte irá socorre-lo ".format(name))
                                engine.say("{}, você  pousou com sucesso, aguarde que a equipe de resgate  de Marte irá socorre-lo ".format(name))
                                engine.runAndWait()
                                engine.stop()

                            if pos_y < 0:
                                pos_y = 600 - 10
                                exit = True
                                print("{} bateu no rochedo, infeliz morreu".format(nome))

                                engine.say("{} bateu no rochedo, infeliz morreu".format(nome))
                                engine.runAndWait()
                                engine.stop()
                                navegation()

                    navegation()
                    pygame.quit()
                    print(
                        "Após o pouso, você foi para uma colônia marciana.Depois da hospedagem hospitaleira, os colônos pediram para ajuda-los na busca de suprimentos  nos destroços, que a tua antiga nave  estava trasportando caso houvesse necessidade para os colônos.Para isso você terá  que controlar um rover não tripulado."
                        "Entretanto,para economizar a bateria das cápsulas de suprimentos, cada uma enviará sinais individualmente, logo após da captura de uma outra caixa, o sinal da cápsula obtida irá se apagar e ficar acoplada no seu veículo"
                        "Você pode optar por não auxiliar na procura ou retribuir o cuidados dele por você."
                        "(Os comandos para essa interação são os mesmo usados na anterior)")
                    engine.say("Após o pouso, você foi para uma colônia marciana.Depois da hospedagem hospitaleira, os colônos pediram para ajuda-los na busca de suprimentos  nos destroços, que a tua antiga nave  estava trasportando caso houvesse necessidade para os colônos.Para isso você terá  que controlar um rover não tripulado."
                        "Entretanto,para economizar a bateria das cápsulas de suprimentos, cada uma enviará sinais individualmente, logo após da captura de uma outra caixa, o sinal da cápsula obtida irá se apagar e ficar acoplada no seu veículo"
                        "Você pode optar por não auxiliar na procura ou retribuir o cuidados dele por você."
                        "(Os comandos para essa interação são os mesmo usados na anterior)")
                    engine.runAndWait()
                    engine.stop()



                except:
                    print("O modulo pygame não foi inicializado com sucesso")
                    engine.say("O modulo pygame não foi inicializado com sucesso")
                    engine.runAndWait()
                    engine.stop()

                Color_Mars = (196, 44, 0)
                Color_sup = (0, 0, 0)
                Color_Rover = (250, 250, 250)

                try:

                    pygame.init()

                    clock = pygame.time.Clock()
                    screen = pygame.display.set_mode((800, 600))
                    pygame.display.set_caption("Recupere os suprimentos ")

                    def rover(carXY):
                        for XY in carXY:
                            pygame.draw.rect(screen, Color_Rover, [XY[0], XY[1], 20, 20])

                    def sup(pos_x, pos_y):
                        pygame.draw.rect(screen, Color_sup, [pos_x, pos_y, 20, 20])

                    def game():
                        exit1 = True
                        pos_x = randint(0, (800 - 20) / 10) * 10
                        pos_y = randint(0, (600 - 20) / 10) * 10
                        sup_x = randint(0, (800 - 20) / 10) * 10
                        sup_y = randint(0, (600 - 20) / 10) * 10
                        vel_x = 0
                        vel_y = 0
                        carXY = []
                        Cartrain = 1
                        while exit1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    exit1 = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT and vel_x != 20:
                                        vel_y = 0
                                        vel_x = -20
                                    if event.key == pygame.K_RIGHT and vel_x != -20:
                                        vel_y = 0
                                        vel_x = 20
                                    if event.key == pygame.K_UP and vel_x != 20:
                                        vel_x = 0
                                        vel_y = -20
                                    if event.key == pygame.K_DOWN and vel_y != -20:
                                        vel_x = 0
                                        vel_y = 20
                                    if event.key == pygame.K_SPACE:
                                        exit1 = False
                            screen.fill(Color_Mars)
                            pos_x += vel_x
                            pos_y += vel_y

                            carstart = []
                            carstart.append(pos_x)
                            carstart.append(pos_y)
                            carXY.append(carstart)
                            if len(carXY) > Cartrain:
                                del carXY[0]
                            if any(point == carstart for point in carXY[:-1]):
                                pass

                            rover(carXY)
                            if pos_x == sup_x and pos_y == sup_y:
                                sup_x = randint(0, (800 - 20) / 10) * 10
                                sup_y = randint(0, (600 - 20) / 10) * 10
                                Cartrain += 1

                            sup(sup_x, sup_y)
                            pygame.display.update()
                            clock.tick(15)

                        if pos_x > 800:
                            exit1 = True
                            print("Você perdeu o contato com o rover ")
                            engine.say("Você perdeu o contato com o rover ")
                            engine.runAndWait()
                            engine.stop()
                            game()

                        if pos_x < 0:
                            exit1 = True
                            print("Você perdeu o contato com o rover ")
                            engine.say("Você perdeu o contato com o rover ")
                            engine.runAndWait()
                            engine.stop()
                            game()

                        if pos_y > 600:
                            pos_y = 0
                            exit1 = True
                            print("Você perdeu o contato com o rover ")
                            engine.say("Você perdeu o contato com o rover ")
                            engine.runAndWait()
                            engine.stop()
                            game()

                        if pos_y < 0:
                            pos_y = 600 - 10
                            exit1 = True
                            print("Você perdeu o contato com o rover ")
                            engine.say("Você perdeu o contato com o rover ")
                            engine.runAndWait()
                            engine.stop()
                            game()

                    game()
                    pygame.quit()
                    print(
                        "Depois de ter inspecionado, você  percebe que a colônia está em bom estado e pode retornar à Terra, com a missão cumprida, parabéns {}". format (name))
                    engine.say(
                        "Depois de ter inspecionado, você  percebe que a colônia está em bom estado e pode retornar à Terra, com a missão cumprida, parabéns {}". format (name))
                    engine.runAndWait()
                    engine.stop()
                    menu_princ()




                except:
                    print("O modulo pygame não foi inicializado com sucesso")
                    menu_princ()

        if option5 == 4:
            print("Iniciando chatbot...")
            engine.say("Iniciando chatbot...")

            bot = ChatBot('F.I.H.A', storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                          logic_adapters=[
                              "chatterbot.logic.BestMatch"
                          ],
                          input_adapter="chatterbot.input.TerminalAdapter",
                          output_adapter="chatterbot.output.TerminalAdapter",
                          database="../database.db"
                          )

            bot.set_trainer(ListTrainer)
            wikipedia.set_lang("pt")
            keywords_def = ['quem era', 'quem é ', 'defina', 'definição', 'o que é']
            dict_cmds = {}

            def load_cmds():
                lines = open('cmd.txt', 'r').readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    parts = line.split('\t')
                    dict_cmds.update({parts[0]: parts[1]})
                for _file in os.listdir('database'):  # Passa por todo o arquivo
                    lines = open('database/' + _file, 'r').readlines()  # Abre em leitura e lê linhas
                    bot.train(lines)

            def evaluate(text):
                result = None
                try:
                    result = dict_cmds[text]
                except:
                    result = None
                return result

            def run_cmd(cmd_type):
                result = None

                if cmd_type == 'asktime':
                    now = datetime.now()
                    result = 'São ' + str(now.hour) + ' horas e  ' + str(now.minute) + ' minutos.'

                    s.start()
                if cmd_type == 'askimag':
                    webbrowser.open(
                        "https://apod.nasa.gov/apod/astropix.html")

                if cmd_type == 'askdate':
                    now = datetime.now()
                    months = ['Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
                              'agosto',
                              'Setembro Outubro Novembro Dezembro']
                    result = 'Hoje é ' + months[now.month - 1] + str(now.day) + '.'
                elif cmd_type == 'askcputemp':
                    res = os.popen('vcgencmd measure_temp').readline()
                    CPU = res.replace("temp=", '').replace("'C\n", '')
                    result = 'O sistema está operando com ' + str(CPU) + ' graus Celcius.'
                elif cmd_type == 'askexit':
                    print('F.I.H.A: Tchau!!!')
                    print("Muito obrigado! Volte sempre! <3")
                    engine.say("Muito obrigado! Volte sempre!")
                    engine.runAndWait()
                    engine.stop()
                else:
                    result = None
                return result

            def get_wiki(text):
                result = None
                results = None

                # Pesquisa se estiver com palavra chave
                if text is not None:
                    for key in keywords_def:
                        if text.startswith(key):
                            result = text.replace(key, '')

                if result is not None:
                    results = wikipedia.search(result)
                    result = wikipedia.summary(results[0], sentences=2)

                return result

            load_cmds()

            for k, v in dict_cmds.items():
                print(k, ' > ', v)
            print('---------------------------------------')
            print('F.I.H.A:Olá!!! O que eu posso fazer para você,hoje?')
            engine.say("Olá!!! O que eu posso fazer para você,hoje?")
            engine.runAndWait()
            engine.stop()
            name = "Érick"
            while True:
                quest = input('{}: '.format(name))
                quest = quest.lower()

                resp = run_cmd(evaluate(quest))

                if resp == None:
                    resp = get_wiki(quest)
                    if resp == None:
                        resp = bot.get_response(quest)
                print('F.I.H.A: ' + str(resp))
                engine.say((resp))
                engine.runAndWait()
                engine.stop()
                print('Tipo de comando: ', evaluate(quest))
        if option5 ==5:
            engine.say(
                "Gostaria de usar um simulador sobre a relação da Terra com a Lua?(por favor responda somente com s para sim e n para não)")
            engine.runAndWait()
            engine.stop()
            sim = input(
                "Gostaria de usar um simulador sobre a rotações do nosso sistema solar?(por favor responda somente com s para sim e n para não)")
            if simtl == "s":
                print("Comandos:Para controlar a câmera, use as setas e as respetivas direções das setas irão mover a câmera; para dar  aumentar o s objetos estudados aperte '+'  e para diminuir a imagem use o botão '-' ,ambos estão no lado esquerdo do backsapce; 'r' para redefinir o zoom e as posições; ',' para acelerar e '.' para desacelerar; por fim 'q' para sair da simulação ")
                engine.say("Comandos:Para controlar a câmera, use as setas e as respetivas direções das setas irão mover a câmera; para dar  aumentar o s objetos estudados aperte o 'sinal de soma'  e para diminuir a imagem use o botão 'símbolo de subtração' ,ambos estão do lado esquerdo do backsapce; 'r' para redefinir o zoom e as posições; 'vírgula' para acelerar e 'ponto' para  desacelerar; por fim 'q' para sair da simulação ")
                engine.runAndWait()
                engine.stop()
                engine.say(
                    "Gostaria de ver as rotações planetária no  nosso sistema solar ou do sitema Terra-Lua?(escolha entre  '1',sendo a simulação do sistema solar, e '2' acessar a simulação do sistema de rotação Terra-Lua)")
                engine.runAndWait()
                engine.stop()
                menu()
                os = input(
                    "Gostaria de ver as rotações planetária no  nosso sistema solar ou do sitema Terra-Lua?(escolha entre  '1',sendo a simulação do sistema solar, e '2' acessar a simulação do sistema de rotação Terra-Lua)")
                if os == 1:
                    s = SolarSystem()
                    SolarSystem(
                        dimensions=(500, 700),
                        scale=250,
                        entity_scale=5,
                        sim_rate=3,
                        start_date='2020-07-12',
                        fullscreen=True)
                    s.start()
                    print("Terminamos essa parte do curso")
                    engine.say("Terminamos essa parte do curso")
                    engine.runAndWait()
                    engine.stop()
                    menu_princ()
                if os == 2:
                    s = EarthMoon()
                    EarthoMoon(
                        dimensions=(500, 700),
                        scale=250,
                        entity_scale=5,
                        sim_rate=3,
                        start_date='2020-07-12',
                        fullscreen=True)
                    s.start()
                    print("Terminamos essa parte do curso")
                    engine.say("Terminamos essa parte do curso")
                    engine.runAndWait()
                    engine.stop()
                    menu_princ()
                else:
                    print("Opção inválida")
                    engine.say("Opção inválida")
                    engine.runAndWait()
                    engine.stop()


        if option5 == 6:
            print("Muito obrigado! Volte sempre! <3")
            engine.say("Muito obrigado! Volte sempre!")
            engine.runAndWait()
            engine.stop()
            print("Encerrando F.I.H.A...")
            engine.say("Encerrando F.I.H.A...")
            engine.runAndWait()
            engine.stop()
            break




        else:
            print("Opção inválidade.")
            engine.say("Opção inválidade.")
            print("Tente novamente.")
            engine.say("Tente novamente.")


version = "1.0-BETA"
msg2 = "FIHA"
print("{:=^36}".format(msg2))
msg = " - version {} / BY:ÉRICK PRADO E LIVIA OLIVEIRA ".format(version)
print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg))

print("Olá,mundo!!!")
engine = pyttsx3.init()
engine.say("Olá,mundo!!!")
engine.runAndWait()
engine.stop()

print(
    "Sou  FIHA(Ferramenta de integração humana na astronomia) tenho o objetivo de ajudar pessoas a descobrir ou entenderem a astronomia, por meio da informática.Para isso  conto com uma calculadora,para auxiliar nos teus estudos; um pequeno curso de astronomia,baseado nas aulas da USP e uma história interativa  sobre a exploração espacial, na qual você irá comandar tal missão. ")
engine.say(
    "Sou  FIHA(Ferramenta de integração humana na astronomia) tenho o objetivo de ajudar pessoas a descobrir ou entenderem a astronomia, por meio da informática   para isso  conto com uma calculadora,para auxiliar nos teus estudos; um pequeno curso de astronomia,baseado nas aulas da USP e uma história interativa  sobre a exploração espacial, na qual você irá comandar tal missão ")
engine.runAndWait()
engine.stop()
print(
    "Antes de começarmos, peço que espere eu falar,antes de responder, sendo que você deve responder na última linha e não na pergunta")
engine.say(
    "Antes de começarmos, peço que espere eu falar,antes de responder, sendo que você deve responder na última linha e não na pergunta")
engine.runAndWait()
engine.stop()

while True:

    engine.say("Você tem microfone, por favor responda somente com s para sim e n para não?")
    engine.runAndWait()
    engine.stop()

    micr = input("Você tem microfone, por favor responda somente com s para sim e n para não?")

    if micr == "s":
        r = sr.Recognizer()
        mic = sr.Microphone()
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            print("Qual é o seu nome?")
            engine.say("Qual é o seu nome?")
            engine.runAndWait()
            engine.stop()
            audio = r.listen(fonte)
            print("Enviando para reconhecimento...")
            engine.say("Enviando para reconhecimento")
            engine.runAndWait()
            engine.stop()

        try:
            name = r.recognize_google(audio, language="pt-BR")
            print("Teu nome é {}?".format(name))
            engine.say("Teu nome é {}?".format(name))
            engine.runAndWait()
            engine.stop()
            engine.say("Se sim digite 's', caso não digite 'n' ")
            engine.runAndWait()
            engine.stop()
            respn2 = input("Se sim digite 's', caso não digite 'n'")
            if respn2 == "s":
                engine.say("Excelente,{}".format(name))
                engine.runAndWait()
                engine.stop()
                print("Excelente,{}".format(name))
                print("{},gostaria de saber o que eu posso fazer?".format(name))
                engine.say("{},gostaria de saber o que eu posso fazer?".format(name))
                engine.runAndWait()
                engine.stop()
                engine.say("Se sim digite 's', caso não digite 'n' ")
                engine.runAndWait()
                engine.stop()
                respt3 = input("Se sim digite 's', caso não digite 'n' ")
                if respt3 == "s":
                    engine.say("Que bom")
                    engine.runAndWait()
                    engine.stop()
                    print("Que bom")
                    engine.say("Posso fazer cálculos básicos como")
                    engine.runAndWait()
                    engine.stop()
                    print("Posso fazer cálculos básicos como:")
                    engine.say("Operações de adição")
                    engine.runAndWait()
                    engine.stop()
                    print("Operações de adição")
                    engine.say("Escolha um número")
                    engine.runAndWait()
                    engine.stop()
                    cal1 = int(input("Escolha um número"))
                    engine.say("escolha outro número")
                    engine.runAndWait()
                    engine.stop()
                    cal2 = int(input("escolha outro número"))
                    cal3 = cal1 + cal2
                    engine.say("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))
                    engine.runAndWait()
                    engine.stop()
                    print("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))

                    engine.say("Operações de subtração")
                    engine.runAndWait()
                    engine.stop()
                    print("Operações de subtração")
                    engine.say("Escolha um número")
                    engine.runAndWait()
                    engine.stop()
                    cal1 = int(input("Escolha um número"))
                    engine.say("escolha outro número")
                    engine.runAndWait()
                    engine.stop()
                    cal2 = int(input("escolha outro número"))
                    cal3 = cal1 - cal2
                    print("O resultado entre  {} menos {} resulta em {}".format(cal1, cal2, cal3))
                    engine.say("O resultado entre  {} menos {} resulta em  {}".format(cal1, cal2, cal3))
                    engine.runAndWait()
                    engine.stop()

                    print("Operações com produto")
                    engine.say("Operações com produto")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Escolha um número")
                    engine.runAndWait()
                    engine.stop()
                    cal1 = int(input("Escolha um número"))
                    engine.say("escolha outro número")
                    engine.runAndWait()
                    engine.stop()
                    cal2 = int(input("escolha outro número"))
                    cal3 = cal1 * cal2
                    print("A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                    engine.say("A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                    engine.runAndWait()
                    engine.stop()
                    print("Operações  com frações.")
                    engine.say("Operações  com frações.")
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Escolha um número")
                    engine.runAndWait()
                    engine.stop()
                    cal1 = int(input("Escolha um número"))
                    engine.say("escolha outro número")
                    engine.runAndWait()
                    engine.stop()
                    cal2 = int(input("escolha outro número"))
                    cal3 = cal1 / cal2
                    print("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                    engine.say("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                    engine.runAndWait()
                    engine.stop()


                    def raizes(a, b, c):
                        D = (b ** 2 - 4 * a * c)
                        x1 = (-b + D ** (1 / 2)) / (2 * a)
                        x2 = (-b - D ** (1 / 2)) / (2 * a)

                        print('\nValor de x1: {0}'.format(x1))
                        engine.say("\nValor de x1: {0}".format(x1))
                        engine.runAndWait()
                        engine.stop()
                        print('Valor de x2: {0}'.format(x2))
                        engine.say("Valor de x2: {0}".format(x2))
                        engine.runAndWait()
                        engine.stop()


                    if __name__ == '__main__':
                        while True:
                            engine.say("Posso computar as raízes de uma equação de 2º grau\n")
                            engine.runAndWait()
                            engine.stop()
                            print("Posso computar as raízes de uma equação de 2º grau\n")
                            engine.say("Entre com o valor de a: ")
                            engine.runAndWait()
                            engine.stop()
                            a = float(input('Entre com o valor de a: '))

                            engine.say("Entre com o valor de b: ")
                            engine.runAndWait()
                            engine.stop()
                            b = float(input('Entre com o valor de b: '))
                            engine.say("Entre com o valor de c: ")
                            engine.runAndWait()
                            engine.stop()
                            c = float(input('Entre com o valor de c: '))

                            raizes(a, b, c)

                            print(
                                "Obviamente a minha calculadora será diferente,pois terá mais coisas")
                            engine = pyttsx3.init()
                            engine.say(
                                "obviamente a minha calculadora será diferente,pois terá mais coisas")
                            engine.runAndWait()
                            engine.stop()
                            print("Tenho um chatbot interativo e temas sobre a astronomia")
                            engine.say("Tenho um chatbot interativo e temas sobre a astronomia")
                            engine.runAndWait()
                            engine.stop()

                            engine.say("Chegamos ao final do tutorial")
                            engine.runAndWait()
                            engine.stop()
                            print("Chegamos ao final do tutorial")
                            engine.say("Agora meu menu vai aparecer.")
                            engine.runAndWait()
                            engine.stop()
                            print("Agora meu menu vai aparecer.")
                            option = 0
                            menu_princ()
                if respt3 == "n":
                    engine.say("Agora meu menu vai aparecer.")
                    engine.runAndWait()
                    engine.stop()
                    print("Agora meu menu vai aparecer.")
                    menu_princ()
                else:
                    print("Responda com s ou n, por favor, tente novamente")
                    engine.say("Responda com s ou n, por favor, tente novamente")
                    engine.runAndWait()
                    engine.stop()
            if respt2 == "n":
                engine.say("Agora meu menu vai aparecer.")
                engine.runAndWait()
                engine.stop()
                print("Agora meu menu vai aparecer.")
                menu_princ()




            else:
              print("Responda com s ou n, por favor, tente novamente")
              engine.say("Responda com s ou n, por favor, tente novamente")
              engine.runAndWait()
              engine.stop()






        except:


                engine.say("Digite teu nome")
                engine.runAndWait()
                engine.stop()
                name = input("Digite teu nome")
                print("Teu nome é {}?".format(name))
                engine.say("Teu nome é {}?".format(name))
                engine.runAndWait()
                engine.stop()
                engine.say("Se sim digite 's', caso não digite 'n' ")
                engine.runAndWait()
                engine.stop()
                respn3 = input("Se sim digite 's', caso não digite 'n'")
                if respn3 == "s":
                    engine.say("Excelente,{}".format(name))
                    engine.runAndWait()
                    engine.stop()
                    print("Excelente,{}".format(name))
                    print("{},gostaria de saber o que eu posso fazer?".format(name))
                    engine.say("{},gostaria de saber o que eu posso fazer?".format(name))
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Se sim digite 's', caso não digite 'n' ")
                    engine.runAndWait()
                    engine.stop()
                    respt2 = input("Se sim digite 's', caso não digite 'n' ")
                    if respt2 == "s":
                        engine.say("Que bom")
                        engine.runAndWait()
                        engine.stop()
                        print("Que bom")
                        engine.say("Posso fazer cálculos básicos como")
                        engine.runAndWait()
                        engine.stop()
                        print("Posso fazer cálculos básicos como:")
                        engine.say("Operações de adição")
                        engine.runAndWait()
                        engine.stop()
                        print("Operações de adição")
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 + cal2
                        engine.say("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()
                        print("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))

                        engine.say("Operações de subtração")
                        engine.runAndWait()
                        engine.stop()
                        print("Operações de subtração")
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 - cal2
                        print("O resultado entre  {} menos {} resulta em {}".format(cal1, cal2, cal3))
                        engine.say("O resultado entre  {} menos {} resulta em  {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()

                        print("Operações com produto")
                        engine.say("Operações com produto")
                        engine.runAndWait()
                        engine.stop()
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 * cal2
                        print("A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.say(
                            "A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()
                        print("Operações  com frações.")
                        engine.say("Operações  com frações.")
                        engine.runAndWait()
                        engine.stop()
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 / cal2
                        print("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.say("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()


                        def raizes(a, b, c):
                            D = (b ** 2 - 4 * a * c)
                            x1 = (-b + D ** (1 / 2)) / (2 * a)
                            x2 = (-b - D ** (1 / 2)) / (2 * a)

                            print('\nValor de x1: {0}'.format(x1))
                            engine.say("\nValor de x1: {0}".format(x1))
                            engine.runAndWait()
                            engine.stop()
                            print('Valor de x2: {0}'.format(x2))
                            engine.say("Valor de x2: {0}".format(x2))
                            engine.runAndWait()
                            engine.stop()


                        if __name__ == '__main__':
                            while True:
                                engine.say("Posso computar as raízes de uma equação de 2º grau\n")
                                engine.runAndWait()
                                engine.stop()
                                print("Posso computar as raízes de uma equação de 2º grau\n")
                                engine.say("Entre com o valor de a: ")
                                engine.runAndWait()
                                engine.stop()
                                a = float(input('Entre com o valor de a: '))

                                engine.say("Entre com o valor de b: ")
                                engine.runAndWait()
                                engine.stop()
                                b = float(input('Entre com o valor de b: '))
                                engine.say("Entre com o valor de c: ")
                                engine.runAndWait()
                                engine.stop()
                                c = float(input('Entre com o valor de c: '))

                                raizes(a, b, c)

                                print(
                                    "Obviamente a minha calculadora será diferente,pois terá mais coisas")
                                engine = pyttsx3.init()
                                engine.say(
                                    "obviamente a minha calculadora será diferente,pois terá mais coisas")
                                engine.runAndWait()
                                engine.stop()
                                print("Tenho um chatbot interativo e temas sobre a astronomia")
                                engine.say("Tenho um chatbot interativo e temas sobre a astronomia")
                                engine.runAndWait()
                                engine.stop()

                                engine.say("Chegamos ao final do tutorial")
                                engine.runAndWait()
                                engine.stop()
                                print("Chegamos ao final do tutorial")
                                engine.say("Agora meu menu vai aparecer.")
                                engine.runAndWait()
                                engine.stop()
                                print("Agora meu menu vai aparecer.")
                                option = 0
                                menu_princ()
                    if respt2 == "n":
                        engine.say("Agora meu menu vai aparecer.")
                        engine.runAndWait()
                        engine.stop()
                        print("Agora meu menu vai aparecer.")
                        menu_princ()
                    else:
                        print("Responda com s ou n, por favor, tente novamente")
                        engine.say("Responda com s ou n, por favor, tente novamente")
                        engine.runAndWait()
                        engine.stop()


                if respn3 == "n":
                    engine.say("Digite teu nome")
                    engine.runAndWait()
                    engine.stop()
                    name = input("Digite teu nome")
                    print("{},gostaria de saber o que eu faço?".format(name))
                    engine.say("{},gostaria de saber o que eu faço?".format(name))
                    engine.runAndWait()
                    engine.stop()
                    engine.say("Se sim digite 's', caso não digite 'n' ")
                    engine.runAndWait()
                    engine.stop()
                    respt2 = input("Se sim digite 's', caso não digite 'n' ")
                    if respt2 == "s":
                        engine.say("Que bom")
                        engine.runAndWait()
                        engine.stop()
                        print("Que bom")
                        engine.say("Posso fazer cálculos básicos como")
                        engine.runAndWait()
                        engine.stop()
                        print("Posso fazer cálculos básicos como:")
                        engine.say("Operações de adição")
                        engine.runAndWait()
                        engine.stop()
                        print("Operações de adição")
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 + cal2
                        engine.say("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()
                        print("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))

                        engine.say("Operações de subtração")
                        engine.runAndWait()
                        engine.stop()
                        print("Operações de subtração")
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 - cal2
                        print("O resultado entre  {} menos {} resulta em {}".format(cal1, cal2, cal3))
                        engine.say("O resultado entre  {} menos {} resulta em  {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()

                        print("Operações com produto")
                        engine.say("Operações com produto")
                        engine.runAndWait()
                        engine.stop()
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 * cal2
                        print("A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.say(
                            "A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()
                        print("Operações  com frações.")
                        engine.say("Operações  com frações.")
                        engine.runAndWait()
                        engine.stop()
                        engine.say("Escolha um número")
                        engine.runAndWait()
                        engine.stop()
                        cal1 = int(input("Escolha um número"))
                        engine.say("escolha outro número")
                        engine.runAndWait()
                        engine.stop()
                        cal2 = int(input("escolha outro número"))
                        cal3 = cal1 / cal2
                        print("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.say("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
                        engine.runAndWait()
                        engine.stop()


                        def raizes(a, b, c):
                            D = (b ** 2 - 4 * a * c)
                            x1 = (-b + D ** (1 / 2)) / (2 * a)
                            x2 = (-b - D ** (1 / 2)) / (2 * a)

                            print('\nValor de x1: {0}'.format(x1))
                            engine.say("\nValor de x1: {0}".format(x1))
                            engine.runAndWait()
                            engine.stop()
                            print('Valor de x2: {0}'.format(x2))
                            engine.say("Valor de x2: {0}".format(x2))
                            engine.runAndWait()
                            engine.stop()


                        if __name__ == '__main__':
                            while True:
                                engine.say("Posso computar as raízes de uma equação de 2º grau\n")
                                engine.runAndWait()
                                engine.stop()
                                print("Posso computar as raízes de uma equação de 2º grau\n")
                                engine.say("Entre com o valor de a: ")
                                engine.runAndWait()
                                engine.stop()
                                a = float(input('Entre com o valor de a: '))

                                engine.say("Entre com o valor de b: ")
                                engine.runAndWait()
                                engine.stop()
                                b = float(input('Entre com o valor de b: '))
                                engine.say("Entre com o valor de c: ")
                                engine.runAndWait()
                                engine.stop()
                                c = float(input('Entre com o valor de c: '))

                                raizes(a, b, c)

                                print(
                                    "Obviamente a minha calculadora será diferente,pois terá mais coisas")
                                engine = pyttsx3.init()
                                engine.say(
                                    "obviamente a minha calculadora será diferente,pois terá mais coisas")
                                engine.runAndWait()
                                engine.stop()
                                print("Tenho um chatbot interativo e temas sobre a astronomia")
                                engine.say("Tenho um chatbot interativo e temas sobre a astronomia")
                                engine.runAndWait()
                                engine.stop()

                                engine.say("Chegamos ao final do tutorial")
                                engine.runAndWait()
                                engine.stop()
                                print("Chegamos ao final do tutorial")
                                engine.say("Agora meu menu vai aparecer.")
                                engine.runAndWait()
                                engine.stop()
                                print("Agora meu menu vai aparecer.")
                                option = 0
                                menu_princ()


                    if respt2 == "n":
                        engine.say("Agora meu menu vai aparecer.")
                        engine.runAndWait()
                        engine.stop()
                        print("Agora meu menu vai aparecer.")
                        menu_princ()
                    else:
                        print("Responda com s ou n, por favor, tente novamente")
                        engine.say("Responda com s ou n, por favor, tente novamente")
                        engine.runAndWait()
                        engine.stop()

                else:
                    print("Responda com s ou n, por favor, tente novamente")
                    engine.say("Responda com s ou n, por favor, tente novamente")
                    engine.runAndWait()
                    engine.stop()


    if micr == "n":
        engine.say("Digite teu nome")
        engine.runAndWait()
        engine.stop()
        name = input("Digite teu nome:")
        print("{},gostaria de saber o que eu faço?".format(name))
        engine.say("{},gostaria de saber o que eu faço?".format(name))
        engine.runAndWait()
        engine.stop()
        engine.say("Se sim digite 's', caso não digite 'n' ")
        engine.runAndWait()
        engine.stop()
        respt2 = input("Se sim digite 's', caso não digite 'n' ")
        if respt2 == "s":
            engine.say("Que bom")
            engine.runAndWait()
            engine.stop()
            print("Que bom")
            engine.say("Posso fazer cálculos básicos como")
            engine.runAndWait()
            engine.stop()
            print("Posso fazer cálculos básicos como:")
            engine.say("Operações de adição")
            engine.runAndWait()
            engine.stop()
            print("Operações de adição")
            engine.say("Escolha um número")
            engine.runAndWait()
            engine.stop()
            cal1 = int(input("Escolha um número"))
            engine.say("escolha outro número")
            engine.runAndWait()
            engine.stop()
            cal2 = int(input("escolha outro número"))
            cal3 = cal1 + cal2
            engine.say("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))
            engine.runAndWait()
            engine.stop()
            print("O valor entre a soma de {} com {} resulta em {}".format(cal1, cal2, cal3))

            engine.say("Operações de subtração")
            engine.runAndWait()
            engine.stop()
            print("Operações de subtração")
            engine.say("Escolha um número")
            engine.runAndWait()
            engine.stop()
            cal1 = int(input("Escolha um número"))
            engine.say("escolha outro número")
            engine.runAndWait()
            engine.stop()
            cal2 = int(input("escolha outro número"))
            cal3 = cal1 - cal2
            print("O resultado entre  {} menos {} resulta em {}".format(cal1, cal2, cal3))
            engine.say("O resultado entre  {} menos {} resulta em  {}".format(cal1, cal2, cal3))
            engine.runAndWait()
            engine.stop()

            print("Operações com produto")
            engine.say("Operações com produto")
            engine.runAndWait()
            engine.stop()
            engine.say("Escolha um número")
            engine.runAndWait()
            engine.stop()
            cal1 = int(input("Escolha um número"))
            engine.say("escolha outro número")
            engine.runAndWait()
            engine.stop()
            cal2 = int(input("escolha outro número"))
            cal3 = cal1 * cal2
            print("A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
            engine.say(
                "A resposta da multiplicação de {} com {} tem o valor de {}".format(cal1, cal2, cal3))
            engine.runAndWait()
            engine.stop()
            print("Operações  com frações.")
            engine.say("Operações  com frações.")
            engine.runAndWait()
            engine.stop()
            engine.say("Escolha um número")
            engine.runAndWait()
            engine.stop()
            cal1 = int(input("Escolha um número"))
            engine.say("escolha outro número")
            engine.runAndWait()
            engine.stop()
            cal2 = int(input("escolha outro número"))
            cal3 = cal1 / cal2
            print("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
            engine.say("A resposta da fração de {} sobre{} tem o valor de {}".format(cal1, cal2, cal3))
            engine.runAndWait()
            engine.stop()


            def raizes(a, b, c):
                D = (b ** 2 - 4 * a * c)
                x1 = (-b + D ** (1 / 2)) / (2 * a)
                x2 = (-b - D ** (1 / 2)) / (2 * a)

                print('\nValor de x1: {0}'.format(x1))
                engine.say("\nValor de x1: {0}".format(x1))
                engine.runAndWait()
                engine.stop()
                print('Valor de x2: {0}'.format(x2))
                engine.say("Valor de x2: {0}".format(x2))
                engine.runAndWait()
                engine.stop()


            if __name__ == '__main__':
                while True:
                    engine.say("Posso computar as raízes de uma equação de 2º grau\n")
                    engine.runAndWait()
                    engine.stop()
                    print("Posso computar as raízes de uma equação de 2º grau\n")
                    engine.say("Entre com o valor de a: ")
                    engine.runAndWait()
                    engine.stop()
                    a = float(input('Entre com o valor de a: '))

                    engine.say("Entre com o valor de b: ")
                    engine.runAndWait()
                    engine.stop()
                    b = float(input('Entre com o valor de b: '))
                    engine.say("Entre com o valor de c: ")
                    engine.runAndWait()
                    engine.stop()
                    c = float(input('Entre com o valor de c: '))

                    raizes(a, b, c)

                    print(
                        "Obviamente a minha calculadora será diferente,pois terá mais coisas")
                    engine = pyttsx3.init()
                    engine.say(
                        "obviamente a minha calculadora será diferente,pois terá mais coisas")
                    engine.runAndWait()
                    engine.stop()
                    print("Tenho um chatbot interativo e temas sobre a astronomia")
                    engine.say("Tenho um chatbot interativo e temas sobre a astronomia")
                    engine.runAndWait()
                    engine.stop()

                    engine.say("Chegamos ao final do tutorial")
                    engine.runAndWait()
                    engine.stop()
                    print("Chegamos ao final do tutorial")
                    engine.say("Agora meu menu vai aparecer.")
                    engine.runAndWait()
                    engine.stop()
                    print("Agora meu menu vai aparecer.")
                    option = 0
                    menu_princ()

        if respt2 == "n":
            engine.say("Agora meu menu vai aparecer.")
            engine.runAndWait()
            engine.stop()
            print("Agora meu menu vai aparecer.")
            menu_princ()
        else:
            print("Responda com s ou n, por favor, tente novamente")
            engine.say("Responda com s ou n, por favor, tente novamente")
            engine.runAndWait()
            engine.stop()

    else:
        print("Responda com s ou n, por favor, tente novamente")
        engine.say("Responda com s ou n, por favor, tente novamente")
        engine.runAndWait()
        engine.stop()
