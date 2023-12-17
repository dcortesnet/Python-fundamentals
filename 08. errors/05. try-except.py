class MyError(Exception):
    pass

try:
    raise MyError("Mi error")
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
    print('Este código nunca será ejecutado.')
except MyError as error:
    print(error)  # Mi error
finally: 
    print("Finally")
    

try:
    # Código con error
    pass
except TypeError as error:
    print("TypeError")
except ReferenceError as error:
    print("ReferenceError")
except Exception as error:
    print("Error")
finally:
    print("Finally")