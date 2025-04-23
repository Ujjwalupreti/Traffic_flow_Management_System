from collections import defaultdict
class TrafficBalancer:
    def __init__(self):
        self.queues = defaultdict(list)
    
    def add_vehicle_to_queue(self,node,vehicle_id):
        self.queues[node].append(vehicle_id)
    
    def get_next_vehicle(self,node):
        if(self.queues[node]):
            vehicle_id = self.queues[node].pop(0)
            return vehicle_id
        return None    
    
    def get_queue_status(self):
        return {node:len(queue) for node,queue in self.queues.items()}
    
    def clear_all_load(self):
        self.queue.clear()
    
    def balance_load(self,vehicle_routes):
        node_load = defaultdict(int)
        for routes in vehicle_routes:
            if routes:
                node_load[routes[0]]+=1
                balanced_routes = sorted(vehicle_routes,key=lambda r:node_load[0])
                return balanced_routes