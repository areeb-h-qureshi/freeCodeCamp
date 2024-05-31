class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width**2 + self.height**2)**.5)
    return diagonal
    
  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    res = ""
    for i in range(self.height):
      res += "*"*self.width + "\n"
    return res

  def get_amount_inside(self, rec):
    outer_area = self.get_area()
    inner_area = rec.get_area()
    repeat = outer_area//inner_area
    return repeat

  def __str__(self):
    res = f"Rectangle(width={self.width}, height={self.height})"
    return res
    
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
    
  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side
    
  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
      res = f"Square(side={self.width})"
      return res