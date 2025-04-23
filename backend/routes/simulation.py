import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.train_model import Train_Model
from flask import Blueprint

simulation_bp = Blueprint('simulation',__name__)
    
@simulation_bp.route("/api/simulation/run",methods=['GET'])
def run_function(hour=0,day=1,month=1,year=2025):
    prediction = Train_Model.predict_traffic(day,month,year,hour)
    if prediction<=249:
        return {"status":"Not Busy","score":prediction.tolist()}
    else:
        return {"status":"Busy","score":prediction.tolist()}

if __name__ == "__main__":
    run_function()