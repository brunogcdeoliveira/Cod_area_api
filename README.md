# Projeto cod_area_api (fastapi)

**Description:** o projeto cod_area_api visa a criação e o consumo de uma api onde os códigos de área para ligações DDD (discagem direta à distância) estão disponíveis para acessar, inserindo o código para receber a região onde aquele código atende.

## Instalar dependências
~~~
pip install -r requirements.txt
~~~

## Como rodar o projeto

* Utilixar o Uvicorn para subir o servidor
~~~
uvicorn main:app --reload
~~~
* Acessar o endpoint http://127.0.0.1:8000/docs para ver o swagger e testar os endpoints.


## Tarefas

- [ ] checar uf maiúsculo/minúsculo
- [ ] consumir esta api via script em python
- [ ] tratativa de erro para uf ou ddd que não exista (curso de tratativa de excessão e conhecer fastAPI)
- [ ] usar modelo do pydantic como response para melhorar a documentação
- [x] Criação dos primeiros testes