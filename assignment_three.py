#Anthony Fagiolo
#last modified September 30th
#Made to calculate the area of a rectangle based on user input


import math

def rectangle_area(b,h):
    """
    Determines the area of one side of a rectangle
    :param b: base
    :param h: height
    :return: area
    """
    area=b*h
    return area

def surface_area(b,h,w):
    """
    ses the base, width, and height of rectangle to calculate the surface area.
    calls back the rectangle_area function
    :param b: the base of the rectangle
    :param h: the height of the rectangle
    :param w: the width of the rectangle
    :return: the surface area of the rectangle
    """
    top=rectangle_area(w,h)*2
    left=rectangle_area(b,w)*2
    frnt=rectangle_area(b,h)*2
    area=top+left+frnt
    return area

def surface_input(b,h,w):
   """
   User inputs the base, height, and width to find the surface arae.
   calls back surface_area and rectangle_area function
   :return: surface area of 3D Rectangle
   """
   b = float(input("What is the base of the rectangle?"))
   h = float(input("What is the height of the rectangle?"))
   w = float(input("What is the width of the rectangle?"))
   print(surface_area(b,h,w))

def instruction_manual():
    """
    Tells user the process of the program
    :return: n/a
    """
    print("This program is made to find the surface area of a 3 dimensional object. The functions called surface_area and rectangle_area both calculate surface area, and surface_input is the function that gets input.")
    print("To calculate, you must multiply base times height, base times width, and width times height. They all must be parameters")
    print("Then for input, make sure to set base, height, and width as variables.")

def get_height():
    """Asks the user for the height of the rectangle"""
    h = float(input("What is the height of the rectangle?"))
    return h

def get_base():
    """Asks the user for the base of the rectangle"""
    b= float(input("What is the base of the rectangle?"))
    return b

def get_width():
    """Asks the user for the width of the rectangle"""
    w = float(input("what is the width of the rectangle?"))
    return w


def main():
    """Prints the instruction manual and the surface_area function, which is a composite of the other functions"""
    instruction_manual()
    b = get_base()
    h = get_height()
    w = get_width()
    print(surface_area(b,h,w))

main()

