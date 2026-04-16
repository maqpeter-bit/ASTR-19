# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:30:44 2026

@author: mrdan
"""

class favoriteAnimal:
    def __init__(self, len_arm = 0.0, len_leg = 0.0, num_eyes = 0, has_tail = False, is_furry = False):
        self.len_arm = len_arm
        self.len_leg = len_leg
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
    
    def print(self):
        print(f"YOUR FAVORITE ANIMAL HAS: \nAn arm length of {self.len_arm} \nA leg length of {self.len_leg} \n{self.num_eyes} eyes")
        if (self.has_tail):
            print("This animal DOES have a tail (true)")
        else:
            print("This animal DOES NOT have a tail (false)")
        if (self.is_furry):
            print("This animal IS furry (true)")
        else:
            print("This animal IS NOT furry (false)")
        
fox = favoriteAnimal(len_arm = 6.0, len_leg = 6.0, num_eyes = 2, has_tail = True, is_furry = True)

fox.print()
        
        
        



    