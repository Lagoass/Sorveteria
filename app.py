from flask import Flask,request

sabores_lista = ['Pistache', 'Chocolate', 'Baunilha', 'Flocos']

app = Flask('Sorveteria Prato Feito')

@app.route("/")
def hello_world():
    return "<p>Hello, World! - Lagoa</p>"

@app.route("/sabores", methods=["GET"])
def sabores():
    dict_resp = {'sabores': sabores_lista}
    return dict_resp

@app.route("/adicionar_sabor", methods=["POST"])
def addSabor():
    # Forca a busca de qualquer json independente do tipo de informacao
    #request.get_json(force=True)

    request_data = request.json
    if 'sabor' not in request_data:
        return "Sabor não Informado", 400


    sabor = request_data['sabor']
    if sabor not in sabores_lista:
        sabores_lista.append(sabor)
    return "Sabor Adicionado"

@app.route("/apagar_sabor", methods=["Get"])
def DelSabor():
    if 'sabor' in request.args:
        arg_sabor = request.args.get('sabor')
        if arg_sabor not in sabores_lista:
            return "Sabor Nao encontrado", 404
        else:
            sabores_lista.remove(arg_sabor)
            return f"sabor {arg_sabor} removido com sucesso"
    else:
        return "Sabor nao informado"
    
@app.route("/sabor/<int:id_list>", methods=["GET"])
def sabor(id_list):
    if id_list in sabores_lista:
        sabor_id = sabores_lista[id_list]
    else:
        return "Id inexistente", 400
    return "True"

if __name__ == '__main__':
    app.run(debug=True)