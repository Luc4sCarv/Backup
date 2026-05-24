from typing import Optional
from ninja import Schema
from .models import Aluno

# 1. Defina o Schema para o Aluno
class AlunoOut(Schema):
    id: int
    matricula: str
    nome_aluno: str
    email: Optional[str]
    nome_mae: Optional[str] # Nota: No seu model está FloatField, é isso mesmo?
    # Se quiser o ID do endereço:
    endereco_id: Optional[int] = None

class AlunoIn(Schema):
    matricula: str
    nome_aluno: str
    email: Optional[str]
    nome_mae: Optional[str] 
    endereco_id: Optional[int] = None

class AlunoExcluido(Schema):
    mensagem: str
    id: int

from typing import Optional
from ninja import Schema

# Schemas de Aluno já criados por você omitidos para brevidade...

class EnderecoIn(Schema):
    cep: str
    endereco: str
    bairro: Optional[str] = None
    cidade: str
    estado: str
    regiao: Optional[str] = None

class EnderecoOut(Schema):
    id: int
    cep: str
    endereco: str
    bairro: Optional[str] = None
    cidade: str
    estado: str
    regiao: Optional[str] = None