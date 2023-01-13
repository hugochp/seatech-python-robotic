from exo1_starter_template import Robot


class Human():   
    # Human class content here

    # Un humain doit posséder un sexe attribuable à sa création
    def __init__(self, sexe):
        self.sexe = sexe

    # Un humain doit pouvoir manger un ou plusieurs aliments
    def eat(self, food):
        if isinstance(food, list):
            print("Eating multiple foods:")
            for f in food:
                print(f"Eating {f}")
            else:
                print(f"Eating {food}")

    # Un humain doit pouvoir digérer ce qu'il a mangé
    def digest(self):
        print("Digesting food")
    pass

class Cyborg(Robot, Human):   


    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        
    def fun(self):
        print("I'm a fun cyborg!")

if __name__ == "__main__" :

    cyborg = Cyborg('Deux Ex Machina', 'M')
    cyborg.fun()

    print(cyborg.getName(), 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.setChargingState(True)
    cyborg.getState()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()