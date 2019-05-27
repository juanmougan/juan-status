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
		'description' : 'A web scraper example using Python',
		'topics' : ['webscraping', 'Python']
	}
	p2 = {
		'priority' : 2,
		'description' : 'Reading about Android',
		'topics' : ['mobile', 'Android', 'research']
	}
	p3 = {
		'priority' : 3,
		'description' : 'Create a separate frontend for QuePido app',
		'topics' : ['web-development', 'frontend', 'React']
	}
	p4 = {
		'priority' : 4,
		'description' : 'Some random Ruby stuff (and even Crystal)',
		'topics' : ['web-development', 'backend', 'Ruby', 'Crystal']
	}
	return [p1, p2, p3, p4]
