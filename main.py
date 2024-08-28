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

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host = '127.0.0.1', port = 8000, debug = True)