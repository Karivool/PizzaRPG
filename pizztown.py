import os
import random
import pizzitems
import pizzspells

try:
    import pizzsave
except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
    pass
try:
    import pizzsave2
except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
    pass
try:
    import pizzsave3
except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
    pass
from pizzdungeon import dungeon


def buy_item(hero, comm_key, store_id):
    item_num = 0
    item_added = 0
    comm_key -= 1
    if store_id == "armory":
        buy_list = pizzitems.armor_buy_list
    elif store_id == "general_store":
        buy_list = pizzitems.item_buy_list
    else:
        buy_list = pizzitems.weapon_buy_list
    while item_num != 16:
        if hero.inv[item_num] != pizzitems.item_empty:
            item_num += 1
            if item_num == 16:
                print "Your inventory is too full to store anything else!"
                item_added = False
        else:
            if hero.gold >= buy_list[comm_key].cost:
                hero.inv[item_num] = buy_list[comm_key]
                item_num = 16
                hero.gold -= buy_list[comm_key].cost
                print "%s purchased." % buy_list[comm_key].name
                item_added = True
            else:
                item_num = 16
                print "You don't have enough money!"
                item_added = False
    return item_added


def sell_item(hero, comm_key, store_id):
    item_sold = 0
    command = 0
    comm_key -= 1
    options = ("y", "n")
    if store_id == "general_store":
        pass
    if hero.inv[comm_key] != pizzitems.item_empty:
        item_name = hero.inv[comm_key].name
        item_value = int(hero.inv[comm_key].cost * .6)
        while command not in options:
            os.system('cls')
            print "%s value: %s Gold" % (item_name, item_value)
            print "Would you like to sell this item?"
            print "(Y) Yes  (N) No"
            if hero.bad_key:
                print "A simple yes or no will suffice.."
            command = raw_input().lower()
            if command in options:
                hero.bad_key = False
            if command == "y":
                hero.inv[comm_key] = pizzitems.item_empty
                hero.gold += item_value
                print "Thanks for the %s, here's %s Gold." % (item_name, item_value)
                raw_input()
            elif command == "n":
                return False
            else:
                hero.bad_key = True
    else:
        print "You can't sell me nothing!"
        item_sold = False
    return item_sold


def add_item(hero, temp_slot):
    item_num = 0
    item_added = 0
    while item_num != 16:
        if hero.inv[item_num] != pizzitems.item_empty:
            item_num += 1
            if item_num == 16:
                print "Your inventory is too full to store anything else!"
                item_added = False
        else:
            hero.inv[item_num] = temp_slot
            item_num = 16
            item_added = True
    return item_added


def inn(hero):
    comm_key = 0
    inn_cost = 15 + int(hero.lvl + 1.12 * 1.75)
    while comm_key not in ("r", "t", "b"):
        os.system('cls')
        print " "
        print "Welcome to the Brook N Lynne Inn!"
        print " "
        print "Gold:", hero.gold
        print "HP:  ", hero.hp, "/", hero.hp_ttl
        print "MP:  ", hero.mp, "/", hero.mp_ttl
        print " "
        print "(R) Rest (%s gold)" % inn_cost
        print "(T) Talk"
        print "(B) Back"
        print " "
        if hero.bad_key:
            print "This is a place for resting, not whatever you're suggesting!"
        comm_key = raw_input().lower()
        if comm_key in ("r", "t", "e"):
            hero.bad_key = False
        print "\n"
        if comm_key == "r":
            comm_key = 0
            if hero.gold >= inn_cost:
                print "A good rest restores your health to full!"
                hero.hp = hero.hp_ttl
                hero.mp = hero.mp_ttl
                hero.gold -= inn_cost
                raw_input()
            else:
                print "You don't have enough money!"
                raw_input()
        elif comm_key == "t":
            comm_key = 0
            chat = random.randint(1, 6)
            if chat == 1:
                print "Here at Brook N Lynne Inn, we prefer to think of our bed bugs as 'bed pals'!"
            elif chat == 2:
                print "The reason your health and magic points improve so fast when you sleep with us?"
                print "Our rooms are so unsettling your body does what it needs to leave right away!"
            elif chat == 3:
                print "What did the mattress say to the exhausted busybody workaholic?"
                print "Leave the rest to me!"
            elif chat == 4:
                print "What did the mattress say to the frisky couple?"
                print "Looks like it's time to spring into action!"
            elif chat == 5:
                print "What kind of creatures blossom into blanketflies?"
                print "Caterpillows!"
            else:
                print "You can use our beds as a makeshift money deposit box. It'll be a great cushion"
                print "for your savings!"
            raw_input()
        elif comm_key == "b":
            return
        else:
            hero.bad_key = True


def forge(hero):
    comm_key = 0
    list_plus = 0
    item_list_nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    while comm_key not in ("p", "t", "b"):
        os.system('cls')
        print " "
        print "Welcome to the Bronxe Forge!"
        print " "
        print "Gold:", hero.gold
        print " "
        print "(P) Purchase"
        print "(T) Talk"
        print "(B) Back"
        print " "
        if hero.bad_key:
            print "Ha! Did you hear what %s just said? We don't have that here!" % hero.he
        comm_key = raw_input().lower()
        if comm_key in ("p", "t", "b"):
            hero.bad_key = False
        if comm_key == "p":
            while comm_key != 0:
                os.system('cls')
                print "What would you like to purchase?"
                print "Your Gold: %s" % hero.gold
                print " "
                print "(%s): %s - %s Gold" % (1 + list_plus, pizzitems.weapon_buy_list
                                              [0 + list_plus].name, pizzitems.weapon_buy_list[0 + list_plus].cost)
                print "(%s): %s - %s Gold" % (2 + list_plus, pizzitems.weapon_buy_list
                                              [1 + list_plus].name, pizzitems.weapon_buy_list[1 + list_plus].cost)
                print "(%s): %s - %s Gold" % (3 + list_plus, pizzitems.weapon_buy_list
                                              [2 + list_plus].name, pizzitems.weapon_buy_list[2 + list_plus].cost)
                print "(Q) << Show previous || (W) Show next >>"
                print "(B) Back"
                if hero.bad_key:
                    print "You're buying what now?!"
                print " "
                comm_key = raw_input().lower()
                if comm_key == "b":
                    comm_key = 0
                elif comm_key == "q":
                    if not list_plus <= 0:
                        list_plus -= 3
                elif comm_key == "w":
                    if list_plus <= 0:
                        list_plus += 3
                elif comm_key not in item_list_nums:
                    hero.bad_key = True
                else:
                    hero.bad_key = False
                    store_id = "forge"
                    buy_item(hero, int(comm_key), store_id)
                    raw_input()
            comm_key = 0
        elif comm_key == "t":
            comm_key = 0
            chat = random.randint(1, 6)
            if chat == 1:
                print "Our weapons are so magnificent, they'll cut you to the very core!"
            elif chat == 2:
                print "We had some actors come in needing some weapons to rehearse for a show. They"
                print "were given a few swords, so they took their scripts and blade out their scene!"
            elif chat == 3:
                print "Our business values customer service and keeping our buyers happy. After all,"
                print "we need to build and forge strong relationships!"
            elif chat == 4:
                print "A knight of promise must always keep %s sword" % hero.his
            elif chat == 5:
                print "We had to stop selling the weapon, Manchester, meant to carve open men's"
                print "rib cages. Half our customer base boycotted it, claiming they found it"
                print "extremely offensive."
            else:
                print "The Staff of Hearts is a mystical weapon, known only to be wielded by a"
                print "Pizza Lady. You can wand-er about the lands all you want, but you'll"
                print "never find it!"
            raw_input()
        elif comm_key == "b":
            return
        else:
            hero.bad_key = True


def armory(hero):
    comm_key = 0
    list_plus = 0
    item_list_nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    while comm_key not in ("b", "t", "e"):
        os.system('cls')
        print " "
        print "Welcome to Queen's Armory!"
        print " "
        print "Gold:", hero.gold
        print " "
        print "(P) Purchase"
        print "(T) Talk"
        print "(B) Back"
        print " "
        if hero.bad_key:
            print "We don't sell that kind of thing here, you silly %s!" % hero.gender
        comm_key = raw_input().lower()
        if comm_key in ("p", "t", "b"):
            hero.bad_key = False
        if comm_key == "p":
            while comm_key != 0:
                os.system('cls')
                print "What would you like to purchase?"
                print "Your Gold: %s" % hero.gold
                print " "
                print "(%s): %s - %s Gold" % (1 + list_plus, pizzitems.armor_buy_list
                                              [0 + list_plus].name, pizzitems.armor_buy_list[0 + list_plus].cost)
                print "(%s): %s - %s Gold" % (2 + list_plus, pizzitems.armor_buy_list
                                              [1 + list_plus].name, pizzitems.armor_buy_list[1 + list_plus].cost)
                print "(%s): %s - %s Gold" % (3 + list_plus, pizzitems.armor_buy_list
                                              [2 + list_plus].name, pizzitems.armor_buy_list[2 + list_plus].cost)
                print "(Q) << Show previous || (W) Show next >>"
                print "(B) Back"
                if hero.bad_key:
                    print "You're buying what now?!"
                print " "
                comm_key = raw_input().lower()
                if comm_key == "b":
                    comm_key = 0
                elif comm_key == "q":
                    if not list_plus <= 0:
                        list_plus -= 3
                elif comm_key == "w":
                    if list_plus < 9:
                        list_plus += 3
                elif comm_key not in item_list_nums:
                    hero.bad_key = True
                elif comm_key not in item_list_nums:
                    hero.bad_key = True
                else:
                    hero.bad_key = False
                    store_id = "armory"
                    buy_item(hero, int(comm_key), store_id)
                    raw_input()
            comm_key = 0
        elif comm_key == "t":
            comm_key = 0
            chat = random.randint(1, 6)
            if chat == 1:
                print "Get our armor while it lasts, it's a real steel!"
            elif chat == 2:
                print "Getting insurance with our gear is great for some extra protection."
            elif chat == 3:
                print "Did you know? Those who buy our stuff strongly resist being hit by magic."
            elif chat == 4:
                print "One of our customers tried to return some iron platelegs the other day."
                print "When asked how it was used, they got defensive."
            elif chat == 5:
                print "Men and women have said our gender neutral tops are the breast plates"
                print "they've ever purchased!"
            else:
                print "The mystical Chef's Hat is only worn by a pizza of introverted emotional"
                print "being. It raises luck like mad!"
            raw_input()
        elif comm_key == "b":
            return
        else:
            hero.bad_key = True


def g_store(hero):
    store_id = "general_store"
    list_plus = 0
    comm_key = 0
    item_list_nums = ("1", "2", "3", "4", "5", "6")
    sell_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", 1)
    while comm_key not in ("p", "s", "t", "b"):
        os.system('cls')
        print " "
        print "Welcome to Man Hats And More General Store!"
        print " "
        print "Gold:", hero.gold
        print " "
        print "(P) Purchase"
        print "(S) Sell"
        print "(T) Talk"
        print "(B) Back"
        print " "
        if hero.bad_key:
            print "We don't deal with those sorts of goods, mate."
        comm_key = raw_input().lower()
        if comm_key in ("p", "s", "t", "b"):
            hero.bad_key = False
        print "\n"
        if comm_key == "p":
            while comm_key != 0:
                os.system('cls')
                print "What would you like to purchase?"
                print "Your Gold: %s" % hero.gold
                print " "
                print "(%s): %s - %s Gold" % (1 + list_plus, pizzitems.item_buy_list
                                              [0 + list_plus].name, pizzitems.item_buy_list[0 + list_plus].cost)
                print "(%s): %s - %s Gold" % (2 + list_plus, pizzitems.item_buy_list
                                              [1 + list_plus].name, pizzitems.item_buy_list[1 + list_plus].cost)
                print "(%s): %s - %s Gold" % (3 + list_plus, pizzitems.item_buy_list
                                              [2 + list_plus].name, pizzitems.item_buy_list[2 + list_plus].cost)
                print "(Q) << Show previous || (W) Show next >>"
                print "(B) Back"
                if hero.bad_key:
                    print "You're buying what now?!"
                print " "
                comm_key = raw_input().lower()
                if comm_key == "b":
                    comm_key = 0
                elif comm_key == "q":
                    if not list_plus <= 0:
                        list_plus -= 3
                elif comm_key == "w":
                    if list_plus <= 0:
                        list_plus += 3
                elif comm_key not in item_list_nums:
                    hero.bad_key = True
                else:
                    hero.bad_key = False
                    buy_item(hero, int(comm_key), store_id)
                    raw_input()
        elif comm_key == "s":
            while comm_key != 0:
                os.system('cls')
                print "Your Gold: %s" % hero.gold
                hero.inventory_menu(menuing=True)
                print "What would you like to sell?"
                if hero.bad_key:
                    print "We don't know what you're selling."
                print " "
                comm_key = raw_input().lower()
                print comm_key
                if comm_key == "b":
                    print "Back"
                    comm_key = 0
                elif comm_key not in sell_list:
                    hero.bad_key = True
                else:
                    hero.bad_key = False
                    sold = sell_item(hero, int(comm_key), store_id)
                    if sold:
                        raw_input()
        elif comm_key == "t":
            comm_key = 0
            chat = random.randint(1, 6)
            if chat == 1:
                print "Our healing potions are cheap, so you can recover the cost through battle fast!"
            elif chat == 2:
                print "Getting inflicted with status effects are a terrible poison on your health!"
            elif chat == 3:
                print "What did the shopkeeper say to the salesman who tried to pawn them a 'valuable' gem?"
                print "I don't buy it."
            elif chat == 4:
                print "What do you call a store that goes bankrupt without selling a single item?"
                print "Sellibite!"
            elif chat == 5:
                print "What is a fitting name for a woman who showcases products to get others"
                print "to buy it?"
                print "Ad-manda!"
            else:
                print "What did the shopkeeper say as they opened their box of buyable goods?"
                print "See what's in store!"
            raw_input()
        elif comm_key == "b":
            return
        else:
            hero.bad_key = True


def inventory(hero):
    hero.inventory_sys(False)
    return


def stats(hero):
    os.system('cls')
    print "%s - Level %s   %s" % (hero.name, hero.lvl, hero.mbti)
    print "--------------------------------------"
    print "HP: ", hero.hp, "/", hero.hp_ttl
    print "MP: ", hero.mp, "/", hero.mp_ttl
    print "Str:", hero.atk_ttl
    print "Mag:", hero.mag_ttl
    print "Skl:", hero.skl_ttl
    print "Spd:", hero.spd_ttl
    print "Lck:", hero.lck_ttl
    print "Def:", hero.def_ttl
    print "Res:", hero.res_ttl
    print " "
    print "Gold:", hero.gold
    print "EXP: ", hero.exp, "  " "To next:", hero.exp_ttl - hero.exp
    print " "
    print "Press Enter to return."
    raw_input()
    print "\n" * 10
    return


def equip_gear(hero):
    command = 0
    temp_slot = pizzitems.item_empty
    eq_slots = ("1", "2", "3", "4", "5", "b")
    item_slots = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "b")
    while command != "b":
        os.system('cls')
        print "Which slot would you like to change?"
        print "(1) Weapon: %s" % hero.weapon.name
        print "(2) Head: %s" % hero.head.name
        print "(3) Chest: %s" % hero.body.name
        print "(4) Legs: %s" % hero.legs.name
        print "(5) Accessory: %s" % hero.accs.name
        print "(B) Back"
        if hero.bad_key:
            print "That's not any part of your body!"
        print " "
        command = raw_input().lower()
        if command in eq_slots:
            hero.bad_key = False
            if command == "1":
                slot_type = "Weapon"
                command = 0
            elif command == "2":
                slot_type = "Head"
                command = 0
            elif command == "3":
                slot_type = "Body"
                command = 0
            elif command == "4":
                slot_type = "Legs"
                command = 0
            elif command == "5":
                slot_type = "Accessory"
                command = 0
            else:
                command = "b"
            while command not in item_slots:
                os.system('cls')
                hero.inventory_menu(menuing=True)
                print "Which item would you like to equip for the %s slot?" % slot_type
                command = raw_input().lower()
                try:
                    choice = int(command) - 1
                    if slot_type == "Weapon" and hero.inv[choice].wep:
                        if hero.weapon != pizzitems.we_none:
                            temp_slot = hero.weapon
                        hero.weapon = hero.inv[choice]
                        hero.inv[choice] = pizzitems.item_empty
                        if temp_slot != pizzitems.item_empty:
                            add_item(hero, temp_slot)
                        print "%s equipped." % hero.weapon
                        raw_input()
                    elif slot_type == "Head" and hero.inv[choice].head:
                        if hero.head != pizzitems.ar_none:
                            temp_slot = hero.head
                        hero.head = hero.inv[choice]
                        hero.inv[choice] = pizzitems.item_empty
                        if temp_slot != pizzitems.item_empty:
                            add_item(hero, temp_slot)
                        print "%s equipped." % hero.head
                        raw_input()
                    elif slot_type == "Body" and hero.inv[choice].body:
                        if hero.body != pizzitems.ar_none:
                            temp_slot = hero.body
                        hero.body = hero.inv[choice]
                        hero.inv[choice] = pizzitems.item_empty
                        if temp_slot != pizzitems.item_empty:
                            add_item(hero, temp_slot)
                        print "%s equipped." % hero.body
                        raw_input()
                    elif slot_type == "Legs" and hero.inv[choice].legs:
                        if hero.legs != pizzitems.ar_none:
                            temp_slot = hero.legs
                        hero.legs = hero.inv[choice]
                        hero.inv[choice] = pizzitems.item_empty
                        if temp_slot != pizzitems.item_empty:
                            add_item(hero, temp_slot)
                        print "%s equipped." % hero.legs
                        raw_input()
                    elif slot_type == "Accessory" and hero.inv[choice].accs:
                        if hero.accs != pizzitems.ar_none:
                            temp_slot = hero.accs
                        hero.accs = hero.inv[choice]
                        hero.inv[choice] = pizzitems.item_empty
                        if temp_slot != pizzitems.item_empty:
                            add_item(hero, temp_slot)
                        print "%s equipped." % hero.accs
                        raw_input()
                    else:
                        print "You can't equip that there!"
                        raw_input()
                except (KeyError, AttributeError, ValueError):
                    if command == "b":
                        pass
                    else:
                        print "You can't equip that there!"
                        raw_input().lower()
        else:
            hero.bad_key = True
    return


def remove_gear(hero):
    command = 0
    eq_slots = ("1", "2", "3", "4", "5")
    while command != "b":
        os.system('cls')
        print "Which item would you like to remove?"
        print "(1) Weapon: %s" % hero.weapon.name
        print "(2) Head: %s" % hero.head.name
        print "(3) Chest: %s" % hero.body.name
        print "(4) Legs: %s" % hero.legs.name
        print "(5) Accessory: %s" % hero.accs.name
        print "(B) Back"
        if hero.bad_key:
            print "You can't remove that!"
        print " "
        command = raw_input().lower()
        if command in eq_slots:
            hero.bad_key = False
            if command == "1":
                slot_type = "Weapon"
                command = 0
            elif command == "2":
                slot_type = "Head"
                command = 0
            elif command == "3":
                slot_type = "Body"
                command = 0
            elif command == "4":
                slot_type = "Legs"
                command = 0
            else:
                slot_type = "Accessory"
                command = 0
            if slot_type == "Weapon":
                if hero.weapon == pizzitems.we_none:
                    print "You're bare-fisted, silly!"
                else:
                    temp_slot = hero.weapon
                    removed = add_item(hero, temp_slot)
                    if removed:
                        hero.weapon = pizzitems.we_none
                        print "%s unequipped." % temp_slot
            elif slot_type == "Head":
                if hero.head == pizzitems.ar_none:
                    print "You're bare-headed, silly!"
                else:
                    temp_slot = hero.head
                    removed = add_item(hero, temp_slot)
                    if removed:
                        hero.head = pizzitems.ar_none
                        print "%s unequipped." % temp_slot
            elif slot_type == "Body":
                if hero.body == pizzitems.ar_none:
                    print "You're topless, silly!"
                else:
                    temp_slot = hero.body
                    removed = add_item(hero, temp_slot)
                    if removed:
                        hero.body = pizzitems.ar_none
                        print "%s unequipped." % temp_slot
            elif slot_type == "Legs":
                if hero.legs == pizzitems.ar_none:
                    print "You're already pantless you weirdo.."
                else:
                    temp_slot = hero.legs
                    removed = add_item(hero, temp_slot)
                    if removed:
                        hero.legs = pizzitems.ar_none
                        print "%s unequipped." % temp_slot
            else:
                if hero.accs == pizzitems.ar_none:
                    print "You have no nice accessories on. :("
                else:
                    temp_slot = hero.accs
                    removed = add_item(hero, temp_slot)
                    if removed:
                        hero.accs = pizzitems.ar_none
                        print "%s unequipped." % temp_slot
            raw_input()
        elif command == "b":
            pass
        else:
            hero.bad_key = True
    return


def equipment(hero):
    command = 0
    equip_comm = ("1", "2", "b")
    while command not in equip_comm:
        os.system('cls')
        print "%s's Equipment" % hero.name
        print " "
        print "-------------------------------------------------------------------------------"
        print hero.weapon.name
        print "Weapon:    %s" % hero.weapon.name
        print "HP +%s |MP +%s |Str +%s |Mag +%s |Skl +%s |Spd +%s |Lck +%s |Def +%s |Res +%s |" \
              % (hero.weapon.hp_max, hero.weapon.mp_max, hero.weapon.pwr, hero.weapon.mag, hero.weapon.skl,
                 hero.weapon.spd, hero.weapon.lck, hero.weapon.blck, hero.weapon.res)
        print "-------------------------------------------------------------------------------"
        print "Head:      %s" % hero.head.name
        print "HP +%s |MP +%s |Str +%s |Mag +%s |Skl +%s |Spd +%s |Lck +%s |Def +%s |Res +%s |" \
              % (hero.head.hp_max, hero.head.mp_max, hero.head.pwr, hero.head.mag, hero.head.skl,
                 hero.head.spd, hero.head.lck, hero.head.blck, hero.head.res)
        print "-------------------------------------------------------------------------------"
        print "Chest:     %s" % hero.body.name
        print "HP +%s |MP +%s |Str +%s |Mag +%s |Skl +%s |Spd +%s |Lck +%s |Def +%s |Res +%s |" \
              % (hero.body.hp_max, hero.body.mp_max, hero.body.pwr, hero.body.mag, hero.body.skl,
                 hero.body.spd, hero.body.lck, hero.body.blck, hero.body.res)
        print "-------------------------------------------------------------------------------"
        print "Legs:      %s" % hero.legs.name
        print "HP +%s |MP +%s |Str +%s |Mag +%s |Skl +%s |Spd +%s |Lck +%s |Def +%s |Res +%s |" \
              % (hero.legs.hp_max, hero.legs.mp_max, hero.legs.pwr, hero.legs.mag, hero.legs.skl,
                 hero.legs.spd, hero.legs.lck, hero.legs.blck, hero.legs.res)
        print "-------------------------------------------------------------------------------"
        print "Accessory: %s" % hero.accs.name
        print "HP +%s |MP +%s |Str +%s |Mag +%s |Skl +%s |Spd +%s |Lck +%s |Def +%s |Res +%s |" \
              % (hero.accs.hp_max, hero.accs.mp_max, hero.accs.pwr, hero.accs.mag, hero.accs.skl,
                 hero.accs.spd, hero.accs.lck, hero.accs.blck, hero.accs.res)
        print "-------------------------------------------------------------------------------"
        print " "
        print "(1) Equip    (2) Unequip."
        print "(B) Back"
        if hero.bad_key:
            print "I don't understand that command."
        command = raw_input()
        if command not in equip_comm:
            hero.bad_key = True
        else:
            hero.bad_key = False
            if command == "1":
                equip_gear(hero)
                command = 0
            elif command == "2":
                remove_gear(hero)
                command = 0
            else:
                return
    return


def save_game(hero):
    global savegame, savegame
    comm_key = 0
    save_choices = ("1", "2", "3", "b")
    while comm_key not in save_choices:
        os.system('cls')
        print " " * 1
        print "Which save file will you write to?"
        try:
            savegame = open("pizzsave.py", 'r')
            try:
                name_save = pizzsave.savegame[0]
                lvl_save = pizzsave.savegame[20]
                mbti_save = pizzsave.savegame[21]
                print "(1) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                print "(1) Empty"
        except IOError:
            print "(1) Empty"
        try:
            savegame = open("pizzsave2.py", 'r')
            try:
                name_save = pizzsave2.savegame[0]
                lvl_save = pizzsave2.savegame[20]
                mbti_save = pizzsave2.savegame[21]
                print "(2) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                print "(2) Empty"
        except IOError:
            print "(2) Empty"
        try:
            savegame = open("pizzsave3.py", 'r')
            try:
                name_save = pizzsave3.savegame[0]
                lvl_save = pizzsave3.savegame[20]
                mbti_save = pizzsave3.savegame[21]
                print "(3) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                print "(3) Empty"
        except IOError:
            print "(3) Empty"
        print "(B) Back"
        print " "
        comm_key = raw_input()
        if comm_key == "1":
            savegame = open("pizzsave.py", 'w')
        elif comm_key == "2":
            savegame = open("pizzsave2.py", 'w')
        elif comm_key == "3":
            savegame = open("pizzsave3.py", 'w')
        elif comm_key == "b":
            print "Game not saved"
            raw_input()
            return
        else:
            print "Invalid file number!"
            print raw_input()
    print "Writing to file"
    save_file = (hero.name, hero.sex, hero.gender, hero.he, hero.his, hero.him,
                 hero.hp, hero.hp_max, hero.mp, hero.mp_max, hero.pwr, hero.mag,
                 hero.skl, hero.spd, hero.lck, hero.blck, hero.res, hero.gold,
                 hero.exp, hero.exp_ttl, hero.lvl, hero.mbti)
    equip1 = hero.weapon.idnum
    equip2 = hero.head.idnum
    equip3 = hero.body.idnum
    equip4 = hero.legs.idnum
    equip5 = hero.accs.idnum
    spells = (hero.spells[0].id_num, hero.spells[1].id_num, hero.spells[2].id_num, hero.spells[3].id_num,
              hero.spells[4].id_num, hero.spells[5].id_num, hero.spells[6].id_num, hero.spells[7].id_num,
              hero.spells[8].id_num, hero.spells[9].id_num, hero.spells[10].id_num, hero.spells[11].id_num)
    inv = (hero.inv[0].idnum, hero.inv[1].idnum, hero.inv[2].idnum, hero.inv[3].idnum, hero.inv[4].idnum,
           hero.inv[5].idnum, hero.inv[6].idnum, hero.inv[7].idnum, hero.inv[8].idnum, hero.inv[9].idnum,
           hero.inv[10].idnum, hero.inv[11].idnum, hero.inv[12].idnum, hero.inv[13].idnum, hero.inv[14].idnum,
           hero.inv[15].idnum)
    equipped = (equip1, equip2, equip3, equip4, equip5)
    savegame.write("savegame = " + str(save_file) + "\n" + "equipped = " + str(equipped) + "\n" + "inv = " + str(inv) +
                   "\n" + "spells = " + str(spells))
    savegame.close()
    print "Game saved."
    hero.saved = True
    raw_input()
    return


def load_game(hero):
    comm_key = 0
    load_options = ("1", "2", "3", "b")
    loaded = False
    while comm_key not in load_options:
        os.system('cls')
        print "Which save file will you load?"
        try:
            from pizzsave import savegame
            name_save = savegame[0]
            lvl_save = savegame[20]
            mbti_save = savegame[21]
            print "(1) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            print "(1) Empty"
        try:
            from pizzsave2 import savegame
            name_save = savegame[0]
            lvl_save = savegame[20]
            mbti_save = savegame[21]
            print "(2) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            print "(2) Empty"
        try:
            from pizzsave3 import savegame
            name_save = savegame[0]
            lvl_save = savegame[20]
            mbti_save = savegame[21]
            print "(3) %s - Level %s: %s" % (name_save, lvl_save, mbti_save)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            print "(3) Empty"
        print "(B) Back"
        print " "
        comm_key = raw_input().lower()
        if comm_key == "1":
            try:
                from pizzsave import savegame
                from pizzsave import equipped
                from pizzsave import inv
                from pizzsave import spells
                loaded = True
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                pass
        elif comm_key == "2":
            try:
                from pizzsave2 import savegame
                from pizzsave2 import equipped
                from pizzsave2 import inv
                from pizzsave2 import spells
                loaded = True
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                pass
        elif comm_key == "3":
            try:
                from pizzsave3 import savegame
                from pizzsave3 import equipped
                from pizzsave3 import inv
                from pizzsave3 import spells
                loaded = True
            except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
                pass
        elif comm_key == "b":
            return False
        if loaded:
            try:
                hero.name = savegame[0]
                hero.sex = savegame[1]
                hero.gender = savegame[2]
                hero.he = savegame[3]
                hero.his = savegame[4]
                hero.him = savegame[5]
                hero.hp = savegame[6]
                hero.hp_max = savegame[7]
                hero.mp = savegame[8]
                hero.mp_max = savegame[9]
                hero.pwr = savegame[10]
                hero.mag = savegame[11]
                hero.skl = savegame[12]
                hero.spd = savegame[13]
                hero.lck = savegame[14]
                hero.blck = savegame[15]
                hero.res = savegame[16]
                hero.gold = savegame[17]
                hero.exp = savegame[18]
                hero.exp_ttl = savegame[19]
                hero.lvl = savegame[20]
                hero.mbti = savegame[21]
                hero.weapon = pizzitems.weapon_list[equipped[0]]
                hero.head = pizzitems.armor_list[equipped[1]]
                hero.body = pizzitems.armor_list[equipped[2]]
                hero.legs = pizzitems.armor_list[equipped[3]]
                hero.accs = pizzitems.armor_list[equipped[4]]
                hero.location = "town"
                hero.inv[0] = pizzitems.inv_list[inv[0]]
                hero.inv[1] = pizzitems.inv_list[inv[1]]
                hero.inv[2] = pizzitems.inv_list[inv[2]]
                hero.inv[3] = pizzitems.inv_list[inv[3]]
                hero.inv[4] = pizzitems.inv_list[inv[4]]
                hero.inv[5] = pizzitems.inv_list[inv[5]]
                hero.inv[6] = pizzitems.inv_list[inv[6]]
                hero.inv[7] = pizzitems.inv_list[inv[7]]
                hero.inv[8] = pizzitems.inv_list[inv[8]]
                hero.inv[9] = pizzitems.inv_list[inv[9]]
                hero.inv[10] = pizzitems.inv_list[inv[10]]
                hero.inv[11] = pizzitems.inv_list[inv[11]]
                hero.inv[12] = pizzitems.inv_list[inv[12]]
                hero.inv[13] = pizzitems.inv_list[inv[13]]
                hero.inv[14] = pizzitems.inv_list[inv[14]]
                hero.inv[15] = pizzitems.inv_list[inv[15]]
                hero.spells[0] = pizzspells.spell_list[spells[0]]
                hero.spells[1] = pizzspells.spell_list[spells[1]]
                hero.spells[2] = pizzspells.spell_list[spells[2]]
                hero.spells[3] = pizzspells.spell_list[spells[3]]
                hero.spells[4] = pizzspells.spell_list[spells[4]]
                hero.spells[5] = pizzspells.spell_list[spells[5]]
                hero.spells[6] = pizzspells.spell_list[spells[6]]
                hero.spells[7] = pizzspells.spell_list[spells[7]]
                hero.spells[8] = pizzspells.spell_list[spells[8]]
                hero.spells[9] = pizzspells.spell_list[spells[9]]
                hero.spells[10] = pizzspells.spell_list[spells[10]]
                hero.spells[11] = pizzspells.spell_list[spells[11]]
                print "Save game load successful."
                raw_input()
                return True
            except ImportError:
                print "Error loading save file!"
                raw_input()
                comm_key = 0
        else:
            print "No such save file exists!"
            raw_input()
            comm_key = 0


def quit_game():
    quitting = 0
    while quitting != "y" or quitting != "n":
        print " "
        print "Are you sure you want to quit playing?"
        print "Y or N"
        quitting = raw_input().lower()
        if quitting:
            os.system('cls')
            print "Thanks for playing Pizza Lady's RPG."
            print "<( )Bai2u"
            exit()
        else:
            quitting = "n"
            return quitting


def town(hero):
    if hero.saved:
        try:
            reload(pizzsave)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            pass
        try:
            reload(pizzsave2)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            pass
        try:
            reload(pizzsave3)
        except (ImportError, IndexError, AttributeError, SyntaxError, NameError):
            pass
        hero.saved = False
    hero.location = "town"
    town_options = {"1": "inn", "2": "armory", "3": "g_store", "i": "inventory", "t": "stats",
                    "e": "equipment", "s": "save_game", "l": "load_game", "q": "quit_game", "0": "dungeon"}
    location = town
    hero.stats_total()
    while location not in town_options:
        os.system('cls')
        print "Central Point"
        print "----------------------------"
        print "%s - Level %s  %s" % (hero.name, hero.lvl, hero.mbti)
        print " "
        print "(1) Inn             (2) Forge"
        print "(3) Armory          (4) General Store"
        print "(0) Dungeon"
        print " "
        print "(I) Inventory       (M) Spells"
        print "(T) Stats           (E) Equipment"
        print " "
        print "(S) Save Game       (L) Load Game"
        print "(Q) Quit Game"
        print " "
        if hero.bad_key:
            print "Invalid command, %s, try again." % hero.name
        else:
            print "We await your command, %s." % hero.name
        location = raw_input().lower()
        if location in town_options:
            hero.bad_key = False
        print "\n" * 3
        if location == "1":
            inn(hero)
        elif location == "2":
            forge(hero)
        elif location == "3":
            armory(hero)
        elif location == "4":
            g_store(hero)
        elif location == "i":
            inventory(hero)
        elif location == "t":
            stats(hero)
        elif location == "e":
            equipment(hero)
        elif location == "s":
            save_game(hero)
        elif location == "m":
            sp_choice = 0
            while sp_choice != "Cancelled":
                sp_choice = hero.spell()
                if sp_choice != "Cancelled":
                    if not hero.spells[sp_choice - 1].healing:
                        print "There's no need to cast that outside battle!"
                    else:
                        damage = int(pizzspells.spell_effects(hero, 0, 0, 0, "hero", "self", sp_choice))
                        print "You heal yourself for %s HP!" % damage
                        hero.hp += damage
                        if hero.hp > hero.hp_ttl:
                            hero.hp = hero.hp_ttl
                    raw_input()
        elif location == "l":
            load_game(hero)
        elif location == "0":
            dungeon(hero)
        elif location == "q":
            quit_game()
        else:
            hero.bad_key = True
