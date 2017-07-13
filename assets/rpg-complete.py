# rpg-complete.py

import random


class Character:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.attacks = {}
        for attack in attacks:
            self.attacks[attack.name.lower()] = attack

    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def attack_something(self, target, attack=None):
        if self.hp <= 0:
            return
        if attack is None:
            attack = random.choice(self.attacks.values())
        elif type(attack) == str:
            attack = self.attacks[attack]
        attack.perform(self, target)


class CharSlime(Character):
    def __init__(self, name, hp, can_disintegrate):
        attacks = [AttackAcid()]
        if can_disintegrate:
            attacks.append(AttackDisintegrate())
        Character.__init__(self, name, hp, attacks)


class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} dmg)'.format(self.name, self.damage)

    def perform(self, source, target):
        target.hp = min(max(0, target.hp - self.damage), target.hp_max)
        print '{} used {} on {}'.format(source.name, self, target)


class AttackAcid(Attack):
    def __init__(self):
        Attack.__init__(self, 'Acid', 2)

    def perform(self, source, target):
        Attack.perform(self, source, target)
        self.damage += 1


class AttackHeal(Attack):
    def __init__(self):
        Attack.__init__(self, 'Heal', -8)

    def __str__(self):
        return '{} ({} healing)'.format(self.name, -self.damage)


class AttackDisintegrate(Attack):
    def __init__(self):
        Attack.__init__(self, 'Disintegrate', 9)

    def perform(self, source, target):
        Attack.perform(self, source, target)
        Attack.perform(self, source, source)


#==================================================================
player_name = 'Hiro'
player_key = player_name.lower()

combatants = {}
combatants[player_key] = Character(player_name, 20, [Attack('Slash', 4), AttackHeal()])
combatants['slimea'] = CharSlime('Slime A', 5, False)
combatants['slimeb'] = CharSlime('Slime B', 5, True)

# keep doing combat while player is alive, and they're not alone
while player_key in combatants.keys() and len(combatants) > 1:
    # write status of combat
    print 'Your attacks:'
    for atk in sorted(combatants[player_key].attacks.values()):
            print '  {}'.format(atk)
    print 'Remaining combatants:'
    for char in sorted(combatants.values()):
        print '  ' + str(char)
    # player attacks a monster
    atk_name = ''
    monster_name = ''
    while atk_name not in combatants[player_key].attacks.keys() or monster_name not in combatants.keys():
        atk_name, monster_name = raw_input('<attack> <combatant>: ').split(' ')
    combatants[player_key].attack_something(combatants[monster_name], atk_name)

    # monsters attack player
    for key, char in combatants.iteritems():
        if key == player_key:
            continue
        char.attack_something(combatants[player_key])

    # clean up dead combatants
    dead_monsters = []
    for key, monster in combatants.iteritems():
        if monster.hp <= 0:
            dead_monsters.append(key)
            print '{} has died!'.format(monster.name)
    for key in dead_monsters:
        del combatants[key]
    print ''

if player_key not in combatants.keys():
    print 'Failure.'
else:
    print 'Cleared!'

