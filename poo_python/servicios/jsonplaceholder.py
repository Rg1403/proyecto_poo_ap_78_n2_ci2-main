import requests
from prettytable import PrettyTable

def obtener_users_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        # print(respuesta.json())
        tabla_usuarios = PrettyTable()
        tabla_usuarios.field_names= ['Id','Nombre','Email']
        usuarios = respuesta.json()
        for usuario in usuarios:
            tabla_usuarios.add_row([usuario['id'],usuario['name'],usuario['email']])
        print(tabla_usuarios)

def crear_user_api(url):
    nombre = input('Nombre: ')
    usuario = input('Usuario: ')
    email =  input('Email: ')
    telefono = input('Teléfono: ')
    
    user = {
        "name": nombre,
        "username": usuario,
        "email": email,
        "phone": telefono
    }
    respuesta = requests.post(url,json=user)
    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f'Usuario creado exitosamente: {respuesta.json()}')
    
def actualizar_user_api(url):
    nombre = input('Nombre: ')
    usuario = input('Usuario: ')
    email =  input('Email: ')
    telefono = input('Teléfono: ')
    id_usuario = input('Id usuario: ')
    
    url = f'{url}/{id_usuario}'
    
    user = {
        "name": nombre,
        "username": usuario,
        "email": email,
        "phone": telefono
    }
    respuesta = requests.put(url,json=user)
    if respuesta.status_code == 200:
        print(f'Usuario creado exitosamente: {respuesta.json()}')