import os
import pizzbatt
import pizzspells


def dungeon_crawl(hero, selection):
    in_dungeon = True
    at_entrance = True
    area1 = True
    area2 = False
    area3 = False
    area4 = False
    area5 = False
    area_end = False
    dun_num = selection
    while in_dungeon:
        while at_entrance:
            os.system('cls')
            if dun_num == 1:
                if area1:
                    print "You are standing at the candy caned path leading into a sweet, but dangerous"
                    print "place."
                elif area2:
                    print "You are further along in the valley. The path has started to fade and ahead"
                    print "is a sugar cane forest."
                elif area3:
                    print "You are in the sugar cane forest. Stalks of sugar cane and a river made of"
                    print "corn syrup surrounds you."
                elif area4:
                    print "You have exited the forest and are standing at the top of a downhill slope."
                    print "The jelly pink sky is starting to turn a dark magenta."
                else:
                    print "You are at the bottom of the hill, the sky is now a dark purple. Something"
                    print "is glowing in a wide hole a distance away."
            elif dun_num == 2:
                if area1:
                    print "You are standing at the bottom of a mountain, that looks more like a giant hill."
                elif area2:
                    print "You scale the mountain hill, and soon stop to rest in a small cave opening."
                elif area3:
                    print "You have gotten further up, and the air is getting foggy. You are getting quite"
                    print "high up."
                elif area4:
                    print "You are at the peak, where another cave greets you. You hear rumbling sounds"
                    print "echoing from within."
                else:
                    print "You are descending down the cave and hear the rumbling grow louder. There is"
                    print "something lurking here."
            elif dun_num == 3:
                if area1:
                    print "You stand at the entrance hall of Tipping Complex. It smells pungent and moldy."
                elif area2:
                    print "You've ventured further into the building. You're not quite sure where you are,"
                    print "But there isn't much lighting and you see many boarded up doors around."
                elif area3:
                    print "You are deep into the complex, and sure you're venturing downstairs. There are"
                    print "strange sounds echoing around you."
                elif area4:
                    print "There isn't much light, and you're sure you're underground now. The complex"
                    print "walls are now concrete, and the strange sounds are getting louder."
                else:
                    print "There is a long hallway leading to a single metal door. You're not sure what"
                    print "lurks behind it, but you have a bad feeling about this.."
            print "What will you do?"
            print " "
            print "(1) Go Further    (2) Look"
            print "(3) Items         (4) Spells"
            print "(5) Status        (6) Equipment"
            print " "
            print "(R) Retreat"
            if hero.bad_key:
                print "I don't understand."
            command = raw_input().lower()
            if command in ("1", "2", "3", "4", "5", "6", "r"):
                hero.bad_key = False
            if command == "1":
                hero.in_battle = True
                if dun_num == 1:
                    if area1:
                        print "You venture further down the sugar coated path and encounter enemies!"
                    elif area2:
                        print "As you near the sugar cane forest, enemies come out and attack!"
                    elif area3:
                        print "In the reflection of the corn syrup river, you see enemies nearing!"
                    elif area4:
                        print "As you near the downhill slope, you are attacked by monsters!"
                    else:
                        print "From the hole rises a giant star candy, intent on crushing you!"
                elif dun_num == 2:
                    if area1:
                        print "As you make your way up the mountain, you are ambushed by enemies!"
                    if area2:
                        print "Shadows began to form against the cave background - monsters!"
                    if area3:
                        print "From the clouds you see dark forms - enemies are coming!"
                    if area4:
                        print "Enemies ambush you as you near the entrance. Watch out!"
                    if area5:
                        print "A giant drill monstrosity of some kind rises. Get ready to fight!"
                elif dun_num == 3:
                    if area1:
                        print "Passing by a closed door, it suddenly opens and enemies attack!"
                    if area2:
                        print "There is some shaking, and from the ceiling, out tumbles enemies!"
                    if area3:
                        print "The darkness and sounds prevent you from seeing what's in the shadow!"
                    if area4:
                        print "From ahead, enemies begin to charge you. You prepare to fight!"
                    if area5:
                        print "You open the door to find an abomination formed with the walls!!"
                raw_input()
                victory = pizzbatt.fight_battle(hero, dun_num - 1, area5)
                if victory is True:
                    if dun_num == 1:
                        if area1:
                            print "Dusting some crushed confections off, you head further down the sugared road."
                            area1 = False
                            area2 = True
                        elif area2:
                            print "The enemies defeated, you venture inward to the sugar cane forest."
                            area2 = False
                            area3 = True
                        elif area3:
                            print "You leave the forest, and begin to survey your changed surroundings."
                            area3 = False
                            area4 = True
                        elif area4:
                            print "You carefully make your way downhill."
                            area4 = False
                            area5 = True
                        else:
                            print "The star bursts into hundreds of little sugar bits. You have won!"
                            area5 = False
                            area_end = True
                    elif dun_num == 2:
                        if area1:
                            print "As the enemies tumble downward, you continue upward."
                            area1 = False
                            area2 = True
                        elif area2:
                            print "You defeat the monsters and continue up the mountain hill."
                            area2 = False
                            area3 = True
                        elif area3:
                            print "The enemies disappear from sight as they fall, and you go onward."
                            area3 = False
                            area4 = True
                        elif area4:
                            print "You continue on into the dark cave, hearing something strange within."
                            area4 = False
                            area5 = True
                        else:
                            print "The drilling monster defeated, you start to head back out, victorious!"
                            area5 = False
                            area_end = True
                    elif dun_num == 3:
                        if area1:
                            print "You continue down the hall after toppling the enemies."
                            area1 = False
                            area2 = True
                        elif area2:
                            print "Dusting yourself off, you continue through the twisting halls."
                            area2 = False
                            area3 = True
                        elif area3:
                            print "You continue onward, uneasy and unsure of what awaits you."
                            area3 = False
                            area4 = True
                        elif area4:
                            print "Ahead, you see what appears to be a bit of light... what awaits you?"
                            area4 = False
                            area5 = True
                        else:
                            print "The monster is defeated! Finally, you can make your way out of here!"
                            area5 = False
                            area_end = True
                    raw_input()
                    if area_end:
                        return
                elif victory == "dead":
                    return
                else:
                    return
            elif command == "2":
                if dun_num == 1:
                    print "You look around and see that Uncandy Valley is nothing but sugar as far as the"
                    print "eye can see. So many sweet treats, that it's tempting to just indulge your"
                    print "sweet tooth. However, you decide it's best to not let yourself lose control in"
                    print "this tasty place."
                elif dun_num == 2:
                    print "Whoever said Molehill Mountain isn't as dangerous as it seems is right. It"
                    print "isn't as threatening as people make it out to be. But, could it also be"
                    print "that it's deadly but people make it seem relatively safe?"
                elif dun_num == 3:
                    print "The halls of Tipping Complex are worn-down, the wallpaper crumbling away with"
                    print "strange sounds echoing throughout. You're not sure who - or what lives here,"
                    print "but you want to get through and get out as fast as you can. It feels like"
                    print "someone is watching you."
                raw_input()
            elif command == "3":
                hero.inventory_sys(False)
            elif command == "4":
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
            elif command == "5":
                from pizztown import stats
                stats(hero)
            elif command == "6":
                from pizztown import equipment
                equipment(hero)
            elif command == "r":
                if dun_num == 1:
                    print "You retreat in fear of the integrity of your teeth!"
                elif dun_num == 2:
                    print "You retreat, trying not to trip like a bumbler tumbler!"
                elif dun_num == 3:
                    print "You retreat from the twisting halls as fast as you can!"
                else:
                    pass
                raw_input()
                hero.location = "dungeon"
                return
            else:
                hero.bad_key = True


def dungeon(hero):
    hero.location = "dungeon"
    dungeons = ("1", "2", "3")
    selection = "loop"
    while selection not in dungeons:
        os.system('cls')
        print "Town Outskirts"
        print "----------------------------------------------------"
        print "\n"
        print "Where would you like to go?"
        print " "
        print "(1) Uncandy Valley"
        print "(2) Molehill Mountain"
        print "(3) Tipping Complex"
        print "(B) Return to Town"
        print " "
        if hero.bad_key:
            print "I don't know where that is."
        selection = raw_input().lower()
        print "\n"
        if selection in dungeons:
            hero.bad_key = False
            if selection == "1":
                print "You follow the sweet scented trail to Uncandy Valley."
            elif selection == "2":
                print "You take exaggerated steps towards Molehill Mountain."
            elif selection == "3":
                print "You enter the twisting dark halls of Tipping Complex."
            raw_input()
            dungeon_crawl(hero, int(selection))
        elif selection == "b":
            hero.location = "town"
            return
        else:
            selection = "loop"
            hero.bad_key = True
