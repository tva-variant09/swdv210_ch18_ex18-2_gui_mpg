#!/usr/bin/env python3
# author: Marco 
# date: 2024-11-07
# description: A module that contains the business logic for the MPG calculator

from dataclasses import dataclass

@dataclass
class MpgCalculator():
    miles_driven: float = 0.0
    gallons_used: float = 0.0

    def calculate_mpg(self):
        return round(self.miles_driven / self.gallons_used, 2)