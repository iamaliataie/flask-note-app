from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    notes = Note.query.filter_by(user=current_user.id).order_by(Note.id.desc())
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

@views.route('/delete-note/<note_id>', methods=['GET', 'POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({})
