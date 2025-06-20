import unittest
import urllib.parse
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
import urllib
from classes.local import Local
from classes.juego import Juego

load_dotenv()

class TestModelo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar conexión de prueba
        cls.uri = "mongodb+srv://fcardonabanegas:" + urllib.parse.quote("Creeper@5") +  "@cluster0.cqmsaac.mongodb.net/"
        cls.client = MongoClient(cls.uri)
        cls.db = cls.client["videojuegos_test_db"]
    
    @classmethod
    def tearDownClass(cls):
        # Limpiar base de datos de prueba
        cls.client.drop_database("videojuegos_test_db")
        cls.client.close()
    
    def test_crear_local_y_juego(self):
        # Crear juego
        juego = Juego(titulo="The Witcher 3", genero="RPG", precio=29.99)
        juego_id = juego.save(self.db)
        self.assertIsNotNone(juego_id)
        
        # Crear local
        local = Local(
            nombre="Local de Prueba",
            direccion="Calle Test 123",
            telefono="555-0000",
            juegos_ids=[ObjectId(juego_id)]
        )
        local_id = local.save(self.db)
        self.assertIsNotNone(local_id)
        
        # Verificar relación
        juego_recuperado = self.db.juegos.find_one({"_id": ObjectId(juego_id)})
        self.assertIn(ObjectId(local_id), juego_recuperado["locales_ids"]) # type: ignore
        
        local_recuperado = self.db.locales.find_one({"_id": ObjectId(local_id)})
        self.assertIn(ObjectId(juego_id), local_recuperado["juegos_ids"]) # type: ignore

if __name__ == "__main__":
    unittest.main()
