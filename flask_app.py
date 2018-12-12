from flask import Flask, request, redirect, render_template
import sys

# sys.path.insert(1, "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (1.0.2)")

app = Flask(__name__)

# TODO: MAIN FLOWER LISTINGS, NEEDS TO SEE FIRST 10 OF SIGHTINGS
@app.route('/')
def sql_database():
    from functions.sqlquery import sql_query, sql_query3
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_results = sql_query3('''SELECT * FROM SIGHTINGS WHERE NAME='Draperia' ORDER BY SIGHTED DESC''', 10)
    sightings_table = sql_query('''SELECT * FROM Sightings''')

    return render_template('sqldatabase.html', 
    	sightings_results=sightings_results,
    	sightings_table=sightings_table,
    	flowers_table=flowers_table)

# TODO: REFINE QUERY TO BE MORE ROBUST
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        name = request.form['name']
        person = request.form['person']
        location = request.form['location']
        sighted = request.form['sighted']
        # TODO: SET THIS EQUAL TO SOMETHING MAYBE IT'LL WORK
        sql_edit_insert(''' INSERT OR REPLACE INTO Sightings (name,person,location,sighted) VALUES (?,?,?,?) ''', (name,person,location,sighted) )
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_table = sql_query('''SELECT * FROM Sightings''')

    return render_template('sqldatabase.html', 
    	sightings_table=sightings_table,
    	flowers_table=flowers_table) 

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
    	egenus = request.args['egenus']
    	especies = request.args['especies']
    	ecomname = request.args['ecomname']
    	eresults = sql_query2(''' SELECT * FROM Flowers WHERE genus = ? AND species = ? ''',(egenus,especies))
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    return render_template('sqldatabase.html', 
    	eresults=eresults,
    	flowers_table=flowers_table)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query, sql_query3
    if request.method == 'POST':
    	old_genus = request.form['old_genus']
    	old_species = request.form['old_species']
    	old_comname = request.form['old_comname']
    	genus = request.form['genus']
    	species = request.form['species']
    	comname = request.form['comname']
    	# eresults = sql_query2(''' SELECT * FROM Flowers WHERE genus = ? AND species = ? ''',(genus,species))

    	sql_edit_insert(''' UPDATE Flowers set genus=?,species=?,comname=? WHERE genus=? and species=? and comname=?''', (genus,species,comname,old_genus,old_species, old_comname) )
    flowers_table = sql_query('''SELECT * FROM Flowers''')
    sightings_results = sql_query3('''SELECT * FROM SIGHTINGS WHERE NAME='Draperia' ORDER BY SIGHTED DESC''', 10)
    return render_template('sqldatabase.html', 
    	sightings_results=sightings_results,
    	flowers_table=flowers_table)

# @app.route('/sightings', methods = ['POST', 'GET'])
# def sql_sightingslist():
# 	from functions.sql_query import sql_query3, sql_query
# 	if request.method == 'GET':
# 		comname = request.args.get('comname')
# 		sightings_results = sql_query3('''SELECT * FROM SIGHTINGS WHERE NAME=? ORDER BY SIGHTED DESC''', (comname), 10)
# 	flowers_table = sql_query('''SELECT * FROM Flowers''')
# 	return render_template('sql_database.html',
# 		sightings_results=sightings_result,
# 		flowers_table=flowers_table)

if __name__ == "__main__":
    app.run(debug=True)

