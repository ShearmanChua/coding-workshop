from sys import stdin, stdout
import math

angles_to_check = stdin.readlines()

for angles in angles_to_check:
    angles = angles.split(" ")

    A = int(angles[0])%360 if int(angles[0])>=0 else (360+int(angles[0])%-360)%360
    B = int(angles[1])%360 if int(angles[1])>=0 else (360+int(angles[1])%-360)%360
    C = int(angles[2])%360 if int(angles[2])>=0 else (360+int(angles[2])%-360)%360

    if A in range(B, C+1) or B==C or (B>C and A>=B) or (B>C and A<=C):
        print("TRUE")
    else:
        print("FALSE")
