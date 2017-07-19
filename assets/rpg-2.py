# rpg-2.py


#==================================================================
# Character classes
#==================================================================

#==================================================================
class Character:
    def __init__(self, name, hp, ability):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.ability = ability

    # Special function that Python uses when casting us to a string.
    # There's also "__repr__" for smaller "representations".  This is usually
    # what shows the address in memory, etc.
    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def attack_something(self, target):
        # Let the ability handle doing whatever it wants to do.
        self.ability.perform(self, target)


#==================================================================
# Ability classes
#==================================================================

#==================================================================
class Ability:
    """An ability to use in combat.  Each character gets their own list of
    instances of abilities (no sharing), so abilities can change themselves
    over time per-character."""

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} damage)'.format(self.name, self.damage)

    def perform(self, source, target):
        target.hp = min(max(0, target.hp - self.damage), target.hp_max)
        print '{} used {} on {}'.format(source.name, self, target)


#==================================================================
player = Character('Hiro', 20, Ability('Slash', 5))
slimea = Character('Slime A', 5, Ability('Acid', 2))

print player
print slimea
print ''
player.attack_something(slimea)
slimea.attack_something(player)

