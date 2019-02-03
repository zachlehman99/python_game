from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Floor_55_Start(Scene):

    def enter(self):
        print(dedent("""
            Your name is John and you are in the wrong place at the wrong time. Some stuff is going down and you are now in the middle of it. You over hear someone is going to steal a decent amount of bearer bonds over 600 million dollars...Who ever thought bearer bonds were a great idea...It is a stupid idea, but that is beside the point.

            You have to get the detonator before it is to late and you spend your life dead instead of being alive. You also have no weapons at all through this game, the only thing you can use is your fists and feet for your fighting pleasures...maybe you can find a gun somewhere. You are on the 55th floor of a 77 story building. Do you go up the stairs, down the stairs, up the elevator or down the elevator?
            """))

        insert = input("-> ")

        if insert == "down the stairs":
            print(dedent("""
                You are walking down the stairs and you have some weight on you so you can't walk all 55 flights of stairs. You go 11 stories and now you are on the 44th floor to take a break from all of the freaking walking you had to do. You picked the wrong floor to stop on...
                """))
            return 'floor_44'

        elif insert == "up the stairs":
            print(dedent("""
                You are going up and up and up until you get to the 66th floor, you are tired and somewhat scared that something bad is going to happen to you at this point. You go to this big room with tons of glass walls and you basically can see everything. You see this man staring at you across the way with a big ass gun...
                """))
            return 'floor_66'

        elif insert == "down the elevator":
            #Something to connect the death file
            return 'death'

        elif insert == "up the elevator":
            #Something to connect the death file
            return 'death'

        else:
            print("I have no idea what you said please say it louder or type it better?")
            return 'floor_55'


class Floor_66(Scene):

    def enter(self):
        print(dedent("""
            What exactly should you do at this moment...run up the stairs, run down the stairs or try and fight him?
            """))

        insert = input("-> ")

        if insert == "run up the stairs":
            print(dedent("""
                You ran up the stairs and kept going until you got to the top, A man by the name of Hans Gruber is up there and he has nothing of it. He wants to kick your ass...He shoots you multiple times, and if that is not bad enough he stares at you in you death state and kicks you off the building.
                """))
            return 'floor_77'

        elif insert == "run down the stairs":
            return 'floor_55'

        elif insert == "try and fight":
            #Something to connect the death file
            return 'death'
        else:
            print("I have no idea what you said please say it louder or type it better?")
            return 'floor_66'

class Floor_77(Scene):

    def enter(self):
        print(dedent("""
            You Badly lose!!!! And Died Badly!!!!
            """))
        return 'exit'

class Floor_44(Scene):

    def enter(self):
        print(dedent("""
            You just ran in to some tall, weird blonde hair guy. He looks like he has some sort of machine or pack on him and he has a gun and is ready to protect himself when he has too. You are a cop and you do have some skills in fighting. What should you do in this situation?
            """))

        insert = input('-> ')

        if insert = 'fight':
            print(dedent("""
                You just did what you had to do. He spotted you and he went free will of firing at you. But he was dumb and missed everything and he emptied his clip and it went to an all out brawl. He punched you right in the nose and you were bleeding fiercely...

                This was the breaking point for you. You went into 'Johnzilla' mode and kicked his ass, this fight went down flights of stairs, by the end of it you were on the 33rd floor. And you knocked him out and the problem was he had the thing around his neck, so it must be important, so you took it. And went to get his gun to but it is empty and pointless. You look at the device from the guys neck and the gun just in case.
                """))
            return 'floor_33'

        elif insert = 'run':
            #Something to connect the death file
            return 'death'

        else:
            print("I have no idea what you said please say it louder or type it better?")
            return 'floor_44'


class Floor_33(Scene):
    pass

class Floor_22(Scene):
    pass

class Floor_11(Scene):
    pass

class Floor_0(Scene):
    pass

class Engine(object):
    pass

class Map(object):
    pass
