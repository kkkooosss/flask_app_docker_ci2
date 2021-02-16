#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import make_response

import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return pretty_json({
        "resources": {
            "matrix": "/matrix/<matrix>",
            "column": "/columns/<matrix>/<column_number>",
            "row": "/rows/<matrix>/<row_number>",
        },
        "current_uri": "/",
        "example": "/matrix/'123n456n789'",
    })


@app.route("/matrix/<matrix>", methods=['GET'])
def matrix(matrix):
    b = matrix.split('n')
    m = '\n'.join(b)
    return m

    # TODO: return matrix, each row in a new line


@app.route("/columns/matrix/<matrix>/<column_number>", methods=['GET'])
def column(matrix, column_number):
    c = matrix.split('n')
    z = int(column_number)
    a = c[z]
    column = []
    for i in range(len(c)):
        for j in range(len(c[i])):
            R = (c[i][z])
        column.append(R)
    column = ' '.join(column)
    print(column)
    # TODO: return column based on given column number
    return str(column)


@app.route("/rows/matrix/<matrix>/<row_number>", methods=['GET'])
def row(matrix, row_number):
    b = matrix.split('n')
    z = int(row_number)
    a = b[z]
    a = ' '.join(a)
    print("a = " + a)
    print(type(a))
    # TODO: return row based on given row number
    return a


def pretty_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


if __name__ == "__main__":
    app.run(port=5000)

