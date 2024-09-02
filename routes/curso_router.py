from fastapi import APIRouter

from fastapi import Response
from fastapi import Path

from fastapi import HTTPException
from fastapi import status

from models import Curso

router = APIRouter()

cursos = {
    1: {
        "titulo": "FastAPI - APIs Modernas e Assíncronas com Python",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 85,
        "horas": 23
    },
    3: {
        "titulo": "Machine Learning com AWS e Sagemaker",
        "aulas": 86,
        "horas": 16
    }
}

@router.get('/cursos')
async def get_cursos():
    return cursos


@router.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None, title='ID do curso', 
                                         description='Deve ser entre 1 e 2.', gt=0, lt=5)): #maior que 0 e menor que 5
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


@router.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    
    return curso


@router.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Não existe um curso com o id {curso_id}')


@router.delete ('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]

        return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Não existe um curso com o id {curso_id}')