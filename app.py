from models import db, Automobilis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def visi_automobiliai():
    query = request.args.get('search', '')

    if query:
        # Filter results based on the query
        automobiliai = Automobilis.query.filter(
            (Automobilis.gamintojas.like(f"%{query}%")) |
            (Automobilis.modelis.like(f"%{query}%")) |
            (Automobilis.spalva.like(f"%{query}%")) |
            (Automobilis.metai.like(f"%{query}%")) |
            (Automobilis.kaina.like(f"%{query}%"))
        ).all()
    else:
        # If no search query, display all cars
        automobiliai = Automobilis.query.all()

    return render_template('automobiliai.html', automobiliai=automobiliai, query=query)


@app.route('/automobiliai/<int:automobilio_id>')
def vienas_automobilis(automobilio_id):
    automobilis = Automobilis.query.get_or_404(automobilio_id)
    return render_template('automobilis.html', automobilis=automobilis)


@app.route('/automobiliai/prideti', methods=['GET', 'POST'])
def prideti_automobili():
    if request.method == 'POST':
        gamintojas = request.form['gamintojas']
        modelis = request.form['modelis']
        spalva = request.form['spalva']
        metai = int(request.form['metai'])
        kaina = float(request.form['kaina'])

        naujas_automobilis = Automobilis(
            gamintojas=gamintojas,
            modelis=modelis,
            spalva=spalva,
            metai=metai,
            kaina=kaina
        )
        db.session.add(naujas_automobilis)
        db.session.commit()
        return redirect(url_for('visi_automobiliai'))

    return render_template('prideti.html')


@app.route('/automobiliai/redaguoti/<int:automobilio_id>', methods=['GET', 'POST'])
def redaguoti_automobili(automobilio_id):
    automobilis = Automobilis.query.get_or_404(automobilio_id)

    if request.method == 'POST':
        automobilis.gamintojas = request.form['gamintojas']
        automobilis.modelis = request.form['modelis']
        automobilis.spalva = request.form['spalva']
        automobilis.metai = int(request.form['metai'])
        automobilis.kaina = float(request.form['kaina'])

        db.session.commit()
        return redirect(url_for('visi_automobiliai'))

    return render_template('redaguoti.html', automobilis=automobilis)


@app.route('/automobiliai/istrinti/<int:automobilio_id>', methods=['POST'])
def istrinti_automobili(automobilio_id):
    automobilis = Automobilis.query.get_or_404(automobilio_id)
    db.session.delete(automobilis)
    db.session.commit()
    return redirect(url_for('visi_automobiliai'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
