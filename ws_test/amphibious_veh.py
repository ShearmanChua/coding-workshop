from sys import stdin, stdout
import cmath

class Point:
    def __init__(self, x, y):
        self.coordinates = (x,y)
        
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Polygon:
    def __init__(self, points):
        self.no_of_points = len(points)
        self.points = points

def if_point_in_segment_pop(P, P0,P1): #from https://www.linkedin.com/pulse/short-formula-check-given-point-lies-inside-outside-polygon-ziemecki/
    p0 = P0[0]- P[0], P0[1]- P[1]
    p1 = P1[0]- P[0], P1[1]- P[1]


    det = (p0[0]*p1[1] - p1[0]*p0[1])
    prod = (p0[0]*p1[0] + p0[1]*p1[1])
    
    return (det == 0 and prod < 0) or (p0[0] == 0 and p0[1] == 0) or (p1[0] == 0 and p1[1] == 0)


def isInsidePolygon(P: tuple, Vertices: list, validBorder=False): #from https://www.linkedin.com/pulse/short-formula-check-given-point-lies-inside-outside-polygon-ziemecki/

    sum_ = complex(0,0)

    for i in range(1, len(Vertices) + 1):
        v0, v1 = Vertices[i-1] , Vertices[i%len(Vertices)]

        if if_point_in_segment_pop(P,v0,v1):
            return validBorder, "validBorder"
        
        sum_ += cmath.log( (complex(*v1) - complex(*P)) / (complex(*v0) - complex(*P)) )


    return abs(sum_) > 1, "notValidBorder"

def direction(p1, p2, p3):
    return (p3[1]-p1[1]) * (p2[0]-p1[0]) > (p2[1]-p1[1]) * (p3[0]-p1[0])

def on_line(p, q, r):
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and 
           (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False

def is_intersect(p1,p2,p3,p4):
    direction_0 = direction(p1,p3,p4)
    direction_1 = direction(p2,p3,p4)
    direction_2 = direction(p1,p2,p3)
    direction_3 = direction(p1,p2,p4)
    
    return direction_0 != direction_1 and direction_2 != direction_3

def check_intersect(line,points):
    p1, p2 = line.p1.coordinates, line.p2.coordinates
    for i in range(1, len(points) + 1):
        side_0, side_1 = points[i-1] , points[i%len(points)]
        if is_intersect(p1,p2,side_0,side_1):
            return True
    return False

lines = stdin.readlines()

vehicles = lines[1:int(lines[0])+1]

polygons = []

polygon_count = int(lines[int(lines[0])+1])
line_count = int(lines[0])+2

while polygon_count > 0:
    point_lines = lines[line_count+1:int(lines[line_count])+line_count+1]
    points = [[int(point.split()[0]),int(point.split()[1])] for point in point_lines]
    polygons.append(Polygon(points))
    line_count += int(lines[line_count]) + 1
    polygon_count -= 1

for vehicle in vehicles:
    x1, y1, x2, y2 = vehicle.strip().split(" ")
    vehicle_line = Line(Point(int(x1),int(y1)), Point(int(x2),int(y2)))
    output = "Sea"

    for polygon in polygons:
        if check_intersect(vehicle_line,polygon.points):
            output = "Land/Sea"
            break
        else:
            front, front_condition = isInsidePolygon(vehicle_line.p1.coordinates, polygon.points) 
            back, back_condition = isInsidePolygon(vehicle_line.p2.coordinates, polygon.points)
            
            if front and back:
                output = "Land"
                break
            elif front_condition=="validBorder" or back_condition=="validBorder":
                output = "Land/Sea"
                break
            
    print(output)