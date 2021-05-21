#CALCULADORA - ALCANCE DE ANÚNCIO ONLINE:

investimento = input('Digite o valor a ser investido: ')
investimento = float(investimento)

#Visualizações atreladas ao valor investido:
visualizacao = investimento*30

#Cliques gerados por volume de visualizações:
cliques = int(visualizacao*.12)

#Compartilhamentos por volume de cliques:
compartilham = int(cliques*.15)

#Manipulação de compartilhamentos considerando restrições: 

#Sequência de compartilhamentos 
controle_compart = compartilham//5
resto = compartilham%5
controle_compart *= 4
controle_compart += resto

#Visualizações atreladas aos compartilhamentos:
visualiz_extra = controle_compart * 40

#Total de visualizações:
visualizacao += visualiz_extra
visualizacao = int(visualizacao)
print(f'O alcance do seu anúncio é de aproximadamente {visualizacao} visualizações. ')