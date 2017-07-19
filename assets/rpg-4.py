# rpg-4.py


#==================================================================
# Character classes
#==================================================================

#==================================================================
class Character(object):
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
class Ability(object):
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
class AbilityStrongerEveryUse(Ability):
    """Special variety of an attack that gets stronger every use."""

    def __init__(self, name, damage, growth):
        super(AbilityStrongerEveryUse, self).__init__(name, damage)
        self.growth = growth

    def perform(self, source, target):
        super(AbilityStrongerEveryUse, self).perform(source, target)
        self.damage += self.growth


#==================================================================
class AbilityHeal(Ability):
    def __init__(self, name, heal_amount):
        super(AbilityHeal, self).__init__(name, -heal_amount)

    def __str__(self):
        return '{} ({} healing)'.format(self.name, -self.damage)


#==================================================================
class AbilityDisintegrate(Ability):
    def __init__(self, damage):
        super(AbilityDisintegrate, self).__init__('Disintegrate', damage)

    def perform(self, source, target):
        super(AbilityDisintegrate, self).perform(source, target)
        super(AbilityDisintegrate, self).perform(source, source)


#==================================================================
player = Character('Hiro', 20, AbilityHeal('Heal', 8))
slimea = Character('Slime A', 5, AbilityStrongerEveryUse('Acid', 2, 1))
slimeb = Character('Slime B', 5, AbilityStrongerEveryUse('Acid', 2, 1))
slimec = Character('Slime C', 5, AbilityDisintegrate(9))

print player
print slimea
print slimeb
print ''

slimea.attack_something(player)
slimea.attack_something(player)
slimeb.attack_something(player)
slimec.attack_something(player)
player.attack_something(player)

