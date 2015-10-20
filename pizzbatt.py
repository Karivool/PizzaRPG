import os
import copy
import random
import pizzenemy
import pizzspells


def enemy_formation(dungeon_num):
    enemy_amount_easy = (1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3)
    enemy_amount_med = (1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3)
    enemy_amount_hard = (1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3)
    if dungeon_num == 0:
        enemy_list = enemy_amount_easy
    elif dungeon_num == 1:
        enemy_list = enemy_amount_med
    else:
        enemy_list = enemy_amount_hard
    enemy_num = random.choice(enemy_list)
    return enemy_num


def fight_battle(hero, dungeon_num, area5):
    enemy1 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
    enemy2 = pizzenemy.Enemy("Blank", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
    enemy3 = pizzenemy.Enemy("Blank", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
    if area5:
        if dungeon_num == 0:
            enemy1 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
            enemy2 = copy.deepcopy(pizzenemy.foe_twinkie_star)
            enemy3 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
        elif dungeon_num == 1:
            enemy1 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
            enemy2 = copy.deepcopy(pizzenemy.foe_cave_drweller)
            enemy3 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
        elif dungeon_num == 2:
            enemy1 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
            enemy2 = copy.deepcopy(pizzenemy.foe_trilbyous_pursuit)
            enemy3 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
    else:
        enemy_num = enemy_formation(dungeon_num)
        if enemy_num == 2:
            enemy2 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
        if enemy_num == 3:
            enemy2 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
            enemy3 = copy.deepcopy(random.choice(pizzenemy.enemy_list[dungeon_num].values()))
    victory = battle_system(hero, enemy1, enemy2, enemy3)
    return victory


def choose_enemy(enemy1, enemy2, enemy3):
    command = 0
    selection = ["1", "b"]
    while command not in selection:
        selection = ["1", "b"]
        if enemy2.used:
            selection = ["1", "2", "b"]
        if enemy3.used:
            selection = ["1", "2", "3", "b"]
        print " "
        print "Attack which enemy?"
        if enemy1.hp > 0:
            print "(1) %s / HP: %s/%s" % (enemy1.name, enemy1.hp, enemy1.hp_ttl)
        else:
            selection.remove("1")
        if enemy2.used:
            if enemy2.hp > 0:
                print "(2) %s / HP: %s/%s" % (enemy2.name, enemy2.hp, enemy2.hp_ttl)
            else:
                selection.remove("2")
        if enemy3.used:
            if enemy3.hp > 0:
                print "(3) %s / HP: %s/%s" % (enemy3.name, enemy3.hp, enemy3.hp_ttl)
            else:
                selection.remove("3")
        print "(b) Back"
        command = raw_input().lower()
        if command not in selection:
            print "Invalid enemy selection!"
            command = 0
        else:
            return command


def battle_menu(hero, enemy1, enemy2, enemy3):
    os.system('cls')
    print "%s" % enemy1.name
    print "HP: %s/%s" % (enemy1.hp, enemy1.hp_ttl)
    if not enemy2.used:
        print "\n" * 1
    else:
        print "%s" % enemy2.name
        print "HP: %s/%s" % (enemy2.hp, enemy2.hp_ttl)
    if not enemy3.used:
        print "\n" * 1
    else:
        print "%s" % enemy3.name
        print "HP: %s/%s" % (enemy3.hp, enemy3.hp_ttl)
    print " "
    print "Name: %s    HP: %s/%s    MP: %s/%s" % (hero.name, hero.hp, hero.hp_ttl, hero.mp, hero.mp_ttl)
    print "(1) Attack   (2) Magic    (R) Run"
    print "(3) Items    (4) Status"
    print " "


def flee_batt(hero, enemy1, enemy2, enemy3):
    flee_chance = (hero.skl * .5 + hero.spd * 2 + hero.lck) + (random.randint(0, 10)) / \
                                                              ((enemy1.spd_ttl + enemy2.spd_ttl + enemy3.spd_ttl) *
                                                               round(random.uniform(.75, 1.75), 3))
    if flee_chance >= 1.0:
        return True
    else:
        return False


def attack_action(hero, enemy1, enemy2, enemy3, enemy_target, sp_choice):
    if sp_choice == "Cancelled":
        damage = int(hero.str_atk(enemy1, enemy2, enemy3, enemy_target))
    if enemy_target == "no_speed":
        hero_speed = 0
    else:
        hero_speed = hero.atk_spd()
    enemy1_speed = enemy1.atk_spd()
    enemy2_speed = enemy2.atk_spd()
    enemy3_speed = enemy3.atk_spd()
    rounds = 1
    if enemy1.used:
        rounds += 1
    if enemy2.used:
        rounds += 1
    if enemy3.used:
        rounds += 1
    while rounds != 0:
        hero_aim = hero.atk_aim()
        hero_dodge = hero.atk_dodge()
        enemy1_aim = enemy1.atk_aim()
        enemy1_dodge = enemy1.atk_dodge()
        enemy2_aim = enemy2.atk_aim()
        enemy2_dodge = enemy2.atk_dodge()
        enemy3_aim = enemy3.atk_aim()
        enemy3_dodge = enemy3.atk_dodge()
        if hero_speed >= enemy1_speed and hero_speed >= enemy2_speed and hero_speed >= enemy3_speed and hero_speed != 0:
            attacker = "hero"
            if hero.hp > 0:
                if enemy_target == "1":
                    if sp_choice != "Cancelled":
                        damage = int(pizzspells.spell_effects(hero, enemy1, enemy2, enemy3, attacker, enemy_target,
                                                              sp_choice))
                    if hero_aim > enemy1_dodge:
                        if (hero.crit_chance() / enemy1.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                            print "Critical hit!!"
                            print "%s does %s damage to %s!!" % (hero.name, damage * 3, enemy1.name)
                            enemy1.hp -= (damage * 3)
                        else:
                            print "%s does %s damage to %s!" % (hero.name, damage, enemy1.name)
                            enemy1.hp -= damage
                    else:
                        print "%s dodges the attack!" % enemy1.name
                elif enemy_target == "2":
                    if sp_choice != "Cancelled":
                        damage = int(pizzspells.spell_effects(hero, enemy1, enemy2, enemy3, attacker, enemy_target,
                                                              sp_choice))
                    if hero_aim > enemy2_dodge:
                        if (hero.crit_chance() / enemy2.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                            print "Critical hit!!"
                            print "%s does %s damage to %s!!" % (hero.name, damage * 3, enemy2.name)
                            enemy2.hp -= (damage * 3)
                        else:
                            print "%s does %s damage to %s!" % (hero.name, damage, enemy2.name)
                            enemy2.hp -= damage
                    else:
                        print "%s dodges the attack!" % enemy2.name
                elif enemy_target == "3":
                    if sp_choice != "Cancelled":
                        damage = int(pizzspells.spell_effects(hero, enemy1, enemy2, enemy3, attacker, enemy_target,
                                                              sp_choice))
                    if hero_aim > enemy3_dodge:
                        if (hero.crit_chance() / enemy3.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                            print "Critical hit!!"
                            print "%s does %s damage to %s!!" % (hero.name, damage * 3, enemy3.name)
                            enemy3.hp -= (damage * 3)
                        else:
                            print "%s does %s damage to %s!" % (hero.name, damage, enemy3.name)
                            enemy3.hp -= damage
                    else:
                        print "%s dodges the attack!" % enemy3.name
                else:
                    damage = int(pizzspells.spell_effects(hero, enemy1, enemy2, enemy3, attacker, enemy_target,
                                                          sp_choice))
                    print "You heal yourself for %s HP!" % damage
                    hero.hp += damage
                    if hero.hp > hero.hp_ttl:
                        hero.hp = hero.hp_ttl
            hero_speed = 0
            rounds -= 1
            print " "
        elif enemy1_speed >= enemy2_speed and enemy1_speed >= enemy3_speed:
            if enemy1.hp > 0:
                enemy_atk = enemy1.attack()
                damage1 = int(enemy_atk - (hero.def_ttl * random.uniform(.7, 1.2)))
                if damage1 < 0:
                    damage1 = 0
                if enemy1_aim > hero_dodge:
                    if (enemy1.crit_chance() / hero.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                        print "Oh no! Critical hit!!"
                        print "%s does %s damage!!" % (enemy1.name, damage1 * 3)
                        hero.hp -= (damage1 * 3)
                    else:
                        hero.hp -= damage1
                        print "%s does %s damage!" % (enemy1.name, damage1)
                else:
                    print "You dodge %s's attack!" % enemy1.name
            enemy1_speed = 0
            rounds -= 1
            print " "
        elif enemy2_speed >= enemy3_speed:
            if enemy2.hp > 0:
                enemy_atk = enemy2.attack()
                damage2 = int(enemy_atk - (hero.def_ttl * random.uniform(.7, 1.2)))
                if damage2 < 0:
                    damage2 = 0
                if enemy2_aim > hero_dodge:
                    if (enemy2.crit_chance() / hero.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                        print "Oh no! Critical hit!!"
                        print "%s does %s damage!!" % (enemy2.name, damage2 * 3)
                        hero.hp -= (damage2 * 3)
                    else:
                        hero.hp -= damage2
                        print "%s does %s damage!" % (enemy2.name, damage2)
                else:
                    print "You dodge %s's attack!" % enemy2.name
            enemy2_speed = 0
            rounds -= 1
            print " "
        else:
            if enemy3.hp > 0:
                enemy_atk = enemy3.attack()
                damage3 = int(enemy_atk - (hero.def_ttl * random.uniform(.7, 1.2)))
                if damage3 < 0:
                    damage3 = 0
                if enemy3_aim > hero_dodge:
                    if (enemy3.crit_chance() / hero.lck_ttl) / 15.0 > round(random.uniform(0.0, 1.0), 3):
                        print "Oh no! Critical hit!!"
                        print "%s does %s damage!!" % (enemy3.name, damage3 * 3)
                        hero.hp -= (damage3 * 3)
                    else:
                        hero.hp -= damage3
                        print "%s does %s damage!" % (enemy3.name, damage3)
                else:
                    print "You dodge %s's attack!" % enemy3.name
            enemy3_speed = 0
            rounds -= 1
            print " "
    raw_input()
    return


def give_gold(enemy1, enemy2, enemy3):
    gold_add = enemy1.gold + enemy2.gold + enemy3.gold
    return gold_add


def give_exp(enemy1, enemy2, enemy3):
    exp_add = enemy1.exp + enemy2.exp + enemy3.exp
    return exp_add


def battle_system(hero, enemy1, enemy2, enemy3):
    command_keys = ("1", "2", "3", "4", "r")
    command = 0
    enemy_target = 0
    in_menu = True
    fled_failed = False
    while hero.is_alive:
        while hero.in_battle:
            while in_menu:
                while command not in command_keys and not fled_failed:
                    battle_menu(hero, enemy1, enemy2, enemy3)
                    if hero.bad_key:
                        print "Not a valid command!"
                    command = raw_input().lower()
                    if command not in command_keys:
                        hero.bad_key = True
                        command = 0
                    else:
                        hero.bad_key = False
                if command == "1":
                    enemy_target = choose_enemy(enemy1, enemy2, enemy3)
                    if enemy_target != "b":
                        sp_choice = "Cancelled"
                        attack_action(hero, enemy1, enemy2, enemy3, enemy_target, sp_choice)
                elif command == "2":
                    sp_choice = hero.spell()
                    if sp_choice != "Cancelled":
                        if not hero.spells[sp_choice - 1].healing:
                            enemy_target = choose_enemy(enemy1, enemy2, enemy3)
                        else:
                            enemy_target = "self"
                        if enemy_target != "b":
                                attack_action(hero, enemy1, enemy2, enemy3, enemy_target, sp_choice)
                elif command == "3":
                    used_item = hero.inventory_sys(True)
                    if used_item:
                        enemy_target = "no_speed"
                        sp_choice = 0
                        attack_action(hero, enemy1, enemy2, enemy3, enemy_target, sp_choice)
                    else:
                        enemy_target = "b"
                elif command == "4":
                    from pizztown import stats
                    stats(hero)
                    enemy_target = "b"
                else:
                    print "You attempt to make a hasty retreat!"
                    flee_succeed = flee_batt(hero, enemy1, enemy2, enemy3)
                    if flee_succeed:
                        print "You successfully escape!"
                        raw_input()
                        return False
                    else:
                        print "Eek! You fail to make your escape!"
                        raw_input()
                        fled_failed = True
                if enemy1.hp < 0:
                    enemy1.hp = 0
                if enemy2.hp < 0:
                    enemy2.hp = 0
                if enemy3.hp < 0:
                    enemy3.hp = 0
                if enemy_target != "b":
                    if enemy1.hp + enemy2.hp + enemy3.hp == 0:
                        in_menu = False
                        hero.in_battle = False
                    else:
                        command = 0
                    if hero.hp <= 0:
                        hero.is_alive = False
                        hero.in_battle = False
                        hero.location = "dead"
                        return "dead"
                else:
                    command = 0
        gold_add = give_gold(enemy1, enemy2, enemy3)
        exp_add = give_exp(enemy1, enemy2, enemy3)
        os.system('cls')
        print "You are victorious!"
        print "You gained %s gold and %s EXP." % (gold_add, exp_add)
        raw_input()
        hero.gold += gold_add
        hero.exp += exp_add
        hero.level_up()
        return True
