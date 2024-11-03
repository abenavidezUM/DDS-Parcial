from app.database import metadata, engine
from repositories.dna_repository import dna_record

def create_tables():
    metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()