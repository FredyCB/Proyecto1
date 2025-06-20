from dataclasses import dataclass, field #genera métodos especiales
from typing import List, Optional
from bson import ObjectId

@dataclass
class Juego:
    _id: Optional[ObjectId] = None
    titulo: str = ""
    genero: str = ""
    precio: float = 0.0
    locales_ids: List[ObjectId] = field(default_factory=list)

    def save(self, db): #Crea un diccionario local data, con los datos del juego
        juego_data = {
            "titulo": self.titulo,
            "genero": self.genero,
            "precio": self.precio,
            "locales_ids": self.locales_ids
        }
        
        if self._id is None: # Guarda el nuevo id como una nueva coleccion
            result = db.juegos.insert_one(juego_data)
            self._id = result.inserted_id
        else:
            db.juegos.update_one({"_id": self._id}, {"$set": juego_data})
        return str(self._id)
