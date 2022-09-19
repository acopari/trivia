import time # Importamos la librería time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'



puntaje = 0

iniciar_trivia = True  
intentos = 0  

print (CYAN+"Bienvenido a mi trivia sobre preguntas random")
print ("Pondremos a prueba tus conocimientos")
nombre=input(BLUE+'\nIngresa tu nombre :')
print (nombre,"Tienes", puntaje, "puntos")

while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0

  print(YELLOW+"\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  time.sleep(1) 
  print("Jugando...")
  time.sleep(1)

  print(GREEN+'\n¿Cuál es el único mamífero que puede volar?')
  print(YELLOW+'a)El pato')
  print(YELLOW+'b)El murciélago')
  print(YELLOW+'c)El avestruz') 
  print(YELLOW+'d)El dodo'+RESET)
  respuesta=input('\ningrese respuesta : ')
  while respuesta not in ('a','b','c','d'):
    respuesta=input(MAGENTA+'solo debe ingresar a,b,c ó d ingrese nuevamente su respuesta: ')

  
  if respuesta == 'a':
    print('respuesta incorrecta  :(')
    print(RED+"sabias que el pato es un animal ovíparo, es decir, la hembra pone huevos para tener cría")
  elif respuesta == 'c':
    print('respuesta incorrecta  :(')
    print(RED+"sabias que es el ave actual más grande y más pesada")
  elif respuesta == 'd':
    print('respuesta incorrecta  :(')
    print(RED+"sabias que se trata de un ave no voladora pero que está extinta")
  else:
    print('respuesta correcta  :)')
    puntaje = puntaje +20  
    print(CYAN+"Excelente, has obtenido", puntaje, "puntos")
  print("\n¿Deseas intentar la trivia nuevamente?")

  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si":  
     print(GREEN+"\nEspero ",nombre," que lo hayas pasado bien, hasta pronto!")
     iniciar_trivia = False  




















  
  
  
  

