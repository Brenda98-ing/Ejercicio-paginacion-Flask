
from flask import request, jsonify, Blueprint
from http import HTTPStatus

from resources import paginacion


v = Blueprint('routes', __name__)

@v.route('/ejercicio', methods=['GET','OPTIONS'])
def ejercicio():
    #Indicamos el nombre de la variable
    id_inicia=request.args.get('id_inicia')
    id_termina=request.args.get('id_termina')

    #Lo mostramos de referencia
    print(id_inicia)

    headers = {'content-type': 'application/json'}
    
    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT)

    if request.method == 'GET':
        response,http_code = paginacion.get_paginated_list(paginacion.llama_lista(), id_inicia,id_termina)
        
    http_code= HTTPStatus.OK   
    return (response, http_code,headers)



