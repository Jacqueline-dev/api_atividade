from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey)
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.bb', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocmmit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format((self.nome))


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoas)

