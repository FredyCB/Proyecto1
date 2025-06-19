from dataclasses import dataclass, field
from typing import List, Optional
from bson import ObjectId

@dataclass
class Local:
    _id: Optional[ObjectId] = None
    nombre: str = ""
    direccion: str = ""
    telefono: str = ""
    juegos_ids: List[ObjectId] = field(default_factory=list)

    def save(self, db):
        local_data = {
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "juegos_ids": self.juegos_ids
        }
        
        if self._id is None:
            result = db.locales.insert_one(local_data)
            self._id = result.inserted_id
        else:
            db.locales.update_one({"_id": self._id}, {"$set": local_data})
        
        return str(self._id)
