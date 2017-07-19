---
category: info
info_order: 5
date: 2017-07-12 00:25 -07:00
title: RPG combat
---

```bash
Your attacks:
  Slash (4 dmg)
  Heal (8 healing)
Remaining combatants:
  Hiro (20/20 hp)
  Slime A (5/5 hp)
  Slime B (5/5 hp)
<attack> <combatant>: slash slimea
Hiro used Slash (4 dmg) on Slime A (1/5 hp)
Slime B used Disintegrate (9 dmg) on Hiro (11/20 hp)
Slime B used Disintegrate (9 dmg) on Slime B (0/5 hp)
Slime A used Acid (2 dmg) on Hiro (9/20 hp)
Slime B has died!
```
<!-- more -->

[The complete RPG combat.]({{ site.baseurl }}{% link /assets/rpg-complete.py %})

---

## Extra credit

1. Be more informative/helpful when the player doesn't know the key names for monsters.
2. Give attacks a chance to miss (accuracy rating).  Print it out when listing attacks.  Or, give them a chance to critically hit for double damage.
3. Make up a new attack type, and implement it.  You may have to change the Attack class and/or the combat code.  Suggestions:
	- Attack all targets in a list.
	- Make an attack have a certain number of charges available (think items or mana).

