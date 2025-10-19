from fastapi import FastAPI

app = FastAPI()

users = ["Adrián", "Violeta", "Jeiron"]

# Funció per a passar la llista d'usuaris a Diccionari
def passarADict():
    ids = range(len(users))
    diccionari = dict(zip(ids, users))
    return diccionari

# 1. Crear - Afegir a la list
@app.post("/api/users", response_model=dict)
def add_users(nombre: str):
    users.append(nombre)
    diccionari = passarADict()
    return diccionari

# 2. Llegir - Consultar un usuari/objecte de la llista
@app.get("/api/users/{id}", response_model=dict)
def read_user(id:int):
    if id >= len(users) or id < 0:
        return {"error": "Usuari no trobat"}
    else:
        diccionari = passarADict()
        return {id: diccionari[id]}

# 3. Llegir - Consultar tots els usuaris
@app.get("/api/users", response_model=dict)
def read_users():
    diccionari = passarADict()
    return diccionari

# 4. Actualitzar - Actualitzación completa
@app.put("/api/users/{id}", response_model=dict)
def update_user(id:int, nombre: str):
    if id >= len(users) or id < 0:
        return {"error": "Usuari no trobat"}
    else:
        users[id] = nombre
        diccionari = passarADict()
        return diccionari
    
# 6. Eliminar - Esborrar usuari 
@app.delete("/api/usuaris/{id}", response_model=dict)
def delete_user(id: int):
    if id >= len(users) or id < 0:
        return {"error": "Usuari no trobat"}
    else:
        users.pop(id)
        diccionari = passarADict()
        return diccionari
    

