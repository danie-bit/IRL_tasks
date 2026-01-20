from flask import Flask, render_template, request, redirect, flash
from models import db, URLModel
import validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SECRET_KEY'] = 'mysecretkey123'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    shortened_url = None

    if request.method == 'POST':
        original = request.form.get('url')

        if not validators.url(original):
            flash("Please enter a valid URL (include http:// or https://)")
            return redirect('/')

        found_url = URLModel.query.filter_by(original_url=original).first()
        if found_url:
            new_entry = found_url
        else:
            new_entry = URLModel(original_url=original)
            db.session.add(new_entry)
            db.session.commit()

        shortened_url = request.host_url + new_entry.short_code

    return render_template('index.html', short_link=shortened_url)

@app.route('/history')
def history():
    all_urls = URLModel.query.all()
    return render_template('history.html', urls=all_urls)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    link = URLModel.query.filter_by(short_code=short_code).first_or_404()
    return redirect(link.original_url)

if __name__ == '__main__':
    app.run(debug=True)
