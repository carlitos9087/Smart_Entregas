import sqlalchemy as sql
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base

connectionurl = 'postgresql://postgres:123@localhost:5432/postgres'

Base = declarative_base()

engine = sql.create_engine(connectionurl)

class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String)
    idade = Column(Integer)
    data_nascimento = Column(Date)

    def __repr__(self):
        return f'<Pessoa(nome={self.nome}, idade={self.idade}, data_nascimento={self.data_nascimento})>'

class Veiculo(Base):
    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    modelo = Column(String)
    ano = Column(Integer)
    placa = Column(String)

    def __repr__(self):
        return f'<Veiculo(modelo={self.modelo}, ano={self.ano}, placa={self.placa})>'

class Veiculo2(Base):
    __tablename__ = 'veiculos2'

    id = Column(Integer, primary_key=True)
    modelo = Column(String)
    ano = Column(Integer)
    placa = Column(String)
    carlitos = Column(String)

    def __repr__(self):
        return f'<Veiculo2(modelo={self.modelo}, ano={self.ano}, placa={self.placa}, carlitos={self.carlitos})>'

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

pessoa = Pessoa(nome='João', idade=30, data_nascimento='1990-01-01')
veiculo = Veiculo(modelo="carrooooo", ano=2000, placa="123648sd")
session.add(veiculo)
session.add(pessoa)
session.commit()

pessoas = session.query(Pessoa).all()

