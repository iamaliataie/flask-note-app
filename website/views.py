from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)

@views.route('/new-note', methods=['GET', 'POST'])
@login_required
def new_note():
    if request.method == 'POST':
        form = request.form
        new_note = Note(body=form['body'], user=current_user.id)
        if new_note:
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('views.home'))
        else:
            flash('Something wrong happend. Please try again!')
    return render_template('new_note.html')