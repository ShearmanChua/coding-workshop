from sys import stdin, stdout

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Polygon:
    def __init__(self, points):
        self.no_of_points = len(points)
        self.points = points

def on_line(line, point):
    if (point.x <= max(line.p1.x, line.p2.x) and point.x <= min(line.p1.x, line.p2.x) and (point.y <= max(line.p1.y, line.p2.y) and point.y <= min(line.p1.y, line.p2.y))):
        return True
    return False

def direction(a, b, c):
    value = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if value == 0:
        # Colinear
        return 0
    elif (value < 0):
        # Anti-clockwise direction
        return 2
    # Clockwise direction
    return 1

def is_intersect(line_1,line_2):
    dir1 = direction(line_1.p1, line_1.p2, line_2.p1)
    dir2 = direction(line_1.p1, line_1.p2, line_2.p2)
    dir3 = direction(line_2.p1, line_2.p2, line_1.p1)
    dir4 = direction(line_2.p1, line_2.p2, line_1.p2)

    # When intersecting
    if (dir1 != dir2 and dir3 != dir4):
        return True
 
    # When p2 of line2 are on the line1
    if (dir1 == 0 and on_line(line_1, line_2.p1)):
        return True
 
    # When p1 of line2 are on the line1
    if (dir2 == 0 and on_line(line_1, line_2.p2)):
        return True
 
    # When p2 of line1 are on the line2
    if (dir3 == 0 and on_line(line_2, line_1.p1)):
        return True
 
    # When p1 of line1 are on the line2
    if (dir4 == 0 and on_line(line_2, line_1.p2)):
        return True
 
    return False

def on_line_new(p, q, r):
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
    if ((o1 == 0) and on_line_new(p1, p2, q1)):
        return True
    # p1 , q1 and q2 are collinear and q2 lies on Line p1q1
    if ((o2 == 0) and on_line_new(p1, q2, q1)):
        return True
    # p2 , q2 and p1 are collinear and p1 lies on Line p2q2
    if ((o3 == 0) and on_line_new(p2, p1, q2)):
        return True
    # p2 , q2 and q1 are collinear and q1 lies on Line p2q2
    if ((o4 == 0) and on_line_new(p2, q1, q2)):
        return True 
    # If none of the cases
    return False

def check_inside(polygon, point_to_check, line_to_check):
    ex_line = Line(point_to_check,Point(1001,point_to_check.y))

    polygon_points = polygon.points
    intersect_count = 0

    for idx, point in enumerate(polygon_points):
        side = Line(point, polygon_points[(idx + 1)%polygon.no_of_points]) 
        if check_intersect(side.p1,side.p2, line_to_check.p1,line_to_check.p2):
            return True, "landsea"
        elif check_intersect(side.p1,side.p2, ex_line.p1, ex_line.p2):
            # print(side.p1.x,side.p1.y,side.p2.x,side.p2.y)
            # print("intersect")
            if direction(side.p1, point_to_check,side.p2) == 0:
                return on_line(side,point_to_check), "on line"
            intersect_count += 1
            return (intersect_count%2 != 0), "inside"

    return (intersect_count%2 != 0), "inside"

lines = stdin.readlines()

vehicles = lines[1:int(lines[0])+1]

polygons = []

polygon_count = int(lines[int(lines[0])+1])
line_count = int(lines[0])+2

while polygon_count > 0:
    point_lines = lines[line_count+1:int(lines[line_count])+line_count+1]
    points = [Point(int(point.split()[0]),int(point.split()[1])) for point in point_lines]
    polygons.append(Polygon(points))
    line_count += int(lines[line_count]) + 1
    polygon_count -= 1

for vehicle in vehicles:
    x1, y1, x2, y2 = vehicle.strip().split(" ")
    vehicle_line = Line(Point(int(x1),int(y1)), Point(int(x2),int(y2)))
    output = "Sea"

    for polygon in polygons:
        front_in, front_on_line = check_inside(polygon, Point(int(x1),int(y1)), vehicle_line)
        
        if front_on_line == "landsea":
            # print("Hello")
            output = "Land/Sea"
            break
            
        # print("checking back")
        back_in, back_on_line = check_inside(polygon, Point(int(x2),int(y2)), vehicle_line)
        # print(front_in,back_in)
        
        if front_in and back_in:
            output = "Land"
            break
        elif (front_on_line == "on line" and back_on_line == "on line") or front_in or back_in:
            output = "Land/Sea"
            break
    
    print(output)



test case
3
1 1 2 2
20 20 21 21
5 5 -10 5
1
4
0 0
0 10
10 10
10 0

expected output
Land
Sea
Land/Sea

test case
2
22 50 1 64
16 100 76 77
1
6
-100 -100
0 100
50 200
100 100
100 0
50 50

expected output
Land
Land

test case
1
16 100 76 77
1
6
-100 -100
0 100
50 101
100 100
100 0
50 50

expected output
Land

test case
3
22 50 1 64
90 100 76 77
0 50 0 51
1
7
-100 -100
0 100
50 110
100 100
100 0
50 50
30 60