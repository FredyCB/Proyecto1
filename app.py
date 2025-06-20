import urllib.parse
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient
from classes.local import Local
from classes.juego import Juego

load_dotenv() # Carga variables de entorno

# Configurar conexión a MongoDB

URI = "mongodb+srv://fcardonabanegas:" + urllib.parse.quote("Creeper@5") +  "@cluster0.cqmsaac.mongodb.net/"

def get_database():
    client = MongoClient(URI)
    return client["videojuegos_db"]

def main():
    db = get_database()
    
    # Crear juegos
    juego1 = Juego(titulo="Cyberpunk 2077", genero="RPG", precio=49.99)
    juego1_id = juego1.save(db)
    
    juego2 = Juego(titulo="FIFA 2025", genero="Deportes", precio=59.99)
    juego2_id = juego2.save(db)

    juego3 = Juego(titulo="TLOZ: Tears of the Kingdom", genero="Accion-MundoAbierto", precio=70.0)
    juego3_id = juego3.save(db)
    
    # Crear locales
    local1 = Local(
        nombre="GameCenter Plaza",
        direccion="Av. Principal 123",
        telefono="555-1234",
        juegos_ids=[ObjectId(juego1_id), ObjectId(juego2_id),ObjectId(juego3_id)]
    )
    local1_id = local1.save(db)
    
    local2 = Local(
        nombre="Gamer's Paradise",
        direccion="Calle Secundaria 456",
        telefono="555-5678",
        juegos_ids=[ObjectId(juego2_id)]
    )
    local2_id = local2.save(db)


    local3 = Local(
        nombre="Game Station",
        direccion="2do nivel City mall",
        telefono="525-4654",
        juegos_ids=[ObjectId(juego3_id)]
    )
    local3_id = local3.save(db)
    
    # Actualizar relaciones
    juego1.locales_ids = [ObjectId(local1_id), ObjectId(local2_id), ObjectId(local3_id)]
    juego1.save(db)
    
    juego2.locales_ids = [ObjectId(local1_id), ObjectId(local2_id)]
    juego2.save(db)

    juego3.locales_ids = [ObjectId(local2_id), ObjectId(local3_id)]
    juego3.save(db)
    
    print("Local 1 ID:", local1_id)
    print("Local 2 ID:", local2_id)
    print("Local 3 ID", local3_id)
    print("Juego 1 ID:", juego1_id)
    print("Juego 2 ID:", juego2_id)
    print("Juego 3 ID", juego3_id)

if __name__ == "__main__":
    main()
