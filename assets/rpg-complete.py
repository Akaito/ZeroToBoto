# rpg-complete.py

import random


class Character(object):
    name = 'UNNAMED'
    hp = 0
    hp_max = 0
    attacks = {}

    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.attacks = {}
        for attack in attacks:
            self.attacks[attack.name] = attack

    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def attack_something(self, target, attack=None):
        if attack is None:
            attack = random.choice(self.attacks.values())
            #print '  DEBUG: Chose attack {} at random from {}'.format(attack, self.attacks)
        attack.perform(self, target)


class Attack(object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} dmg)'.format(self.name, self.damage)

    def perform(self, source, target):
        target.hp = min(max(0, target.hp - self.damage), target.hp_max)
        print '{} used {} on {}'.format(source, self, target)


class AttackSlash(Attack):
    def __init__(self):
        Attack.__init__(self, 'Slash', 4)


class AttackPunch(Attack):
    def __init__(self):
        Attack.__init__(self, 'Punch', 1)


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


class AttackExplode(Attack):
    def __init__(self):
        Attack.__init__(self, 'Explode', 9)


#==================================================================
monsters = {}
player = Character('Alice', 20, [AttackSlash()])

# characters['Bob'] = Character('Bob', 12, TEAM_PLAYER, [AttackPunch(), AttackHeal()])
monsters['SlimeA'] = Character('SlimeA', 5, [AttackAcid()])
monsters['SlimeB'] = Character('SlimeB', 5, [AttackAcid(), AttackExplode()])

player.attack_something(monsters['SlimeB'])
monsters['SlimeB'].attack_something(player)

