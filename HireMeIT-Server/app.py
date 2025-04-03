from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import mimetypes
# import os

app = Flask(__name__, static_folder="../HireMeIT-Client/dist", static_url_path="/")

# port = int(os.getenv("PORT", 5000))

mimetypes.add_type("application/javascript", ".js")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    company_description = db.Column(db.Text, nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Job {self.title}>"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("dist", path)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{
        'id': job.id,
        'title': job.title,
        'type': job.type,
        'description': job.description,
        'location': job.location,
        'salary': job.salary,
        'company': {
            'name': job.company_name,
            'description': job.company_description,
            'contactEmail': job.contact_email,
            'contactPhone': job.contact_phone
        }
    } for job in jobs])

@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    new_job = Job(
        title=data['title'],
        type=data['type'],
        description=data['description'],
        location=data['location'],
        salary=data['salary'],
        company_name=data['company']['name'],
        company_description=data['company']['description'],
        contact_email=data['company']['contactEmail'],
        contact_phone=data['company']['contactPhone']
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully'}), 201

@app.route('/api/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully'})

@app.route('/api/jobs/<int:id>', methods=['GET'])
def get_job_by_id(id):
    job = Job.query.get_or_404(id)
    return jsonify({
        'id': job.id,
        'title': job.title,
        'type': job.type,
        'description': job.description,
        'location': job.location,
        'salary': job.salary,
        'company': {
            'name': job.company_name,
            'description': job.company_description,
            'contactEmail': job.contact_email,
            'contactPhone': job.contact_phone
        }
    })
    
@app.route('/api/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    data = request.get_json()
    job = Job.query.get_or_404(id)
    job.title = data['title']
    job.type = data['type']
    job.description = data['description']
    job.location = data['location']
    job.salary = data['salary']
    job.company_name = data['company']['name']
    job.company_description = data['company']['description']
    job.contact_email = data['company']['contactEmail']
    job.contact_phone = data['company']['contactPhone']
    db.session.commit()
    return jsonify({'message': 'Job updated successfully'})

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=port, debug=True)
    app.run(debug=True)