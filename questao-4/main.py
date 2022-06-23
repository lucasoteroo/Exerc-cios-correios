'''Modifique uma vez mais o programa para que seja calculado e exibido o peso total em gramas de todos os itens enviados nos pedidos informados pelo usuário. '''


import bibCorreios 

custo_subtotal = 0
somador_arrecadado = 0
contador_entrega = 0
contador_grama = 0

while True: 
  pedido= input("Você deseja informar mais pedidos? digite sim ou nao : ")

  if pedido.upper() == "SIM":
   
    while True:
     tipo_item = input("O tipo do item é pacote ou documento ? ")
     if bibCorreios.validaTipoItem(tipo_item):
      break
     else:
      print("Entrada inválida, digite corretamente ")


    while True:
     peso_item = float(input("O peso do item em quilos é ? "))
     if bibCorreios.validaPeso(peso_item):
      peso_gramas =bibCorreios.convertePeso(peso_item)
      contador_grama += peso_gramas
      custo_subtotal = bibCorreios.calculaCustoItem(tipo_item,peso_gramas)

      break
     else:
      print("Entrada inválida, digite corretamente ")

    while True:
     embalagem_item = input("A embalagem do item é pequena, média, grande ou especial ? ")
     if bibCorreios.validaEmbalagem(embalagem_item):
       custo_subtotal += bibCorreios.calculaCustoEmbalagem(embalagem_item) 
       break
     else:
      print("Entrada inválida, digite corretamente ")

    while True:
     entrega= input("O tipo da entrega será normal, sedex ou sedex10 ? ")
     

     if bibCorreios.validaEntrega(entrega):
       custo_subtotal += bibCorreios.calculaCustoEntrega(entrega) 
       print ("Senhor, o valor total do seu envio é de: "   ,custo_subtotal,"reais")
       somador_arrecadado += custo_subtotal

       if entrega.upper == "SEDEX" or "SEDEX10" : 
        contador_entrega += 1
        print ("_________________________________________________")
       break
     else:
       print("Entrada inválida, digite corretamente ")

   

  elif pedido.upper() == "NAO" or pedido.upper() == "NÃO":
     print("O custo total arrecadado pelos correios é :",somador_arrecadado,"reais" )
     print ( "O total de pedidos com a opção sedex e sedex10 é de :",contador_entrega,"pedidos")
     print("O peso total em gramas de todos os itens enviados nos pedidos informados pelo usuário é de ",contador_grama, "gramas" )
     break
 
