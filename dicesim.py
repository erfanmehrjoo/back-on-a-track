import random

def roll_dice():
    
    dice_drawing = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    roll = input("Roll thw dice? (Yes/No): ")
    
    while roll.lower() == 'Yes'.lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("You rolled a", dice1, "and a", dice2)
        print("\n".join(dice_drawing[dice1] + dice_drawing[dice2]))
        
        roll = input("Roll thw dice? (Yes/No): ")
        
roll_dice()