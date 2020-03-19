from flask import Blueprint, current_app, request, jsonify, render_template, url_for
from .model import Timeline
from .serealizer import TimelineSchema

timeline_bp = Blueprint('timeline', __name__, template_folder='static')

@timeline_bp.route('/')
def index():
    return render_template("index.html")

@timeline_bp.route('/mostrar', methods = ['GET'])
def mostrar():
    ts = TimelineSchema(many=True)

    result = Timeline.query.all()
    return ts.jsonify(result), 200

@timeline_bp.route('/cadastrar', methods = ['POST'])
def cadastrar():
    ts = TimelineSchema()
    
    timeline = ts.load(request.json)
    
    current_app.db.session.add(timeline)
    current_app.db.session.commit()
    return jsonify("Cadastro efetuado com sucesso!"), 201
    # return ["testando"], 200

@timeline_bp.route('/deletar/<id>', methods = ['GET'])
def deletar(id):
    if(Timeline.query.filter(Timeline.id == id).delete()):
        current_app.db.session.commit()
        return jsonify("Deletado!" ), 200
    else:
        return jsonify("Id não existente, nenhum registro deletado!"), 200


@timeline_bp.route('/modificar/<id>', methods = ['POST'])
def modificar(id):

    q = Timeline.query.filter(Timeline.id == id)
    if(q.update(request.json)):
        current_app.db.session.commit()
        return jsonify("Registro modificado com sucesso!"), 201
    else:
        return jsonify("Id não existente, nenhum resgitro modificado!"), 200

@timeline_bp.route('/autocomplete', methods = ['POST'])
def autocomplete():
    ts = TimelineSchema(many=True)
    json = request.form['string']
    if(len(json) >= 2):
        filtro = Timeline.event.like(json+"%")
        search = Timeline.query.filter(filtro)
        return ts.jsonify(search), 200
    else:
        return ts.jsonify({}), 200

@timeline_bp.route('/autocompletejson', methods = ['POST'])
def autocompletejson():
    ts = TimelineSchema(many=True)
    json = request.json
    if(len(json) >= 2):
        filtro = Timeline.event.like(json+"%")
        search = Timeline.query.filter(filtro)
        return ts.jsonify(search), 200
    else:
        return ts.jsonify({}), 200