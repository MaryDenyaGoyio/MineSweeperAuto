from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random


'''
    unknown = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == -1]
    
    while unknown:
        # Get all known squares
        known = [(i, j) for i in range(n) for j in range(m) if grid[i][j] != -1]

        probabilities = {}
        for i, j in unknown:
            # For each unknown square, calculate the probability of it being a mine
            neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) 
                         if 0 <= x < n and 0 <= y < m and (x, y) != (i, j)]
            mines_neighbors = [grid[x][y] for x, y in neighbors if (x, y) in known]
            # Calculate the probability
            prob = sum(mines_neighbors) / len(mines_neighbors) if mines_neighbors else 0
            probabilities[(i, j)] = prob

        # Choose the square with the minimum probability of being a mine
        min_prob_square = min(probabilities, key=probabilities.get)
        if probabilities[min_prob_square] >= 0.5:
            # If all probabilities are 0.5 or more, choose a square randomly
            min_prob_square = random.choice(unknown)
        
        # Open the square
        unknown.remove(min_prob_square)
        i, j = min_prob_square
        grid[i][j] = int((i, j) in mines)
'''


class Miner():
    def __init__(self, uuid=2437260880):
        self.driver = webdriver.Chrome()
        self.driver.get(f'https://minesweeper.online/ko/game/{uuid}')

        self.reset = WebDriverWait(self.driver, 60).until( EC.presence_of_element_located((By.ID, "top_area_face")) )
        self.reset.click()

        self.board = [ [ None for x in range(30) ] for y in range(16) ]
        self.sides = [ (x, y) for x in [1, 0, -1] for y in [1, 0, -1] if not (x==0 and y==0) ]

    def click(self, x, y):
        element = self.driver.find_element(By.ID, f"cell_{x}_{y}")
        element.click()

    def get(self, x, y):
        element = self.driver.find_element(By.ID, f"cell_{x}_{y}")

        temp = element.get_attribute('class').split(' ')

        status = True if temp[2] == 'hd_closed' else False
        number = int(temp[3][7:]) if status else None

        return status, number
    
    def check(self, x, y):
        return (0<=x and x<30) and (0<=y and y<16)
    
    def search(self):

        if status:
            for x, y in self.sides:
                if not self.check(x, y):
                    break

                if self.board[x][y] == None:
                    # Edges


        pass
    
    # cell size24 hd_opened hd_type0
    # cell size24 
#'''
