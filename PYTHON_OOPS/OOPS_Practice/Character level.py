'''THIS CODE HAS A PROBLEM. IT'S CHAOS'''
'''IT IS NOT SAVING THE VALUES'''
# Write a Python program that creates a Character class with exp, and level attributes. 
# The character should automatically level up and reset exp whenever accumulated experience reaches or exceeds 100.

class Character:
    def __init__(self,name,result,exp):
        self.name=name
        self.result=result      # victory or defeat
        self.level=0
        self.exp=exp

    def upgrade(self):
        # if result==victory => exp +30
        # if result==defeat => exp -20
        # level up when exp==100
        # exp can not be negative

        if self.result=="victory":
            #self.exp+=30
            target_exp=100-self.exp

            if self.exp>100:
                self.level+=1
                print(f"All hail the Champion!")
                print(f"Victory to {self.name}")
                print(f"{self.name} leveled up to level-{self.level}. Glory!")
                self.exp=0

            elif self.exp>0 and target_exp>0:
                print(f"All hail the Champion!")
                print(f"Victory to {self.name}")
                print(f"You need {target_exp} exp to level up. Keep Winning!")

            elif self.exp<0:
                print(f"{self.name} avenges himself!")
                print(f"All hail the Champion!")
                print(f"Keep winning to level up!")

        elif self.result=="defeat":
            #self.exp-=20
            target_exp=100-self.exp

            if self.exp>0:
                print(f"Even the sun must set to rise again!")
                print(f"Awaken, {self.name}-your legend is unfinished!")
                print(f"You need {target_exp} exp to level up. Keep Winning!")

            elif self.exp<=0:
                print(f"The light has walked into the dark. Rise {self.name}")
                print(f"Win to avenge your lose {self.name}")

# Omnigod:-
char1=Character("Omnigod","victory",50)   
char1.upgrade()
print(" ")

char2=Character("Raiden-Kai","victory",30) 
char2.upgrade()
print(" ")

char1=Character("Omnigod","defeat",110)     
char1.upgrade()
print(" ")

char2=Character("Raiden-Kai","victory",110) 
char2.upgrade()
print(" ")

char1=Character("Omnigod","defeat",-90) 
char1.upgrade()
print(" ")