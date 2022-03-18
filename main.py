# from typing import Optional
from fastapi import FastAPI, responses

app = FastAPI()


@app.get("/", response_class=responses.HTMLResponse)
def home():
    return """<html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <h1>Olá humano</h1>
        <body>
            <b>Esta é sua primeira api! </b>
            <p>Você poderá interagir com a api através dos links abaixo </p>

            <h2>Sumário</h2>
            <ol>
            <a href="/">index.html</a><br/>
            <a href="/hello">Your first Json</a><br/>
            <a href="/login/igor">try to login an user</a><br/>
            <a href="/login/igor/321">login with user and password</a><br/>
            <a href="/produto">List of products with basic information</a><br/>
            <a href="/produto/1">First product</a><br/>
            <a href="/produto/2">Second product</a><br/>
            <a href="/produto/3">Third product</a><br/>
            <a href="/produto/-1">Last product</a><br/>
            <a href="[POST] /pedido/igor/1/12">Buy 12 product with unauthorized user</a><br/>
            <a href="[POST] /pedido/admin/1/12">Buy 12 product with admin user</a><br/>
            <a href="[DELETE] /pedido/admin/4567890">Remove the order</a><br/>
            Dica, a parte de pedidos usa método POST, para acessá-la utilize o Postman ou a extensão Thunder Client
            <br/>
            Para excluir o pedido utilize o método [DELETE]
            </ol>

        </body>
    </html>"""


@app.get("/hello")
def hello():
    return {"Message": "Hello world"}


@app.get("/login/{usuario}")
def login(usuario: str):
    return {"usuário": usuario, "mensagem": "Digite sua senha", "url": f"http://localhost:8000/login/{usuario}/123456789"}


@app.get("/login/{usuario}/{senha}")
def login(usuario: str, senha: str):
    if senha == '123':
        return {"mensagem": f"Bem vindo {usuario}"}
    else:
        return {"mensagem": "Senha inválida"}


@app.get("/produto")
def produto():
    return [{"ref": 1,
        "nome": "Cadeira",
        "url": "/produto/1"
    }, {"ref": 2,
        "nome": "Sofá",
        "url": "/produto/2"
    }, {"ref": 3,
        "nome": "Almofada",
        "url": "/produto/3"
    }]

tabela = {
        1: {"ref": 1, "nome": "Cadeira", "preco": 366.50, "quantidade": 95},
        2: {"ref": 2, "nome": "Sofá", "preco": 960.90, "quantidade": 105},
        3: {"ref": 3, "nome": "Almofada", "preco": 95, "quantidade": 200}
    }

@app.get("/produto/{produto}")
def produto(produto: int):

    #isto é como um switch case no python    
    return tabela[produto]
  
#É por isso que python é a melhor linguagem para aprender
def CalcularPreco(produto):
    return tabela[produto].preco

def CalcularTotal(produto, quant):
    return CalcularPreco(produto) * quant

@ app.post("/pedido/{usuario}/{produto}/{quant}")
def pedido(usuario: str, produto: str, quant: int):
    if usuario != 'admin':
        return {"Erro": "Não autorizado"}

    return [{"Pedido aceito": "4567890"},
        {"Nome": produto,
        "Preco": CalcularPreco(produto),
        "Quant": quant,
        "Total": CalcularTotal(produto, quant)}]

def Existe(pedido):
    if pedido == "4567890":
        return True
    else:
        return False

@ app.delete("/pedido/{usuario}/{pedido}")
def pedido(usuario: str, pedido: str):
    if usuario != 'admin':
        return {"Erro": "Não autorizado"}

    if Existe(pedido):
        return [{"Pedido excluído": pedido}]
    else:
        return [{"Este pedido não foi encontrado": pedido}]
