#!/usr/bin/env python3
# author: Marco 
# date: 2024-11-07
# description: A GUI application that calculates miles per gallon

import tkinter as tk
from tkinter import ttk, messagebox
from business import MpgCalculator

# Create a class for the GUI
class MpgFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="20 20 20 20")
        self.pack()
        self.parent = parent
        self.calculator = MpgCalculator()

        # Define string variables for text entry fields
        
        self.milesDriven = tk.StringVar()
        self.gallonsUsed = tk.StringVar()
        self.mpg = tk.StringVar()
        
        self.ui_components()

    # Create the UI components
    def ui_components(self):
        self.pack()
        
        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesDriven).grid(column=1, row=0)
        ttk.Label(self, text="Gallons of Gas Used:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallonsUsed).grid(column=1, row=1)
        ttk.Label(self, text="Miles Per Gallon:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.mpg, state="readonly").grid(column=1, row=2)
        
        self.makeButtons()

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
    
    # Create the buttons        
    def makeButtons(self):
        # Create a frame to hold the buttons
        buttonFrame = ttk.Frame(self)
        
        # Add the frame to the window
        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)
        
        # Create the buttons
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Clear", command=self.clear_inputs).grid(column=1, row=0)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy).grid(column=2, row=0)
     
     # Get the float value from the text field and validate it       
    
    # Get the float value from the text field and validate it
    def get_float(self, val, field_name):
        try:
            value = float(val)
            if value < 0:
                self.message += f"{field_name} must be a positive number.\n"
                return None
            return value
        except ValueError:
            self.message += f"{field_name}  must be a number.\n"
     
     # Calculate the miles per gallon   
    
    # Calculate the miles per gallon
    def calculate(self):
        self.message = "" # Clear any previous messages
        
        # Get the values from the text fields
        self.calculator.miles_driven = self.get_float(self.milesDriven.get(), "Miles Driven")
        self.calculator.gallons_used = self.get_float(self.gallonsUsed.get(), "Gallons Used")
        
        # Calculate the miles per gallon
        if self.message == "": # If no errors
            self.mpg.set(self.calculator.calculate_mpg())
        else:
            messagebox.showerror("Input Error", self.message)
    
    # Clear the input fields        
    def clear_inputs(self):
            self.milesDriven.set("")
            self.gallonsUsed.set("")
            self.mpg.set("")     

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MpgFrame(root)
    root.mainloop()
