
'''
code taken from:
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
algorithm attempt:

check if any lines of the polygon intersect the vehicle 
if yes, return Land/Sea immediately, since (if any part of vehicle touches a land border)

else, it would mean the vehicle is either fully on land or fully in the sea

check one (theoretically one should be sufficient) of the points of the vehicle is inside 
or outside the polygon

if inside => Land
if outside => Sea


'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"\n x: {self.x} | y: {self.y} \n"


class Vehicle:
    
    def __init__(self,x_front,y_front,x_back,y_back):
        self.front = Point(x_front, y_front)
        self.back = Point(x_back, y_back)
        
    def __repr__(self):
        return f"\n front: {self.front} \n back: {self.back})\n"

def on_line(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False

def check_orientation(p, q, r):
    # to find the orientation of 3 pts (p, q, r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0

    
# The main function that returns true if 
# the line segment 'p1q1' and 'p2q2' intersect.
def check_intersect(p1,q1,p2,q2):
    # Find the 4 orientations required for 
    # the general and special cases
    o1 = check_orientation(p1, q1, p2)
    o2 = check_orientation(p1, q1, q2)
    o3 = check_orientation(p2, q2, p1)
    o4 = check_orientation(p2, q2, q1)
  
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
    # Special Cases
    # p1 , q1 and p2 are collinear and p2 lies on Line p1q1
    if ((o1 == 0) and on_line(p1, p2, q1)):
        return True
    # p1 , q1 and q2 are collinear and q2 lies on Line p1q1
    if ((o2 == 0) and on_line(p1, q2, q1)):
        return True
    # p2 , q2 and p1 are collinear and p1 lies on Line p2q2
    if ((o3 == 0) and on_line(p2, p1, q2)):
        return True
    # p2 , q2 and q1 are collinear and q1 lies on Line p2q2
    if ((o4 == 0) and on_line(p2, q1, q2)):
        return True 
    # If none of the cases
    return False
    
def check_point_inside(vehicle, polygon):
   
    #check if the front point of the vehicle is inside
    
    #set inifinity point x to be outside constraint of 1000 and y to be same as vehicle front
    infinity_point=Point(1001,vehicle.front.y)
    
    count=0
    
    for i in range(1,len(polygon)):
        if check_intersect(vehicle.front,infinity_point,polygon[i-1],polygon[i]):
            count +=1
        
    # Check last line between last point and first
    
    if check_intersect(vehicle.front,infinity_point,polygon[-1],polygon[0]):
            count +=1
            
    # Dont need to account for point touching the line as it would have been an
    # auto Land/Sea and covered in check_border 
    
    #if even inside
    if(count%2==1):
        return True
    else:
        return False
        

def check_border(vehicle, polygon):
    
    intersect = False
    
    for i in range(1,len(polygon)):
        if check_intersect(vehicle.front,vehicle.back,polygon[i-1],polygon[i]):
            intersect =True
        
    # Check last line between last point and first
    
    if check_intersect(vehicle.front,vehicle.back,polygon[-1],polygon[0]):
            intersect =True
            
    return intersect


def main_check(vehicles,polygons):
    
    for vehicle in vehicles:
        
        result=None
        
        for polygon in polygons:
            
            if(check_border(vehicle,polygon)):
                result = "Land/Sea"
                break
            # if not touching border means must be either land or sea
            elif(check_point_inside(vehicle, polygon)):
                result = "Land"
                break
        if(not result):
            result="Sea"
        print(result)
            
        
def get_polygons():
    m = int(input())
    polygons=[]
    for _ in range(m):
        no_of_points = int(input())
        points=[]
        for _ in range(no_of_points):
            x,y = map(int,input().strip().split(" "))
            points.append(Point(x,y))
        polygons.append(points)
    return polygons
        
def get_vehicles():
    n = int(input())
    vehicles = []
    for _ in range(n):
        x_front,y_front,x_back,y_back = map(int,input().strip().split(" "))
        vehicles.append(Vehicle(x_front,y_front,x_back,y_back))
    return vehicles

def main():
    
    vehicles = get_vehicles()
    
    # print(f"vehicles: {vehicles}")
    
    polygons = get_polygons()
    
    # print(f"polygons: {polygons}")
    
    main_check(vehicles,polygons)
        

if __name__ == "__main__":
    main()