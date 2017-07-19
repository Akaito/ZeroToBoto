# rpg-complete.py

import random


#==================================================================
# Character classes
#==================================================================

#==================================================================
class Character:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.attacks = {}
        for attack in attacks:
            self.attacks[attack.name.lower()] = attack

    # Special function that Python uses when casting us to a string.
    # There's also "__repr__" for smaller "representations".  This is usually
    # what shows the address in memory, etc.
    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def attack_something(self, target, attack=None):
        # Don't let dead things attack.
        if self.hp <= 0:
            return
        # If we're called with no attack set, just pick one we can do at
        # random.
        if attack is None:
            attack = random.choice(self.attacks.values())
        # If we're called with the name of an attack (instead of an
        # Attack-inheriting object), find that attack in our list.
        elif type(attack) == str:
            attack = self.attacks[attack]
        # Let the attack handle doing whatever it wants to do.
        attack.perform(self, target)


#==================================================================
# Just an easy way to make basic slimes that all have the Acid attack.
class CharSlime(Character):
    def __init__(self, name, hp, can_disintegrate):
        attacks = [AttackStrongerEveryUse('Acid', 1)]
        # Optionally, allow extra dangerous slimes to disintigrate.
        if can_disintegrate:
            attacks.append(AttackDisintegrate())
        # Call the Character class' initialization function on ourselves, so we
        # get all the base Character goodness handled, passing it the temporary
        # list "attacks" we prepared within this function.
        Character.__init__(self, name, hp, attacks)


#==================================================================
# Attack classes
#==================================================================

#==================================================================
class Attack:
    """An ability to use in combat.  Each character gets their own list of
    instances of abilities (no sharing), so attacks can change themselves over
    time per-character."""

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} damage)'.format(self.name, self.damage)

    def perform(self, source, target):
        target.hp = min(max(0, target.hp - self.damage), target.hp_max)
        print '{} used {} on {}'.format(source.name, self, target)


#==================================================================
class AttackStrongerEveryUse(Attack):
    """Special variety of an attack that gets stronger every use."""

    def __init__(self, name, growth):
        Attack.__init__(self, name, 2)
        self.growth = growth

    def perform(self, source, target):
        Attack.perform(self, source, target)
        self.damage += self.growth


#==================================================================
class AttackHeal(Attack):
    def __init__(self, name, heal_amount):
        Attack.__init__(self, name, -heal_amount)

    def __str__(self):
        return '{} ({} healing)'.format(self.name, -self.damage)


#==================================================================
class AttackDisintegrate(Attack):
    def __init__(self):
        Attack.__init__(self, 'Disintegrate', 9)

    def perform(self, source, target):
        Attack.perform(self, source, target)
        Attack.perform(self, source, source)


#==================================================================
player_name = 'Hiro'
player_key = player_name.lower()

# Holds combatants with an arbitrary keyname to make them easy to type in while
# playing.
combatants = {}
# Add a player to the encounter.
combatants[player_key] = Character(player_name, 20, [
    Attack('Slash', 4), AttackHeal('Heal', 8)
])
# Add two slimes.
combatants['slimea'] = CharSlime('Slime A', 5, False)
combatants['slimeb'] = CharSlime('Slime B', 5, True)

# Keep doing combat while player is alive, and they're not alone.
while player_key in combatants.keys() and len(combatants) > 1:
    # Write status of combat.
    print 'Your attacks:'
    for atk in sorted(combatants[player_key].attacks.values()):
            print '  {}'.format(atk)
    print 'Remaining combatants:'
    for char in sorted(combatants.values()):
        print '  ' + str(char)

    # Get player's choice of target and attack (ability) to use.
    atk_name = ''
    monster_name = ''
    # Keep trying until they give us something valid.
    while atk_name not in combatants[player_key].attacks.keys() or monster_name not in combatants.keys():
        # str.split(' ') is splitting the user's input on spaces.  We expect
        # the player to give us "some_word<space>another_word".
        user_input = raw_input('<attack> <combatant>: ').split(' ')
        if len(user_input) != 2:
            continue
        atk_name = user_input[0]
        monster_name = user_input[1]

    # Player finally performs their attack.
    combatants[player_key].attack_something(combatants[monster_name], atk_name)

    # Make each monster use some random attack against the player.
    for key, char in combatants.iteritems():
        if key == player_key:
            continue
        char.attack_something(combatants[player_key])

    # Clean up dead combatants.
    # Python may have a more Pythonic way to do this.  This ugly-looking chunk
    # of lines is my way of handling this in a semi-C++-like way, and may not
    # be a great example as an approach.  But it does work, is reasonably
    # readable, and will translate well to other languages.
    # We can't modify a container while we're enumerating over it, so we're
    # going to collect something to identify the things to remove, then get
    # done enumerating the container, then remove the stuff we don't want from
    # it.
    dead_monsters = []
    for key, monster in combatants.iteritems():
        if monster.hp <= 0:
            dead_monsters.append(key)  # get keys of things to remove from dict later
            print '{} has died!'.format(monster.name)
    for key in dead_monsters:
        # del on a dict like this kills the object stored there, *and* removes
        # the key from the dictionary where it was located.
        del combatants[key]
    print ''

if player_key not in combatants.keys():  # did the player die?
    print 'Failure.'
else:
    print 'Cleared!'

