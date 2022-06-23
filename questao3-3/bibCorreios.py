
# Questão 1
def validaTipoItem(item): 
   
  if item.upper() == "PACOTE" or  item.upper() == "DOCUMENTO" : 
     return True 
  else: 
     return False 

# Questão 2
def validaPeso(peso):
  if peso >= 0:
    return True
  else:
    return False  

# QUestão 3 
def convertePeso(peso):
  return (peso)*1000

# QUestão 4 
def calculaCustoItem(tipo,peso):
 valor = 0
 if tipo.upper() == "PACOTE":
  valor = peso * 0.003
  return valor
 elif tipo.upper() == "DOCUMENTO":
    valor = peso * 0.002
    return valor

# QUestão 5 
def validaEmbalagem(tamanho):
  if tamanho.upper() == "PEQUENA" or tamanho.upper() == "MEDIA" or tamanho.upper() == "GRANDE" or tamanho.upper() == "ESPECIAL":
    return True
  else:
    return False

# QUestão 6
def calculaCustoEmbalagem(tamanho):
  if tamanho.upper() == "PEQUENA":
    return 4
  elif tamanho.upper() == "MEDIA":
    return 7      
  elif tamanho.upper() == "GRANDE":
    return 10
  elif tamanho.upper() == "ESPECIAL":
    return 0   


# QUestão 7 
def validaEntrega(entrega):
  if entrega.upper() == "NORMAL" or entrega.upper() == "SEDEX" or entrega.upper() == "SEDEX10":
      return True
  else:
    return False

# QUestão 8 

def calculaCustoEntrega(entrega):
  if entrega.upper() == "NORMAL":
    return 0
  elif entrega.upper() == "SEDEX":
    return 5
  elif entrega.upper() == "SEDEX10":
    return 8   