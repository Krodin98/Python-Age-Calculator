import tkinter as tk
from tkinter import ttk
from datetime import date
import calendar
import random

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x250")
        self.root.configure(background="#f0f0f0")
        
        # Create frames
        self.input_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
        self.input_frame.pack(fill=tk.BOTH, expand=False)
        
        self.result_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.button_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
        self.button_frame.pack(fill=tk.BOTH, expand=False)
        
        # Surprise frame
        self.surprise_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
        self.surprise_frame.pack(fill=tk.BOTH, expand=False)
        
        # Create date selection components
        tk.Label(self.input_frame, text="Year:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        current_year = date.today().year
        years = [str(current_year - i) for i in range(100)]
        self.year_combobox = ttk.Combobox(self.input_frame, values=years, width=10)
        self.year_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.year_combobox.current(0)
        
        tk.Label(self.input_frame, text="Month:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        months = list(calendar.month_name)[1:]  # Skip the empty first item
        self.month_combobox = ttk.Combobox(self.input_frame, values=months, width=10)
        self.month_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.month_combobox.current(0)
        
        tk.Label(self.input_frame, text="Day:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        days = [str(i) for i in range(1, 32)]
        self.day_combobox = ttk.Combobox(self.input_frame, values=days, width=10)
        self.day_combobox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.day_combobox.current(0)
        
        # Create result label
        self.result_label = tk.Label(self.result_frame, 
                                  text="Enter your birthdate and click Calculate",
                                  bg="#f0f0f0",
                                  font=("Arial", 10))
        self.result_label.pack(pady=10)
        
        # Create surprise message label
        self.surprise_label = tk.Label(self.surprise_frame, 
                                    text="",
                                    bg="#f0f0f0",
                                    font=("Arial", 10, "italic"))
        self.surprise_label.pack(pady=5)
        
        # Create calculate button
        calculate_button = ttk.Button(self.button_frame, text="Calculate Age", command=self.calculate_age)
        calculate_button.pack(side=tk.LEFT, padx=5)
        
        # Create surprise button
        self.surprise_button = ttk.Button(self.button_frame, text="Surprise!", command=self.show_surprise)
        self.surprise_button.pack(side=tk.LEFT, padx=5)
        self.surprise_button.state(['disabled'])  # Disabled until age is calculated
        
        # Age data for surprise feature
        self.current_age_years = 0
        
        # Surprise messages by age group
        self.surprise_messages = {
            'child': [
                "Did you know? At your age, your brain is growing faster than it ever will!",
                "Fun fact: Your bones are still growing and changing shape!",
                "Wow! You have more taste buds now than adults do!"
            ],
            'teen': [
                "Did you know? Your brain is rewiring itself during these years!",
                "Cool fact: Your generation is the most tech-savvy in history!",
                "Amazing! Your ability to learn new skills is at its peak now!"
            ],
            'adult': [
                "Interesting fact: You've likely made about 90% of the friends you'll have in life!",
                "Did you know? Your brain reaches its maximum weight in your 20s!",
                "Fun fact: Your wisdom teeth may still be deciding whether to show up!"
            ],
            'midlife': [
                "Did you know? Your vocabulary is probably at its peak now!",
                "Interesting fact: Your emotional intelligence is likely at its strongest!",
                "Amazing! Your ability to problem-solve complex issues peaks now!"
            ],
            'senior': [
                "Did you know? You're likely happier now than you were in your 40s!",
                "Wonderful fact: Your crystallized intelligence (wisdom) continues to grow!",
                "Amazing! Your brain has created around 4 terabytes of memories!"
            ]
        }
        
        # Colors for different age groups
        self.age_colors = {
            'child': "#FFD700",  # Gold
            'teen': "#87CEEB",   # Sky Blue
            'adult': "#98FB98",  # Pale Green
            'midlife': "#FFA07A", # Light Salmon
            'senior': "#DDA0DD"  # Plum
        }
    
    def calculate_age(self):
        try:
            year = int(self.year_combobox.get())
            month_idx = self.month_combobox.current() + 1  # Convert to 1-based index
            day = int(self.day_combobox.get())
            
            birth_date = date(year, month_idx, day)
            today = date.today()
            
            # Calculate age
            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day
            
            # Adjust for negative months or days
            if days < 0:
                # Borrow from months
                months -= 1
                # Get days in the previous month
                if today.month == 1:
                    previous_month = 12
                    previous_month_year = today.year - 1
                else:
                    previous_month = today.month - 1
                    previous_month_year = today.year
                
                days_in_previous_month = calendar.monthrange(previous_month_year, previous_month)[1]
                days += days_in_previous_month
            
            if months < 0:
                # Borrow from years
                years -= 1
                months += 12
            
            self.current_age_years = years
            self.result_label.config(text=f"You are {years} years, {months} months, and {days} days old.")
            
            # Enable surprise button after calculation
            self.surprise_button.state(['!disabled'])
            
            # Clear any previous surprise message
            self.surprise_label.config(text="")
            
            # Reset background color
            self.root.configure(background="#f0f0f0")
            self.input_frame.configure(background="#f0f0f0")
            self.result_frame.configure(background="#f0f0f0")
            self.button_frame.configure(background="#f0f0f0")
            self.surprise_frame.configure(background="#f0f0f0")
            self.result_label.configure(background="#f0f0f0")
            self.surprise_label.configure(background="#f0f0f0")
            
            # Reset labels in input frame
            for widget in self.input_frame.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.configure(background="#f0f0f0")
                
        except ValueError:
            self.result_label.config(text="Please enter a valid date")
            self.surprise_button.state(['disabled'])
    
    def get_age_group(self):
        if self.current_age_years < 13:
            return 'child'
        elif self.current_age_years < 20:
            return 'teen'
        elif self.current_age_years < 40:
            return 'adult'
        elif self.current_age_years < 65:
            return 'midlife'
        else:
            return 'senior'
    
    def show_surprise(self):
        # Get age group and corresponding messages and color
        age_group = self.get_age_group()
        messages = self.surprise_messages[age_group]
        color = self.age_colors[age_group]
        
        # Choose a random message
        message = random.choice(messages)
        
        # Update surprise label
        self.surprise_label.config(text=message)
        
        # Change colors
        self.root.configure(background=color)
        self.input_frame.configure(background=color)
        self.result_frame.configure(background=color)
        self.button_frame.configure(background=color)
        self.surprise_frame.configure(background=color)
        self.result_label.configure(background=color)
        self.surprise_label.configure(background=color)
        
        # Update labels in input frame
        for widget in self.input_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(background=color)
        
        # Add some extra fun for children
        if age_group == 'child':
            self.root.title("🎉 Age Calculator 🎉")
        # Add wisdom for seniors
        elif age_group == 'senior':
            self.root.title("🌟 Wisdom Calculator 🌟")
        else:
            self.root.title("Age Calculator")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop() 