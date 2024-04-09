#Variable

mi_string_variable = "Texto con string"
print(mi_string_variable)

mi_int_variable = 3
print(mi_int_variable)

mi_float_variable = 3.14
print(mi_float_variable)

mi_bool_variable = True
print(mi_bool_variable)

mi_complex_variable = 1+3j
print(mi_complex_variable)

mi_list_variable = [1,2,3]
print(mi_list_variable)

mi_tuple_variable = (1,2,3)
print(mi_tuple_variable)

mi_set_variable = {1,2,3}
print(mi_set_variable)

mi_dict_variable = {"nombre":"Juan"}
print(mi_dict_variable)

mi_none_variable = None
print(mi_none_variable)

#Concatenacion de variables en un print
print(mi_string_variable, mi_int_variable, mi_float_variable, mi_bool_variable, mi_complex_variable, mi_list_variable, mi_tuple_variable, mi_set_variable, mi_dict_variable, mi_none_variable)  

#uso de la funcion str(), type()
mi_int_to_string = str(mi_int_variable)
print(mi_int_to_string)
print(type(mi_int_to_string))

print(len(mi_string_variable)) #longitud de la cadena de texto con la funcion len()
print("Esta es el valor de la variable mi_string_variable: ", mi_string_variable)

print("La longitud de  cadena de texto es:", len(mi_string_variable)) #longitud de la cadena de texto con la funcion len()


#Variables en una sola linea, pero no es recomendable
nombre, apellido, alias, sapo= "Fredy", "Pallo","Pato", "Si"
print("Mi nombre es ", nombre, " mi apellido es ", apellido, " mi alias es ", alias, "y si soy sapo?", sapo)

#ingresar valores por teclado, con la funcion input()
tecladoString = input("Ingrese un Nombre: ")
tecladoString2 = input("Ingrese un Apellido: ")

print("El nombre ingresado es: ", tecladoString)
print("El apellido ingresado es: ", tecladoString2)

