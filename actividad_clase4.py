def lista():
     lista_de_numeros=[]
     while True:
          ing=input("queres ingresar numeros a las lista s o n?: ")
          if "si"== ing.lower():
           
           i = input("ingresar numero: ")
           
           lista_de_numeros.append(i)
           
          else:
              print("gracias!")
              break
     print("la lista es: ", lista_de_numeros)
     suma= 0
     for n in lista_de_numeros:
      suma += int(n)
        
     print(suma)
     indice = len(lista_de_numeros)
     promedio = suma/ indice
     print(promedio)
     
lista()