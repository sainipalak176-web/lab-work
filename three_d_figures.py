import math
#cube
def cube_volume(side):
    return side**3
    def cube_surface_area(side):
        return 6 *side*side

        #cuboid
        def_cuboid volume(length,breadth,height):
            return length*breadth*height
            def cuboid_surface_area(length,breadth,height):
                reutrn 2 * (length*breadth+breadth*height+height*length)

                #cylinder
                def cylinder_volume(radius,height):
                    return math.pi * radius* radius* height
                    def cylinder_surface_area(radius,height):
                        return 2 * math.pi*radius*(radius + height)
                        
                        #cone
                        def cone_volume(radius,height):
                            return(1/3)*math.pi*radius*radius*height
                            def cone_surface_area(radius,height):
                            I=math.sqrt(radius**2+height**2) # slant height
                            return math.pi*radius*(radius+I)

                            #sphere
                            def sphere_volume(radius):
                                return(4/3)*math.pi*radius**3
                                def sphere_surface_area(radius):
                                    return 4 * math.pi*radius**2

                                    #hemisphere
                                    def hemisphere_volume(radius):
                                        return(2/3)*math.pi*radius**3
                                        def hemisphere_surface_area(radius):
                                            return 3*math.pi*radius**2
                        