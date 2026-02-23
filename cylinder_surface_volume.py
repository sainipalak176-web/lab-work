import math 
#function to calculate curved surface area
def curved_surface_area(radius,height):
    return 2*math.pi*radius*height
    #function to calculate total surface area
    def total_surface_area(radius,height):
        return 2*math.pi*radius*(radius+height)
        #function to calculate volume
        def volume_cylinder(radius,height):
            return math.pi*radius*radius*height
            #taking input from user
            r=float(input("Enter radius of cylinder:"))
            h=float(input("Enter height of cylinder"))
            #function calls
            cse=curved_surface_area(r,h)
            tsa=total_surface_area(r,h)
            vol=volume_cylinder(r,h)
            #displaying result
            print("curved surface area=",csa)
            print("Total surafce area=",tsa)
            print("volume of cylinder=",vol)