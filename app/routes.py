from flask import render_template, request, redirect
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    edit_user = None

    if request.method == 'POST':
        user_id = request.form.get('id')
        name = request.form['name']
        language = request.form['language']

        if user_id:  # Bagian Edit
            user = User.query.get_or_404(user_id)
            user.name = name
            user.language = language
        else:  # Bagian Tambah
            new_user = User(name=name, language=language)
            db.session.add(new_user)

        db.session.commit()
        return redirect('/')

    edit_id = request.args.get('edit')
    if edit_id:
        edit_user = User.query.get_or_404(edit_id)

    users = User.query.all()
    return render_template('index.html', users=users, edit_user=edit_user)

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')
