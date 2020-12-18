from flask import Flask, request
import csv

app = Flask(__name__)

@app.route("/api/1.0.0/get/<neighborhood>")
def get(neighborhood):
    if request.method == "GET":
        with open("DEINFO_AB_FEIRASLIVRES_2014.csv", "r") as data:
            csv_reader = csv.reader(data, delimiter=",")
            for row in csv_reader:
                if row[15] == neighborhood:
                    return ({
                        "id": row[0],
                        "longitude": row[1],
                        "latitude": row[2],
                        "setorCensitario": row[3],
                        "areaPonderacao": row[4],
                        "codigoDistrito": row[5],
                        "distrito": row[6],
                        "subprefeitura": row[7],
                        "codigoSubprefeitura": row[8],
                        "regiao05": row[9],
                        "regiao08": row[10],
                        "nomeFeira": row[11],
                        "registro": row[12],
                        "logradouro": row[13],
                        "numero": row[14],
                        "bairro": row[15],
                        "referencia": row[16]
                    }, 200)
        return {"error": "usuário não encontrado"}, 404

@app.route("/api/1.0.0/put/<info>")
def put(info):
    if request.method == "PUT":
        pass

@app.route("/api/1.0.0/post/<data>")
def post(data):
    if request.method == "POST":
        pass

@app.route("/api/1.0.0/delete/<data>")
def delete(data):
    if request.method == "DELETE":
        pass

app.run()
