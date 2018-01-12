####################################
#							              #
#	Programa: Operacoes de Ponto	  #
#              Flutuante.          #
#	Finalizado em: 26/05/2014	     #
#	por: Larissa Pinto Lopes	     #
#                   11221826       #
#		Ramon M. de A. Sorage        #
#                   10811053       #
#							              #
####################################

			##################
			#	Funcoes!      #
			##################

#####################
#                   #
# Funcao para ler   #
# o valor informado #
# usuario.          #
#                   #
#####################

def LeValor():
	
	aux = 0
	npf = [0.0, 0]
	while(1):

		try:
			npf[0] = aux = float(raw_input("\n>> Digite um valor: "))
			
		except ValueError:
			print("\a>>> Valor invalido. Digite novamente!")
			pass
			
		if (type(aux) == float):
			break
	
	print ("\nNumero informado pelo usuario: %.5f" % aux)
	
	if(aux > 0):
		if(aux > 10):
			while(npf[0] > 10.0):
				npf[0] /= 10.0
				npf[1] += 1
	
	
		if(aux < 1):
			while(npf[0] < 1.0):
				npf[0] *= 10.0
				npf[1] -= 1
	
	elif(aux < 0):
		if(aux < -10):
			while(npf[0] < -10.0):
				npf[0] /= 10.0
				npf[1] += 1
	
	
		if(aux > -1):
			while(npf[0] > -1.0):
				npf[0] *= 10.0
				npf[1] -= 1
	return npf

###########################
#                         #
# Operacoes:              #
# O resultado sera        #
# apresentado como numero #
# de ponto flutuante.     #
#                         #
###########################

#####################
#                   #
# Funcao de Adicao. #
#                   #
#####################

def Soma(npf1, npf2):

	result = npf1[0] + npf2[0]
	exp = npf1[1]
	
	if(npf1[1] > 0):
		while(exp):
			result *= 10
			exp -= 1
	elif(npf1[1] < 0):
		while(exp):
			result /= 10
			exp += 1
	return result

########################
#                      #
# Funcao de Subtracao. #
#                      #
########################
	
def Subtracao(npf1, npf2):

	result = npf1[0] - npf2[0]
	exp = npf1[1]
	
	if(npf1[1] > 0):
		while(exp):
			result *= 10
			exp -= 1
	elif(npf1[1] < 0):
		while(exp):
			result /= 10
			exp += 1
	return result
	
############################
#                          #
# Funcao de Multiplicacao. #
#                          #
############################

def Multiplicacao(npf1, npf2):

	result = npf1[0] * npf2[0]
	exp = 2 * npf1[1] 
	
	if(npf1[1] > 0):
		while(exp):
			result *= 10
			exp -= 1
	elif(npf1[1] < 0):
		while(exp):
			result /= 10
			exp += 1
	return result
	
######################
#                    #
# Funcao de Divisao. #
#                    #
######################
	
def Divisao(npf1, npf2):

	result = npf1[0] / npf2[0] 
	
	return result
	
#############################
#                           #
# Funcao que recebe         #
# o resultado da operacao e #
# o normatiza.              #
#                           #
#############################
	
def AjusteFinal(aux):

	npf = [0.0, 0]
	npf[0] = aux
	if(aux > 0):
		if(aux > 10):
			while(npf[0] > 10.0):
				npf[0] /= 10.0
				npf[1] += 1
	
	
		if(aux < 1):
			while(npf[0] < 1.0):
				npf[0] *= 10.0
				npf[1] -= 1
	
	elif(aux < 0):
		if(aux < -10):
			while(npf[0] < -10.0):
				npf[0] /= 10.0
				npf[1] += 1
	
	
		if(aux > -1):
			while(npf[0] > -1.0):
				npf[0] *= 10.0
				npf[1] -= 1
				
	return npf

	
############################################## MAIN ##############################################

##############################
#                            #
# Chamando a funcao para     #
# leitura do valor fornecido #
# pelo usuario.              #
#                            #
##############################

print("\n>> Calculadora de numeros de ponto flutuante <<.\n>> Os numeros serao apresentados na forma de ponto flutuante e normatizada. <<")

	
npf1 = LeValor()
print ("Numero informado na forma normatizada: " + "%.5f" % npf1[0] + " * 10^" + "%i" % npf1[1])

npf2 = LeValor()
print ("\n" + "Numero informado na forma normatizada: " + "%.5f" % npf2[0] + " * 10^" + "%i" % npf2[1] + "\n")

##########################
#                        #  
# Igualando os expoentes #
# dos valores fornecidos #
# pelo usuario.          #
#                        #
##########################


if(npf1[1] < npf2[1]):
	while(npf1[1] != npf2[1]):
		npf1[0] /= 10
		npf1[1] += 1
		
elif(npf1[1] > npf2[1]):
	while(npf2[1] != npf1[1]):
		npf2[0] /= 10
		npf2[1] += 1

################################
#                              #
# Leitura do valor equivalente #
# a operacao a ser realizada.  #
#                              #
################################
		
op = 0.0
while(1):
	
	while(1):
		try:
			op = int(raw_input("\nInforme a operacao a ser realizada:\n1- Adicao\n2- Subtracao\n3- Multiplicacao\n4- Divisao\n5 - Sair\n>> "))
			
		except ValueError:
			print("\aValor invalido. Digite novamente!")
			pass
			
		if (type(op) == int and (op >= 1 and op <=5)):
			break

##################################
#                                #
# Python naum tem switch - case, #
# usa-se if: ... elif:           #
#                                #
##################################

	if(op == 1):
		resultado = Soma(npf1, npf2)
		print ("\n" + "Resultado da Operacao de Adicao: " + "%.5f" % resultado)
		resultado = AjusteFinal(resultado)
		print ("Resultado da Operacao de Adicao na forma normatizada: " + "%.5f" % resultado[0] + " * 10^" + "%i" % resultado[1] + "\n")

	elif(op == 2):
		resultado = Subtracao(npf1, npf2)
		print ("\n" + "Resultado da Operacao de Subtracao: " + "%.5f" % resultado)
		resultado = AjusteFinal(resultado)
		print ("\n" + "Resultado da Operacao de Subtracao na forma normatizada: " + "%.5f" % resultado[0] + " * 10^" + "%i" % resultado[1] + "\n")

	elif(op == 3):
		resultado = Multiplicacao(npf1, npf2)
		print ("\n" + "Resultado da Operacao de Multiplicacao: " + "%.5f" % resultado)
		resultado = AjusteFinal(resultado)
		print ("\n" + "Resultado da Operacao de Multiplicacao na forma normatizada: " + "%.5f" % resultado[0] + " * 10^" + "%i" % resultado[1] + "\n")

	elif(op == 4):
		resultado = Divisao(npf1, npf2)
		print ("\n" + "Resultado da Operacao de Divisao: " + "%.5f" % resultado)
		resultado = AjusteFinal(resultado)
		print ("\n" + "Resultado da Operacao de Divisao na forma normatizada: " + "%.5f" % resultado[0] + " * 10^" + "%i" % resultado[1] + "\n")

	elif(op == 5):
		print("\nObrigado por utilizar este programa.\n")
		break
