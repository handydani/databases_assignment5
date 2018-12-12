from flask import Flask, request, redirect, render_template
import sys

# sys.path.insert(1, "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (1.0.2)")

app = Flask(__name__)

# TODO: MAIN FLOWER LISTINGS, ON CLICK NEEDS TO SEE FIRST 10 OF SIGHTINGS
@app.route('/')
def sql_database():
    from functions.sqlquery import sql_query
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_table = sql_query('''SELECT * FROM Sightings''')
    features_table = sql_query('''SELECT * FROM Features''')
    # msg = 'SELECT * FROM Flowers'
    return render_template('sqldatabase.html', 
    	flowers_table=flowers_table, 
    	sightings_table=sightings_table, 
    	features_table=features_table)

# TODO: INSERT ON SIGHTINGS TABLE 
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        name = request.form['name']
        person = request.form['person']
        location = request.form['location']
        sighted = request.form['sighted']
        sql_edit_insert(''' INSERT OR REPLACE INTO Sightings (name,person,location,sighted) VALUES (?,?,?,?) ''', (name,person,location,sighted) )
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_table = sql_query('''SELECT * FROM Sightings''')
    features_table = sql_query('''SELECT * FROM Features''')
    return render_template('sqldatabase.html', 
    	flowers_table=flowers_table, 
    	sightings_table=sightings_table, 
    	features_table=features_table) 

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        egenus = request.args.get('genus')
        especies = request.args.get('species')
        ecomname = request.args.get('comname')
        eresults = sql_query2(''' SELECT * FROM Flowers WHERE genus = ? AND species = ? ''',(egenus,ecomname))
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_table = sql_query('''SELECT * FROM Sightings''')
    features_table = sql_query('''SELECT * FROM Features''')
    return render_template('sqldatabase.html', 
    	eresults=eresults,
    	flowers_table=flowers_table, 
    	sightings_table=sightings_table, 
    	features_table=features_table)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
    	old_genus = request.form['old_genus']
    	old_species = request.form['old_species']
    	old_comname = request.form['old_comname']
    	genus = request.form['genus']
    	species = request.form['species']
    	comname = request.form['comname']
    	sql_edit_insert(''' UPDATE Flowers set genus=?,species=?,comname=? WHERE genus=? and species=? and comname=?''', (genus,species,comname,old_genus,old_species, old_comname) )
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_table = sql_query('''SELECT * FROM Sightings''')
    features_table = sql_query('''SELECT * FROM Features''')
    return render_template('sqldatabase.html', 
    	flowers_table=flowers_table, 
    	sightings_table=sightings_table, 
    	features_table=features_table)

if __name__ == "__main__":
    app.run(debug=True)

