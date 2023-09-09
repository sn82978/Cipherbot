import discord
from discord.ext import commands
from discord import app_commands
import random
from collections import Counter
import re
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
#setting up the bot
TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
botDescription="Bot"
bot = commands.Bot(command_prefix="c.", help_command=None, description=botDescription, intents=intents)

#functions for the bot
plaintext_quotes = ["Any bug can be a bedbug, just tuck it in", 
                    "I know fish don't like mathematics, because they can't perform basic calculations based on the last time I asked one to",
                   "Hey, you look like the kind of girl who catches and eats invasive beetles",
                   "I retain childlike characteristics because I hang out with you kids all the time",
                   "All sixteen year olds know are taxes, insurace, meal prep, and taxes",
                   "Oh to have a wife nagging you to stop looking at bugs",
                   "At some point someone is going to do barcoding and define sminthurididae just to mess with us",
                   "I got banned from a ski resort for dipping my nuts in the soda dispenser",
                   "If it wasn't a strange mix of deeply personal health and drama discussions mixed in with a roleplaying scenario involving sentient, tyrannical bees in the pharmaceautical industry, it wouldn't be my group chat",
                "A maggot is a pill that you can chew", 
                "The worst kind of cow tipping is on wild cows. Wild cows are hard to find, however are wildly unpredictable. You never know what a wild cow's defenses are",
                   "We don't live where we did when you left.  Your dad read in the paper where most accidents happened within twenty miles of home, so we moved", 
                   "We got a bill from the funeral home. Said if we didn't make the last payment on grandma's funeral bill, up she comes", 
                   "Your Uncle John fell in the whiskey vat.  Some men tried to pull him out, but he fought them off playfully, so he drowned.  We cremated him and he burned for four days", 
                   "Your father has a lovely new job.  He has over 500 men under him.  He's cutting grass at the local cemetary", 
                   "I'd love to, but I'm converting my calendar watch from julian to gregorian", 
                   "Nearly one in three American adults queried by the national science foundation said the sun revolves around the earth", 
                   "A gerbil was elected president of the student union at the university of east anglia in england", 
                   "You have an inventive mind and are inclined to be progressive", 
                   "When was the last time you were in a shopping mall and observed a human foaming at the mouth, eating his shirt, and using a solar flashlight", 
                   "Its vacant stare and wideeyed smile seemed to sneer up at him", 
                   "I'm writing this slow 'cause i know that you can't read fast", "We don't live where we did when you left", 'Your dad read in the paper that most accidents happened within twenty miles of home, so we moved', 'This place has a washing machine', 'It only rained twice this week, three days the first time, and four days the second time', 
                   'The coat you wanted me to send to you, your aunt sue said it would be a little too heavy to send in the mail with them heavy buttons, so we cut them off and put them into the pockets',
                    'Your uncle john fell in the whiskey vat', 
                    'Some men tried to pull him out, but he fought them off playfully, so he drowned', 
                    'We cremated him, he burned three days', 
                    'Three of your friends went off the bridge in a pickup', 
                    'The other two were in the back', 'The driver got out', 'He rolled down the window and swam to safety', "They couldn't get the tail gate down", 
                    'Not much more news this time, nothing much has really happened'
                    'Lasers are used for many different applications in society today, such as measuring distances, detecting structural flaws, determining straightness, and so forth', 
                    'That receipt information is stored in a central computer, which keeps inventory and indicates what products the store should order, as well as which products should no longer be carried', 
                    'In fact, in fresno, california, one of eight regional test cities, a new computer system called behavior scan gives shoppers a bar code card that is read at each purchase', 
                    'While most customers claim that they are not affected by these commercials, the advertising companies have spent a lot of money on research proving otherwise', 'Thanks to computers, paychecks are deposited automatically into checking and savings accounts at predefined rates while many bills and loans are automatically paid on time every month', 
                    'No longer does it merely tell time; it also can add and subtract, keep time in three different zones, give the day and the date, and beep at predetermined intervals', 
                    "The card allows direct payment to the seller by instantaneously deducting the purchase amount and any service charges directly from the cardholder's account", 
                    'Thus, not only is the seller paid immediately but, also, the card companies save millions of dollars by eliminating bad payments and personal bankruptcy debts', 
                    'The concern is that we are reaching a highly automated state, which if followed to the next logical step might have profound impacts on how we rate life',
                    "That chip will include not only the person's identification number, social security number, name and birthplace, but also his criminal background, educational level financial worth in the community, and his political affiliations", 
                    'With such a system, the minute someone walked through the door of the bank, he would be sensed and the bank would know who he was, where he came from, what he did, and how much he was worth', 
                    'There had been discussions about placing codes on the hand to be used as identification marks, like fingerprints, similar to package bar codes in supermarkets', 
                    'They would like to control everything, even the areas they say they do not want to control, such as business, transportation, education, religion, entertainment, and other governments', 
                    "If this sounds the least bit exaggerated just look at our government's actions regarding the restrictions of business concerning tax credit, labor laws, advertising, antitrust, and corporate subsidies",
                    'Even in deregulation, transportation requires licensing, registration, inspection, subsidies, price controls, flight approval, and government flight controllers', 
                    'Although there may be talk of eliminating the federal department of education there is no attempt to reduce control of school curriculum, subsidies, and even school lunches', 
                    'The federal government also seeks to control other governments by rewarding or threatening them with trade concessions, military or econonic aid, sanctions, or war', 
                    'In reality, government may take over, not through control of transportation and censorship, but through the economy, the lending institutions, and every financial transaction', 
                    'The central computer for america is in texas, and the international computer that ties all the national central computers together is situated in brussels, belgium', 
                    'This immense computer has enough capacity to store every detail about the lives of every human being on earth, the information contained in the library of congress, and every book ever printed', 
                    "This number also represents the universal consistency of the computers that will be required to control the world's finances and thus the world's people",
                   'The scene is of a soviet military installation on the kola peninsula in the icy barents sea, a place usually off limits to the gaze of the western world', "Using the latest bathymetric technology and state of the art systems known as seam beam and hydrochart, researchers are for the first time assembling detailed underwater maps of the continental shelves and the depths of the world's oceans", 
                   "That attitude has outraged those concerned with the military's increasing efforts to keep information not only from the public but from industry experts, scientists, and even other government officials as well", 
                   'Zero defense department officials have attempted to rewrite key laws that spell out when the president can and cannot appropriate private communications facilities', 
                   'Latham now heads an interagency committee in charge of writing and implementing many of the policies that have put the military in charge of the flow of civilian information and communication', 
                   'And last october the steering group issued a memorandum that defined sensitive information and gave federal agencies broad new powers to keep it from the public', 
                   "When asked how the government's new definition of sensitive information will be used, he defends the necessity for it and tries to put to rest concerns about a new restrictiveness", 
                   'It purged all unclassified government supplied technical data from its system and completely dropped the national technical information system from its database rather than risk a confrontation', 
                   "Representative jack brooks, a texas democrat who chairs the house government operations committee, is an outspoken critic of the nsa's role in restricting civilian information", 
                   'The policy does not directly affect the data over satellite channels, but it does make the nsa privy to vital information about the essential signals needed to operate a satellite', 
                   'Latham insists this, too, is a voluntary procedure and that only companies that wish to install protection will have their systems evaluated by the nsa', 
                   "With just a few thousand dollars' worth of equipment, a disgruntled employee could interfere with a satellite's control signals and disable or even wipe out a hundred million dollar satellite carrying government information", 
                   'Since president reagan took office, the pentagon has stepped up its efforts to rewrite the definition of national emergency and give the military expanded powers in the united states', 
                   "Should the pentagon ever be given the green light, its base for taking over the nation's communications system would be a nondescript yellow brick building within the maze of high rises, government buildings, and apartment complexes that make up the washington suburb of arlington, virginia", 
                   'If war breaks out and communications to a key military base are cut, the pentagon wants to make sure that an alternate link can be set up as fast as possible', 'Defense secretary weinberger personally urged the attorney general to block the lawsuit that resulted in the breakup, as had his predecessor, harold brown', 
                   'Now the brass had to contend with several competing companies to acquire phone lines, and communications was more than a matter of running a line from one telephone to another', 'Satellites, microwave towers, fiberoptics, and other technological breakthroughs never dreamed of by alexander graham bell were in extensive use, and not just for phone conversations', 
                   'According to navy curtis craft deputy director william belford, no physical sites have yet been chosen for a substitute navy curtis craft, and even whether the navy curtis craft itself will survive a nuclear attack is still under study', 
                   "The answer appears to be that because of the pentagon's concerns about the at&t divestiture and the disruptive effects it might have on national security, the navy curtis craft was to serve as the military's peacetime communications center", 
                   'While the report notes that current technical differences such as varying frequencies make it difficult for the pentagon to use commercial satellites, it recommends ways to resolve those problems', 
                   'The pentagon now has an unprecedented access to the civilian communications network: commercial databases, computer networks, electronic links, telephone lines', 
                   'Government officials have offered all kinds of scenarios to justify the navy curtis craft, the satellite survivability report, new domains of authority for the pentagon and the nsa, and the creation of top level government steering groups to think of even more policies for the military', 
                   "That may change sometime this year, when the office of technology assessment issues a report on how the pentagon's policy will affect communications in the united states", 'While it seems unlikely that the pentagon will ever get total control of our information and communications systems, the truth is that it can happen all too easily',
                   "This idea one must know how  to apply whenever it apperars necessary with this bait  of an idea to attract the masses of the pople to  one's party for the purpose of crushing another who  is in authority", 
                   'It  is precisely here that the triumph of our theory  appears; the slackened riens of government are  immediately, by the law of life, caught up and  gathered together by a new hand, because the blind  might of the nation cannot for one single day exist without guidance, and the new authority merely fits  into the placeof the ofd already weakened by livberalism', 
                   'The part played by the press is to keep ponting our requiremnets supposed to be indispensable, to give voice to the complaints  of the people, to express and th create discontent'
                   'Most loans are made to member governments, but if a member will guarantee repayment, loans can be arranged for private firms', 
                   'The technical assistance program of the bank works in two ways: it helps set up a project that may secure a loan, and it then aids recipients in utilizing the loan when it is granted'
                   ]

def aristo_encoder(pt):
    import random
    from collections import Counter

    split_pt = list(pt)
    length = int(len(split_pt) - 1)
    split_char_pt = split_pt[:]
    for i in range(len(split_pt)):
        if split_pt[i].isalpha():
            split_pt[i] = ord(split_pt[i].lower())-97

    duplicates = [number for number in split_pt if (split_pt.count(number) > 1 or split_pt.count(number) == 1) and str(number).isdigit()]
    unique_pt_chars = list(set(duplicates))

    ct_numbers = random.sample(range(26), len(unique_pt_chars))
    for j in range(len(split_pt)):
        if str(split_pt[j]).isdigit():
            split_pt[j] = chr(ct_numbers[unique_pt_chars.index(split_pt[j])]+97).upper()
    return ''.join(str(i) for i in split_pt)

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def random_plaintext():
    plaintext = plaintext_quotes[random.randrange(len(plaintext_quotes))]
    return plaintext

cipher = ''
plaintext = ''

#slash commands for the bot
@tree.command(name = "aristocrat", description = "Gives you an aristocrat", guild=discord.Object(id=ID_HERE))
async def first_command(interaction):
    global plaintext
    plaintext = random_plaintext()
    global cipher
    cipher = aristo_encoder(plaintext)
    await interaction.response.send_message(cipher)

@tree.command(name = 'answer', description = "Tells you the entire plaintext", guild=discord.Object(id=ID_HERE))
async def answer(interaction):
    await interaction.response.send_message(plaintext)

@tree.command(name = 'hint', description = "Tells you the first plaintext character of the cipher", guild=discord.Object(id=ID_HERE))
async def hint(interaction):
    await interaction.response.send_message(plaintext[0])

@tree.command(name = 'help', description = "States possible commands and syntax to get plaintext checked", guild=discord.Object(id=ID_HERE))
async def help(interaction):
    await interaction.response.send_message("Do /answer to see the answer and if you're right \n\nIMPORTANT: The aristocrat displayed may have letters that map onto each other. EX) Plaintext C might be ciphertext C.")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=ID_HERE))
    print("Ready!")

client.run(TOKEN)