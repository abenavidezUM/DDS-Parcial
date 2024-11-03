from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData
from app.database import metadata, database

dna_record = Table(
    'dna_record',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('dna_sequence', String, unique=True, nullable=False),
    Column('is_mutant', Boolean, nullable=False)
)

async def get_dna_record(dna_sequence):
    query = dna_record.select().where(dna_record.c.dna_sequence == dna_sequence)
    return await database.fetch_one(query)

async def save_dna_record(dna_sequence, is_mutant):
    query = dna_record.insert().values(dna_sequence=dna_sequence, is_mutant=is_mutant)
    await database.execute(query)

async def count_mutants():
    query = dna_record.select().where(dna_record.c.is_mutant == True)
    return len(await database.fetch_all(query))

async def count_humans():
    query = dna_record.select().where(dna_record.c.is_mutant == False)
    return len(await database.fetch_all(query))
