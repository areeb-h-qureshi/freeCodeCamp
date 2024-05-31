import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **colors):
    self.colors = colors
    self.balls_total = sum(colors.values())
    self.contents = []
    for key, value in colors.items():
      for i in range(value):
        self.contents.append(key)
    
  def draw(self, num_balls_drawn):
    if num_balls_drawn >= self.balls_total:
      return self.contents
    else:
      self.drawn = []
      for balls in range(num_balls_drawn):
        x = random.choice(self.contents)
        self.contents.remove(x)
        self.drawn.append(x)
      return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match = 0
  for i in range(num_experiments):
    condition_met = True
    
    hat_test = copy.deepcopy(hat)
      
    drawn = hat_test.draw(num_balls_drawn)
    actual_balls = {}
    for color in drawn:
      actual_balls[color] = actual_balls.get(color, 0)+1
      
    for key, value in expected_balls.items():
      if expected_balls[key]>actual_balls.setdefault(key, 0):
        condition_met = False
        
    if condition_met:
      match += 1
      
  prob = match/num_experiments
  return prob