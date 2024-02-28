from sqlalchemy import Column, Integer, String, SmallInteger, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    
    company_id = Column(Integer, primary_key=True)
    commercial_name = Column(String(100), nullable=False)
    contact_person_id = Column(Integer)
    status = Column(SmallInteger, default=1)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    created_by = Column(Integer)
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    updated_by = Column(Integer)
    
    # Define las restricciones de clave externa si es necesario
    # ForeignKey('persons.person_id') debe ajustarse según la tabla de referencia real y la columna
    contact_person = Column(Integer, ForeignKey('persons.person_id'))

    # Otras relaciones referenciadas por esta tabla se pueden definir aquí si es necesario
    # Por ejemplo, si tienes una tabla llamada "doctors" que referencia a "companies", podrías agregar:
    # doctors = relationship('Doctor', back_populates='company')

    # Para relaciones inversas, si la tabla "doctors" tiene una columna llamada "company_id" que hace referencia a "companies":
    # Otra opción sería definir una relación inversa en la clase "Doctor" con:
    # company = relationship('Company', back_populates='doctors')