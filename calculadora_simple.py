

# def calculadora(operador,num1,num2):
#     if operador=="+":
#         return num1+num2
#     elif operador=="-":
#         return num1-num2
#     elif operador=="*":
#         return num1*num2
#     elif operador=="/":
#         if num2==0:
#             raise ValueError("Error: no puedes dividir entre 0")
#         return num1/num2
#     else:
#         print(f"el {operador} no es un operador valido, por favor introduce uno valido")
#         return calculadora()
    
    
# def main():
#     print("bienvenido a la calculadora en python!")
    
#     try:
#         operador= input("Introduce un operador (+,-,*,/): ")
#         operadores_validos= ["+","-","*","/"]
#         if operador not in operadores_validos:
#             print(f"{operador} no es un operdador valido, los operadores validos son {operadores_validos}.")
#             return
        
#         num1=float(input("introduce el primer numero: "))
#         num2=float(input("introduce el segundo numero: "))
        
#         resultado= calculadora(operador,num1,num2)
#         print(f"el resultado es: {round(resultado,3)}")
        
#     except ValueError as e:
#         print (f"Error: {e}")

# print("Hasta la proxima!")

# if __name__=="__main__":
#     main()







def mult():
    var=5
    var2=7 
    result= var * var2
    print(result)


mult()