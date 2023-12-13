from flask import render_template, redirect, request
from app_flask.models.users_models import Ninja
from app_flask.models.users_models import Dojo
from app_flask import app

@app.route('/')
@app.route('/dojos')

def dojos():
    
    dojos_list = Dojo.get_all_dojos()
    
    return render_template('dojos.html', dojos_list = dojos_list)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    
    data = {
        'name': request.form['name']
    }
    
    Dojo.create_dojo(data)
    
    return redirect('/dojos')


@app.route('/ninjas')
def ninjas():
    
    dojos_list = Dojo.get_all_dojos()
    
    return render_template('ninjas.html', dojos_list = dojos_list)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
        
    Ninja.create_ninja(data)
        
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo_and_ninja(id):
    
    data = {
        'id': id
    }
    
    ninja_list = Ninja.obtain_dojo_and_ninjas(data)
    
    
    dojo = Dojo.obtain_one_dojo(data)
    
    return render_template('show.html', ninja_list = ninja_list, dojo = dojo)