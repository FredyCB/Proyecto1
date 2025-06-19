from dataclasses import dataclass, field
from typing import List, Optional
from bson import ObjectId

@dataclass
class Juego:
    _id: Optional[ObjectId] = None
    titulo: str = ""
    genero: str = ""
    precio: float = 0.0
    locales_ids: List[ObjectId] = field(default_factory=list)

    def save(self, db):
        juego_data = {
            "titulo": self.titulo,
            "genero": self.genero,
            "precio": self.precio,
            "locales_ids": self.locales_ids
        }
        
        if self._id is None:
            result = db.juegos.insert_one(juego_data)
            self._id = result.inserted_id
        else:
            db.juegos.update_one({"_id": self._id}, {"$set": juego_data})
        
        return str(self._id)