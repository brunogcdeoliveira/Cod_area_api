# TODO
# chevar uf maiúsculo/minúsculo
# consumir esta api via script em python
# tratativa de erro para uf ou ddd que não exista (curso de tratativa de excessão e conhecer fastAPI)
# usar modelo do pydantic como response para melhorar a documentação

from fastapi import FastAPI
from ddd import DDD_REGIAO

app = FastAPI()


def busca_ddd_uf(uf: str):
    lista_resultados = []
    for ddd in DDD_REGIAO.keys():
        if uf == DDD_REGIAO[ddd]["uf"]:
            # print(uf , DDD_REGIAO[ddd]["regiao"], ddd)
            lista_resultados.append({"regiao": DDD_REGIAO[ddd]["regiao"], "ddd": ddd})
    return lista_resultados


# /busca_ddd/{uf}
@app.get("/busca_ddd/{uf}")
def busca_ddd(uf: str):
    resultados = busca_ddd_uf(uf)

    return {
        "uf_recebida": uf,
        "resultados": resultados,
    }


# /busca_uf/{ddd}
@app.get("/busca_uf/{ddd}")
def busca_uf(ddd: int):
    return {
        "ddd_recebido": ddd,
        "uf": DDD_REGIAO[ddd]["uf"],
        "regiao": DDD_REGIAO[ddd]["regiao"]
    }
    # unpacking diccionary (outra forma)
    # return {
    #     "ddd_recebido": ddd,
    #     **DDD_regiaoS[ddd],
    # }


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/mensagem")
def mensagem():
    return {"message": "mensagem"}


@app.get("/bruno")
def bruno():
    return {"name": "Bruno"}


@app.get("/items/{item_id}")
def read_item(item_id):
    return {"cocacola": item_id}