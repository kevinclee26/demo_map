from flask import Flask, jsonify, render_template
import sqlalchemy as sql

app=Flask(__name__)

engine=sql.create_engine('sqlite:///data/db.sqlite')

@app.route('/data')
def return_data(): 
    results=engine.execute('select * from data').all()
    cali_shape_list=[]
    for each_result in results: 
        shape=eval(each_result[0])
        cali_shape_list.append(shape)
    return jsonify(cali_shape_list)

@app.route('/')
def home(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)