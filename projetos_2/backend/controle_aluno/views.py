from typing import List
from django.shortcuts import get_object_or_404
from ninja_extra import route, api_controller
from controle_aluno.models import Aluno, Endereco
from controle_aluno.schemas import (
    AlunoIn,
    AlunoOut,
    AlunoExcluido,
    EnderecoIn,
    EnderecoOut,
)

# Create your views here.

@api_controller("/controle_aluno",)
class ControleAlunosView:
    @route.get("/consultar-alunos", response=List[AlunoOut])
    def consultar_alunos(self):
        return Aluno.objects.all()
    
    @route.get("/consultar-alunos/{id}", response=AlunoOut)
    def consultar_aluno(self, id: int):
        return get_object_or_404(Aluno, id=id)


    @route.post("/criar-aluno", response=AlunoOut)
    def criar_aluno(self, data: AlunoIn): 
        aluno = Aluno.objects.create(**data.dict())
        return aluno
    
    @route.delete("/deletar-aluno/{id}", response=AlunoExcluido)
    def deletar_aluno(self, id: int):
        aluno = get_object_or_404(Aluno, id=id)
        aluno.delete()
        return {"mensagem": "aluno deletado com sucesso ", "id": id}
