import math

def rectangle_area(b,h):
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

def surface_input():
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
    print("This program is made to find the surface area of a 3 dimensional object. The functions called surface_area and rectangle_area both calculate surface area, and surface_input is the function that gets input.")
    print("To calculate, you must multiply base times height, base times width, and width times height. They all must be parameters")
    print("Then for input, make sure to set base, height, and width as variables.")

def get_height():
    h = float(input("What is the height of the rectangle?"))

def get_base():
    b = float(input("What is the base of the rectangle?"))

def get_width():
    w = float(input("what is the width of the rectangle?"))


def main():
    pass

surface_input()

