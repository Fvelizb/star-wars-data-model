import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    favoritos_planetas = relationship('FavoritoPlaneta', back_populates='usuario')
    favoritos_personajes = relationship('FavoritoPersonaje', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(250))
    clima = Column(String(120))
    poblacion = Column(String(120))

    favoritos = relationship('FavoritoPlaneta', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(250))
    genero = Column(String(120))
    especie = Column(String(120))
    favoritos = relationship('FavoritoPersonaje', back_populates='personaje')

class FavoritoPlaneta(Base):
    __tablename__ = 'favorito_planeta'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='favoritos_planetas')
    planeta = relationship('Planeta', back_populates='favoritos')

class FavoritoPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='favoritos_personajes')
    personaje = relationship('Personaje', back_populates='favoritos')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
