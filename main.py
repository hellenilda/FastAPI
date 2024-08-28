from fastapi import FastAPI

app = FastAPI()

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