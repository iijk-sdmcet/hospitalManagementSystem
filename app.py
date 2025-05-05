from flask import Flask, render_template, request, redirect
from models import db, Patient, Doctor, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        db.session.add(Patient(name=name, age=age))
        db.session.commit()
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        db.session.add(Appointment(patient_id=patient_id, doctor_id=doctor_id))
        db.session.commit()
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
