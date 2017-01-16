#!flask/bin/python
from flask import Flask, jsonify
from app.models import Records

app = Flask(__name__)

@app.route('/learn/all', methods=['GET'])
def learn_all_route():
    record = Records.query.all()
    results = [ r.as_dict() for r in record ]
    return jsonify({'count': len(results), 'results': results})


#Example query is:    http://localhost:5000/learn/paste%20into%20vim
#at the moment we are just replacing all spaces with '%' for the LIKE query in SQL
#and searching the description for them. This might have to become more complex once
#we add more records, but for now it *seems* to be working
@app.route('/learn/<string:task_desc>', methods=['GET'])
def learn_desc_route(task_desc):
    record = Records.query.filter(Records.description.like("%"+task_desc.replace(" ","%")+"%")).all()
    results = [ r.as_dict() for r in record ]
    return jsonify({'count': len(results), 'results': results})

@app.route('/')
def index():
    return "hit /learn, isn't that neat"

if __name__ == '__main__':
    app.run(debug=True)
