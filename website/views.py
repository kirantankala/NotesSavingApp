#routes and views for the website
#other than authentication
#this is the blueprint for the website and have bunch of routes and urls

from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
 

views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST']) #this is the end point for the home page
#so whenever the user goes to this url he redirects to home page and this function is called
@login_required 
def home():#this is the function that is called when the user goes to the home page
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html",user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/edit-note/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash("You don't have permission to edit this note.", category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        note.data = request.form['content']
        db.session.commit()
        flash('Note updated successfully!', category='success')
        return redirect(url_for('views.home'))

    return render_template('edit.html', note=note, user=current_user)
