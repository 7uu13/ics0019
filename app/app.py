from flask import jsonify, render_template, request, redirect, url_for
from config import app, db
from models import Kohvikud
from utils import load_cafes_from_csv

@app.route('/', methods=['GET', 'POST'])
def index():
    cafes = Kohvikud.query.all()
    return render_template('index.html', cafes=cafes)

@app.route('/search', methods=['GET'])
def get_cafe():
    query = request.args.get('query')
    if query:
        results = Kohvikud.query.filter(Kohvikud.time_open.like(f'%{query}%')).all()
    return render_template('index.html', results=results)

@app.route('/add_cafe', methods=['POST'])
def add_cafe():
    name = request.form.get('name')
    location = request.form.get('location')
    operator = request.form.get('operator')
    time_open = request.form.get('time_open')
    time_close = request.form.get('time_close')

    new_cafe = Kohvikud(
        name=name,
        location=location,
        operator=operator,
        time_open=time_open,
        time_close=time_close,
    )
    db.session.add(new_cafe)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/edit_cafe/<int:cafe_id>", methods=["GET"])
def edit_cafe(cafe_id):
    cafe_to_edit = Kohvikud.query.get(cafe_id)
    if not cafe_to_edit:
        return jsonify({"error": "Cafe not found"}), 404

    return render_template('index.html', cafe_to_edit=cafe_to_edit)

@app.route('/update_cafe/<int:cafe_id>', methods=["POST", "PUT"])
def update_cafe(cafe_id):
    cafe = Kohvikud.query.get(cafe_id)

    if not cafe:
        return jsonify({"error": "Cafe not found"}), 404

    if request.method == 'PUT':
        data = request.get_json()
        cafe.name = data.get('updated_item', cafe.name)
        cafe.location = data.get('location', cafe.location)
        cafe.operator = data.get('operator', cafe.operator)
        cafe.time_open = data.get('time_open', cafe.time_open)
        cafe.time_close = data.get('time_close', cafe.time_close)
    else:
        cafe.name = request.form.get('updated_item', cafe.name)
        cafe.location = request.form.get('location', cafe.location)
        cafe.operator = request.form.get('operator', cafe.operator)
        cafe.time_open = request.form.get('time_open', cafe.time_open)
        cafe.time_close = request.form.get('time_close', cafe.time_close)

    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_cafe/<int:cafe_id>', methods=['GET', 'DELETE'])
def delete_cafe(cafe_id):
    cafe = Kohvikud.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return jsonify({"success": False, "message": "Cafe not found"}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        load_cafes_from_csv('./data/Kohvikud.csv')
    app.run(debug=True)
