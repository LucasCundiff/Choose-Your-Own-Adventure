class Scene:
    choice_text = ""
    next_options = []
    entry_text = ""
    is_ending = False

    def __init__(self, choice, options, entry, ending=False):
        self.choice_text = choice
        self.next_options = options
        self.entry_text = entry
        self.is_ending = ending


current_scene = Scene("", {}, "")


def create_scenes():
    seek_guidance = Scene(
        "Seek Guidance for a Heroic Quest",
        [

        ],
        """The Mystic Oracle reveals a noble quest that could bring honor and fortune. 
         
The Mystic Oracle reveals a great quest to retrieve a legendary artifact known as the "Sword of Eternal Light."
You embark on an epic adventure, facing treacherous dungeons and powerful adversaries.

Fame and Fortune: After overcoming numerous challenges, you successfully retrieve the Sword of Eternal Light.
The world recognizes your valor, and tales of your heroic deeds spread far and wide.
         """,
        True
    )

    unlock_powers = Scene(
        "Unlock Hidden Mystical Powers",
        [

        ],
        """You implore the Mystic Oracle to unlock your hidden potential and grant you mystical abilities. 
         
The Mystic Oracle unlocks your latent magical abilities, but warns you of the price you must pay. Though you 
gain immense power, your insatiable thirst for more leads you down a dark path.

Grim Death: The unchecked pursuit of power leads to your own downfall as you are consumed by the very magic 
you sought to control.""",
        True
    )

    visit_oracle = Scene(
        "Visit the Mystic Oracle",
        [
            seek_guidance,
            unlock_powers
        ],
        """Intrigued by the tales of the Mystic Oracle, you set out to seek her guidance.
        
You journey to find the Mystic Oracle, hoping to uncover secrets and prophecies 
that will shape your future."""
    )

    embrace_magic = Scene(
        "Embrace the Forest's Magic",
        [

        ],
        """You succumb to the allure of power, using the magical artifacts to enhance your abilities.

By embracing the magical artifacts, you gain incredible power. However, the dark forces within the Forbidden Woods
corrupt you, turning you into a twisted figure of darkness.

Grim Death: Consumed by the malevolent energy, you become a terror that haunts the land, feared 
by all until a group of courageous adventurers finally defeats you.""",
        True
    )

    resist_temptation = Scene(
        "Resist Temptations and Honor Your Code",
        [

        ],
        """You stay true to your knightly code, resist temptations, and tread carefully through the woods.
        
Your unwavering determination and sense of righteousness help you navigate the dangers of the Forbidden Woods.
You encounter a wise hermit who gifts you a sacred sword blessed by the forest's spirits.

Fame and Fortune: With the newfound weapon and the knowledge gained from the hermit, you return to Aralia
as a legendary knight, revered by the people for your bravery and self-discipline.""",
        True
    )

    explore_woods = Scene(
        "Explore the Forbidden Woods",
        [
            resist_temptation,
            embrace_magic
        ],
        """Feeling restless, you decide to explore the mysterious Forbidden Woods. 
        
As you venture into the Forbidden Woods, you encounter mystical creatures and challenging obstacles.
You face temptations to take shortcuts or indulge in power bestowed by the forest's magical artifacts."""
    )
    assemble_warriors = Scene(
        "Assemble a Renowned Team of Warriors",
        [

        ],
        """Deciding that might is what's needed, you recruit a band of skilled warriors.
        
Your band of skilled warriors proves to be a formidable force. With your tactical prowess and their unmatched combat
abilities, you successfully defend Aralia from Drakoria's invasion. However, during the final battle, you face 
a fearsome dragon, and tragically, not all members of your team make it out alive.

Grim Death: While you emerge victorious, the loss of your comrades weighs heavily on your heart, and you
carry the burden of their sacrifice throughout your life.
        """,
        True
    )

    embark_mission = Scene(
        "Embark on a Diplomatic Mission",
        [

        ],
        """You choose the path of diplomacy and set off to negotiate alliances with neighboring realms.
        
You successfully forge alliances with several neighboring kingdoms. As the armies gather at Aralia's borders,
you lead them to victory against the invading forces of Drakoria. Your wisdom and diplomacy earn you admiration
from your fellow knights, nobles, and the people. Your name becomes synonymous with peace and cooperation.

Fame and Fortune: You are hailed as the "Peacemaker Knight" and become a celebrated diplomat, rising to the ranks
of the king's most trusted advisors.""",
        True
    )

    follow_orders = Scene(
        "Follow the King's Orders",
        [
            embark_mission,
            assemble_warriors
        ],
        """You decide to obey the king's orders and head to the throne room.
        
The king informs you of a dire situation - the neighboring kingdom of Drakoria is amassing an army
to invade Aralia. He entrusts you with a crucial mission: to gather allies from other realms and defend
your kingdom from the impending threat."""
    )

    start = Scene(
        "",
        [
            follow_orders,
            explore_woods,
            visit_oracle
        ],
        """You are Sir Cedric, a valiant knight from the Kingdom of Aralia. As a skilled and honorable warrior,
you have sworn to protect your realm and its people from all threats. One fateful morning,
the king summons you to his throne room."""
    )

    global current_scene
    current_scene = start


def run_game():
    global current_scene
    chapter = 1
    while True:
        print("--------------------------------------------------------------------------------------------------")
        print(f"                                      Chapter {chapter}                                                  ")
        print(current_scene.entry_text)
        if current_scene.is_ending:
            break
        index = 0
        for x in current_scene.next_options:
            print(f"{index + 1}. {x.choice_text}")
            index += 1

        chapter += 1

        while True:
            player_choice = input("What is your choice? ")
            try:
                int_choice = int(player_choice) - 1
            except ValueError:
                "Please try again using the number index displayed before the choice"
            except TypeError:
                "Please try again using the number index displayed before the choice"
            else:
                if -1 < int_choice < index:
                    current_scene = current_scene.next_options[int_choice]
                    break
                else:
                    "Please try again using the number index displayed before the choice"

    print("--------------------------------------------------------------------------------------------------")
    print("The end. Thanks for playing!")
    pause = input()


def main():
    create_scenes()
    run_game()


main()
