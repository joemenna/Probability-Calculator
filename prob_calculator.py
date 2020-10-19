import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        contents = []
        for k,v in balls.items():
            colors = k
            for i in range(v):
                contents.append(colors)

        self.contents = contents
    
    # Draw method to pull a certain amount of balls from the hat
    def draw(self, number):
        draws = number
        if draws >=len(self.contents):
            return self.contents
        else:
            sample = random.sample(self.contents, k = draws)
            for i in sample:
                self.contents.remove(i)
            return sample
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = num_experiments
    m = 0
    exp_balls = []
    for k,v in expected_balls.items():
        color = k
        for i in range(v):
            exp_balls.append(color)
    for tests in range(n):
        exp_hat = copy.deepcopy(hat)  
        draw = exp_hat.draw(num_balls_drawn)
        check = all(True if exp_balls.count(item) <= draw.count(item) else False for item in exp_balls)
        if check == True:
            m += 1
    probability = m/n
    return probability