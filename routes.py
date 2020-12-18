from flask import Flask, request
import sqlite3
import logging
import csv

app = Flask(__name__)
conn = sqlite3.connect("feiras.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS feira (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    longitude BIGINT NOT NULL,
    latitude BIGINT NOT NULL,
    setorCensitario BIGINT NOT NULL,
    areaPonderacao BIGINT NOT NULL,
    codigoDistrito INTEGER NOT NULL,
    distrito TEXT NOT NULL,
    codigoSubprefeitura INTEGER NOT NULL,
    subprefeitura TEXT NOT NULL,
    regiao05 TEXT NOT NULL,
    regiao08 TEXT NOT NULL,
    nomeFeira TEXT NOT NULL,
    registro TEXT NOT NULL UNIQUE,
    logradouro TEXT NOT NULL,
    numero TEXT NOT NULL,
    bairro TEXT NOT NULL,
    referencia TEXT NOT NULL
);
""")

with open("DEINFO_AB_FEIRASLIVRES_2014.csv", "r") as data:
    csv_reader = csv.reader(data, delimiter=",")
    try:
        for row in csv_reader:
            if row[0] == "ID":
                continue
            fields = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16])
            cursor.execute(f"""
INSERT INTO feira (id, longitude, latitude, setorCensitario, areaPonderacao, codigoDistrito, distrito, codigoSubprefeitura, subprefeitura, regiao05, regiao08, nomeFeira, registro, logradouro, numero, bairro, referencia)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" , fields)
            conn.commit()
    except:
        pass

@app.route("/api/1.0.0/post", endpoint="post", methods=["POST"])
@app.route("/api/1.0.0/get", endpoint="get", methods=["GET"])
@app.route("/api/1.0.0/delete", endpoint="delete", methods=["DELETE"])
@app.route("/api/1.0.0/update", endpoint="update", methods=["PATCH"])
def api():
    if request.endpoint == "get":
        cursor.execute("SELECT * FROM feira")
        row = cursor.fetchall()
        json = request.json
        for x in range(0, len(row)):
            try:
                if json.get("distrito") == row[x][6] and json.get("regiao05") == row[x][9] and json.get("nomeFeira") == row[x][11] and json.get("bairro") == row[x][15]:
                    return ({
                        "id": row[x][0],
                        "longitude": row[x][1],
                        "latitude": row[x][2],
                        "setorCensitario": row[x][3],
                        "areaPonderacao": row[x][4],
                        "codigoDistrito": row[x][5],
                        "distrito": row[x][6],
                        "codigoSubprefeitura": row[x][7],
                        "subprefeitura": row[x][8],
                        "regiao05": row[x][9],
                        "regiao08": row[x][10],
                        "nomeFeira": row[x][11],
                        "registro": row[x][12],
                        "logradouro": row[x][13],
                        "numero": row[x][14],
                        "bairro": row[x][15],
                        "referencia": row[x][16]
                    }, 200)
            except Exception as e:
                return {"message": "error", "error": str(e)}, 400
        return {"error": "usuário não encontrado"}, 404
    elif request.endpoint == "post":
        json = request.json
        try:
            fields = (json.get("id"), json.get("longitude"), json.get("latitude"), json.get("setorCensitario"), json.get("areaPonderacao"), json.get("codigoDistrito"), json.get("distrito"), json.get("codigoSubprefeitura"), json.get("subprefeitura"), json.get("regiao05"), json.get("regiao08"), json.get("nomeFeira"), json.get("registro"), json.get("logradouro"), json.get("numero"), json.get("bairro"), json.get("referencia"))
            cursor.execute(f"""
            INSERT INTO feira (id, longitude, latitude, setorCensitario, areaPonderacao, codigoDistrito, distrito, codigoSubprefeitura, subprefeitura, regiao05, regiao08, nomeFeira, registro, logradouro, numero, bairro, referencia)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", fields)
            conn.commit()
            return {"message": "ok"}
        except Exception as e:
            return ({"message": "error", "error": str(e)}, 400)
    elif request.endpoint == "delete":
        json = request.json
        try:
            data = (json.get("id"), json.get("bairro"))
            cursor.execute("""
            DELETE FROM feira
            WHERE ID = ? AND bairro = ?
            """, data)
            conn.commit()
            return {"message": "ok"}
        except Exception as e:
            return ({"message": "error", "error": str(e)}, 400)
    elif request.endpoint == "update":
        json = request.json
        fields = (json.get("longitude"), json.get("latitude"), json.get("setorCensitario"), json.get("areaPonderacao"), json.get("codigoDistrito"), json.get("distrito"), json.get("codigoSubprefeitura"), json.get("subprefeitura"), json.get("regiao05"), json.get("regiao08"), json.get("nomeFeira"), json.get("logradouro"), json.get("numero"), json.get("bairro"), json.get("referencia"), json.get("id"), json.get("registro"))
        cursor.execute("""
        UPDATE feira
        SET longitude = ?, latitude = ?, setorCensitario = ?, areaPonderacao = ?, codigoDistrito = ?, distrito = ?, codigoSubprefeitura = ?, subprefeitura = ?, regiao05 = ?, regiao08 = ?, nomeFeira = ?, logradouro = ?, numero = ?, bairro = ?, referencia = ?
        WHERE id = ? AND registro = ?
        """, fields)
        if cursor.rowcount == 1:
            conn.commit()
            return {"message": "ok"}
        else:
            return {"message": "error"}, 400

logging.basicConfig(filename="demo.log", level=logging.DEBUG)
app.run()
