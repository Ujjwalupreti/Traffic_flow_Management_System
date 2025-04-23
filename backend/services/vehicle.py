class Vehicle:
    def __init__(self,vehicle_id,vehicle_type,entry_point,destination):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.curr_position = entry_point
        self.destination = destination
        self.route = []
        self.status = -1
        
    def assign_route(self,route):
        self.route=route
        self.status=1
    
    def update_position(self,dest):
        self.curr_position = dest  
        if dest == self.destination:
            self.status = 2      
         
    def to_dict(self):
        return{
            "vehile_id":self.vehicle_id,
            "vehile_type":self.vehicle_type,
            "destination":self.destination,
            "routes":self.route,
            "current_position":self.curr_position,
            "status":self.status
        }