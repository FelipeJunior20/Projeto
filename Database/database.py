from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean

db = create_engine('sqlite:///Database/database.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#Tabelas

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    usuario = Column("usuario", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)

    def __init__(self, nome, email, usuario, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.ativo = ativo

Base.metadata.create_all(bind=db)