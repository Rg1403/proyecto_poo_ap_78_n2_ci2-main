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
        print(f'Usuario modificado exitosamente: {respuesta.json()}')
        
def eliminar_user_api(url):
    id_usuario = input('Id usuario: ')
    
    url = f'{url}/{id_usuario}'
    
    respuesta = requests.delete(url,)
    if respuesta.status_code == 200:
        print(f'Usuario eliminado exitosamente: {respuesta.json()}')
        
def obtener_albums_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        # print(respuesta.json())
        tabla_albums = PrettyTable()
        tabla_albums.field_names= ['Id usuario','Id','Titulo']
        albums = respuesta.json()
        for album in albums:
            tabla_albums.add_row([album['Id usuario'],album['Id'],album['Titulo']])
        print(tabla_albums)

def crear_album_api(url):
    tittle =  input('titulo: ')
    
    user = {
        "Titulo": tittle,
    }
    respuesta = requests.post(url,json=user)
    if respuesta.status_code == 200 or respuesta.status_code == 201:
        print(f'album creado exitosamente: {respuesta.json()}')
    
def actualizar_album_api(url):
    id_usuario = input('Id usuario: ')
    id = input('Usuario: ')
    tittle = input('titulo')
    
    url = f'{url}/{id_usuario}'
    
    user = {
        "Id usuario": id_usuario,
        "Id": id,
        "titulo": tittle,
    }
    respuesta = requests.put(url,json=user)
    if respuesta.status_code == 200:
        print(f'album modificado exitosamente: {respuesta.json()}')

def eliminar_album_api(url):
    id_album = input('Id album: ')
    url = f'{url}/{id_album}'
    
    respuesta = requests.delete(url,)
    if respuesta.status_code == 200:
        print(f'album eliminado exitosamente: {respuesta.json()}')