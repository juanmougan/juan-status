from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/projects')
def projects():
	p = current_projects()
	return jsonify(p)

def current_projects():
	p1 = {
		'priority' : 1,
		'description' : 'Reading about Android',
		'topics' : ['mobile', 'Android', 'research']
	}
	p2 = {
		'priority' : 2,
		'description' : 'Create a separate frontend for QuePido app',
		'topics' : ['web-development', 'frontend', 'React']
	}
	p3 = {
		'priority' : 3,
		'description' : 'Some random Ruby stuff (and even Crystal)',
		'topics' : ['web-development', 'backend', 'Ruby', 'Crystal']
	}
	return [p1, p2, p3]
