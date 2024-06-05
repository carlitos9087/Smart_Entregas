import sqlalchemy as sql
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

connection_url = 'postgresql://postgres:123@localhost:5432/postgres'

Base = declarative_base()

engine = sql.create_engine(connection_url)

class Admin(Base):
    __tablename__ = 'admin'

    ID_Admin = Column(Integer, primary_key=True)
    Nome = Column(String)
    Senha = Column(String)
    Email = Column(String)

class Cliente(Base):
    __tablename__ = 'cliente'

    ID_Cliente = Column(Integer, primary_key=True)
    Nome = Column(String)
    Senha = Column(String)
    Endereco = Column(String)
    pacotes = relationship("Pacote")

class Pacote(Base):
    __tablename__ = 'pacote'

    ID_Pacote = Column(Integer, primary_key=True)
    Volume = Column(Float)
    Peso = Column(Float)
    Descricao = Column(String)
    ID_Cliente = Column(Integer, ForeignKey('cliente.ID_Cliente'))

class Remessa(Base):
    __tablename__ = 'remessa'

    ID_Remessa = Column(Integer, primary_key=True)
    ID_Pacote_1 = Column(Integer, ForeignKey('pacote.ID_Pacote'))
    ID_Pacote_2 = Column(Integer, ForeignKey('pacote.ID_Pacote'))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Inserting data
admin = Admin(Nome='Gleiber', Senha='naoesquecer', Email='gleiber@yahoo.com')
session.add(admin)

cliente1 = Cliente(Nome='Lucas', Senha='Roblox', Endereco='Rua Taurus, 520')
session.add(cliente1)

cliente2 = Cliente(Nome='Marcos', Senha='macarrao123', Endereco='Rua Outis, 25')
session.add(cliente2)

session.commit()
