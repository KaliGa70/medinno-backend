from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from ..models.names import Names
from .. import db

def get_all_names() -> list[Names]:
    return Names.query.all()

def create_name(
    first_name: str,
    middle_name: str | None,
    last_name: str,
    second_last_name: str | None
) -> Names:
    # Validación mínima
    if not first_name or not last_name:
        raise ValueError("Los campos 'first_name' y 'last_name' son obligatorios.")
    
    new_name = Names(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        second_last_name=second_last_name,
        created_at=datetime.utcnow()
    )

    try:
        db.session.add(new_name)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise RuntimeError("Error al crear el nombre en la base de datos.") from e

    return new_name
