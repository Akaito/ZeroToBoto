# rpg-0.py


#==================================================================
# Character classes
#==================================================================

#==================================================================
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.hp_max = hp

    # Special function that Python uses when casting us to a string.
    # There's also "__repr__" for smaller "representations".  This is usually
    # what shows the address in memory, etc.
    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)


#==================================================================
player = Character('Hiro', 20)
slimea = Character('Slime A', 5)
slimeb = Character('Slime B', 5)

print str(player)
print str(slimea)
print str(slimeb)

