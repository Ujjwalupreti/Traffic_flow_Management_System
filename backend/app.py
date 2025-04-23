from flask import Flask, render_template, request, jsonify
from routes.simulation import simulation_bp, run_function
from datetime import datetime
from services.vehicle import Vehicle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(simulation_bp, url_prefix='/api/simulation/run')

@app.route('/api', methods=['POST','GET'])
def Get():
    vehicle_id = request.form.get('id')
    vehicle_type = request.form.get('type')
    dest = request.form.get('dest')
    date = request.form.get('date')
    date_str = datetime.strptime(date, "%Y-%m-%d")
    hour = int(request.form.get('hour'))
    day = int(date_str.day)
    month = int(date_str.month)
    year = int(date_str.year)
    if hour > 24 or day > 31 or month > 12:
        return jsonify({"error": "Invalid date/hour"})
    vehicle_detail = Vehicle(vehicle_id, vehicle_type,entry_point="bhimtal",destination=dest)
    
    return jsonify(run_function(day, month, year, hour))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
