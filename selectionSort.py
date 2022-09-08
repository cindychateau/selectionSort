#array = [2, 5, 1, 6]
#j -> 0 - 3
#j = 0
#posicion_menor = 0
#i -> 1 - 3
#i = 1
# array[1] < array[0] -> 5 < 2
#i = 2
# array[2] < array[0] -> 1 < 2
#posicion_menor = 2
#i = 3
# array[3] < array[2] -> 6 < 2
#temp = array[2] = 1
#array[2] = array[0] = 2
#array[0] = temp = 1
#array = [1, 5, 2, 6]

#j = 1
#posicion_menor = 1
# i -> 2 - 3
# i = 2
#array[2] < array[1] -> 2 < 5
#posicion_menor = 2
#i = 3
#array[3] < array[2] -> 6 < 2
#temp = array[2] = 2
#array[2] = array[1] = 5
#array[1] = temp = 2
#array = [1, 2, 5, 6]

#j = 2
#posicion_menor = 2
#i -> 3
#i = 3
#array[3] < array[2] -> 6 < 5

#array = [1, 2, 5, 6]
def selectionSort(array):
    #Primer for es el ROJO, que nos va a indicar la posición en donde queremos hacer el switch
    for j in range(len(array)):
        posicion_menor = j #0
        #SEGUNDO for representa AZUL
        for i in range(j+1, len(array)):
            #Si de mi arreglo el valor que tengo la posición i es menor a lo que tengo en posicion_menor
            if array[i] < array[posicion_menor]:
                posicion_menor = i

        #Hacemos switch entre posicion_menor y j #arr[1] = 10; arr[2] = 1
        temp = array[posicion_menor] #temp = 1
        array[posicion_menor] = array[j] #arr[2] = 10
        array[j] = temp #arr[1] = 1


arr = [2, 5, 1, 6]
selectionSort(arr)
print(arr)