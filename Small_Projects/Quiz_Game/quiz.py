import random
import time
questions = [
    {
        "question": "What is the best-selling PC game of all time?",
        "options": ["A. GTA V", "B. Minecraft", "C. Fortnite", "D. CS:GO"],
        "answer": "B"
    },
    {
        "question": "Which car brand makes the Supra?",
        "options": ["A. Nissan", "B. Honda", "C. Toyota", "D. Mazda"],
        "answer": "C"
    },
    {
        "question": "What caliber does an AK-47 use?",
        "options": ["A. 9mm", "B. 5.56mm", "C. 7.62mm", "D. .45 ACP"],
        "answer": "C"
    },
    {
        "question": "Which movie features the character John Wick?",
        "options": ["A. Taken", "B. John Wick", "C. The Matrix", "D. Heat"],
        "answer": "B"
    },
    {
        "question": "In GTA V, what city is the game set in?",
        "options": ["A. Vice City", "B. Liberty City", "C. Los Santos", "D. San Fierro"],
        "answer": "C"
    },
    {
        "question": "Which PC game features the fictional city of 'Night City'?",
        "options": ["A. Watch Dogs", "B. Cyberpunk 2077", "C. Fallout 4", "D. Deus Ex"],
        "answer": "B"
    },
    {
        "question": "Which platform is the largest digital store for PC gaming?",
        "options": ["A. Epic Games", "B. Origin", "C. Steam", "D. Uplay"],
        "answer": "C"
    },
    {
        "question": "What is the main objective in the game 'Left 4 Dead'?",
        "options": ["A. Racing", "B. Surviving Zombies", "C. Building Cities", "D. Solving Puzzles"],
        "answer": "B"
    },
    {
        "question": "What type of weapon is the famous M4A1?",
        "options": ["A. Sniper Rifle", "B. Shotgun", "C. Assault Rifle", "D. Submachine Gun"],
        "answer": "C"
    },
    {
        "question": "Which pistol is famous for having a polymer frame and no manual safety switch?",
        "options": ["A. Colt M1911", "B. Glock 17", "C. Beretta 92FS", "D. Desert Eagle"],
        "answer": "B"
    },
    {
        "question": "In 'Breaking Bad', what is Walter White's drug lord pseudonym?",
        "options": ["A. Heisenberg", "B. Cap'n Cook", "C. Tuco", "D. Gus"],
        "answer": "A"
    },
    {
        "question": "Which popular Netflix series features characters named Eleven, Mike, and Dustin?",
        "options": ["A. Dark", "B. Stranger Things", "C. The Witcher", "D. Wednesday"],
        "answer": "B"
    },
    {
        "question": "In Christopher Nolan's 'The Dark Knight', who played the role of The Joker?",
        "options": ["A. Joaquin Phoenix", "B. Jared Leto", "C. Heath Ledger", "D. Jack Nicholson"],
        "answer": "C"
    },
    {
        "question": "Who is the iconic British Special Forces operative with the skull mask in Call of Duty?",
        "options": ["A. Captain Price", "B. Soap MacTavish", "C. Ghost", "D. Gaz"],
        "answer": "C"
    },
    {
        "question": "Which sub-series of Call of Duty features the famous 'Zombies' mode created by Treyarch?",
        "options": ["A. Modern Warfare", "B. Black Ops", "C. Vanguard", "D. Ghosts"],
        "answer": "B"
    },
    {
        "question": "Which battle is widely considered the major turning point of World War II in Europe?",
        "options": ["A. Battle of Stalingrad", "B. Battle of Britain", "C. Battle of Midway", "D. Battle of the Bulge"],
        "answer": "A"
    },
    {
        "question": "What was the code name for the historic Allied invasion of Normandy during World War II?",
        "options": ["A. Operation Barbarossa", "B. Operation Desert Storm", "C. Operation Overlord (D-Day)", "D. Operation Valkyrie"],
        "answer": "C"
    },
    {
        "question": "Which iconic submachine gun was heavily used by gangsters and US troops in World War II?",
        "options": ["A. MP40", "B. Thompson (Tommy Gun)", "C. Uzi", "D. P90"],
        "answer": "B"
    },
    {
        "question": "What is the standard sniper rifle caliber often used for long-range military engagements?",
        "options": ["A. .50 BMG", "B. 9mm", "C. .22 LR", "D. 12 Gauge"],
        "answer": "A"
    },
    {
        "question": "Which bolt-action rifle was the standard-issue weapon for German soldiers in both World Wars?",
        "options": ["A. Lee-Enfield", "B. Mosin-Nagant", "C. Karabiner 98k (Kar98k)", "D. M1 Garand"],
        "answer": "C"
    },
    {
        "question": "Which acclaimed World War II movie directed by Steven Spielberg opens with the Normandy beach landing?",
        "options": ["A. Dunkirk", "B. Saving Private Ryan", "C. 1917", "D. Fury"],
        "answer": "B"
    },
    {
        "question": "Which HBO miniseries follows the story of 'Easy Company' during World War II?",
        "options": ["A. The Pacific", "B. Band of Brothers", "C. Generation Kill", "D. Catch-22"],
        "answer": "B"
    },
    {
        "question": "In the movie 'Fury', Brad Pitt plays the commander of what type of military vehicle?",
        "options": ["A. Fighter Jet", "B. Submarine", "C. Sherman Tank", "D. Battleship"],
        "answer": "C"
    },
    {
        "question": "Which Call of Duty game introduced the highly popular 'Warzone' battle royale mode?",
        "options": ["A. Black Ops 4", "B. Modern Warfare (2019)", "C. WWII", "D. Infinite Warfare"],
        "answer": "B"
    },
    {
        "question": "What does the military weapon acronym 'RPG' officially stand for?",
        "options": ["A. Rapid Pressure Gun", "B. Rocket-Propelled Grenade", "C. Rifle Precision Gear", "D. Radar Pulse Grenade"],
        "answer": "B"
    },
    {
        "question": "Which light machine gun (LMG) is famous for its circular pan magazine and was used in WWII?",
        "options": ["A. DP-28", "B. M60", "C. Minimi", "D. MG42"],
        "answer": "A"
    },
    {
        "question": "Which country suffered the highest total number of casualties during World War II?",
        "options": ["A. Germany", "B. USA", "C. Soviet Union (USSR)", "D. UK"],
        "answer": "C"
    },
    {
        "question": "In 'Call of Duty: Black Ops', what is the name of the main protagonist who is interrogated about 'the numbers'?",
        "options": ["A. Alex Mason", "B. Frank Woods", "C. Jason Hudson", "D. Viktor Reznov"],
        "answer": "A"
    },
    {
        "question": "Which Netflix crime series revolves around a criminal mastermind known as 'The Professor'?",
        "options": ["A. Narcos", "B. Peaky Blinders", "C. Money Heist", "D. Ozark"],
        "answer": "C"
    },
    {
        "question": "Which movie features a specialized weapon called the 'Noisy Cricket'?",
        "options": ["A. Men in Black", "B. Star Wars", "C. Terminator", "D. Predator"],
        "answer": "A"
    },
    {
        "question": "Which sniper rifle in Call of Duty is famous for performing 'one-shot kills' and quickscopes?",
        "options": ["A. Intervention", "B. XPR-50", "C. Dragunov", "D. Outlaw"],
        "answer": "A"
    },
    {
        "question": "What is the name of the final main story mission in Call of Duty: Modern Warfare 2 (2009)?",
        "options": ["A. No Russian", "B. Endgame", "C. Loose Ends", "D. Cliffhanger"],
        "answer": "B"
    },
    {
        "question": "Which country developed the famous Maxim Gun, the first fully automatic machine gun?",
        "options": ["A. Germany", "B. United Kingdom", "C. United States", "D. France"],
        "answer": "C"
    },
    {
        "question": "What year did World War II officially end?",
        "options": ["A. 1939", "B. 1941", "C. 1945", "D. 1950"],
        "answer": "C"
    },
    {
        "question": "Which weapon type does the military term 'MANPADS' refer to?",
        "options": ["A. Heavy Machine Gun", "B. Shoulder-fired Anti-Aircraft Missile", "C. Combat Knife", "D. Tactical Drone"],
        "answer": "B"
    },
    {
        "question": "What is the name of the primary German secret police during World War II?",
        "options": ["A. Gestapo", "B. KGB", "C. MI6", "D. CIA"],
        "answer": "A"
    },
    {
        "question": "In 'The Matrix', which color pill does Neo take to see the real world?",
        "options": ["A. Blue", "B. Green", "C. Red", "D. Yellow"],
        "answer": "C"
    },
    {
        "question": "Which movie series features a fictional PMC company named 'Weyland-Yutani'?",
        "options": ["A. Alien", "B. Predator", "C. RoboCop", "D. Resident Evil"],
        "answer": "A"
    },
    {
        "question": "What caliber ammunition does the standard NATO military assault rifle (like M16) use?",
        "options": ["A. 7.62x39mm", "B. 5.56x45mm", "C. 9x19mm", "D. .308 Winchester"],
        "answer": "B"
    },
    {
        "question": "Which Call of Duty game was the first to be set entirely in a futuristic setting?",
        "options": ["A. Advanced Warfare", "B. Black Ops II", "C. Infinite Warfare", "D. Ghosts"],
        "answer": "B"
    },
    {
        "question": "Which historic battle involved the massive evacuation of Allied soldiers from French beaches?",
        "options": ["A. Battle of Dunkirk", "B. Battle of Waterloo", "C. Battle of Berlin", "D. Battle of Somme"],
        "answer": "A"
    },
    {
        "question": "What weapon is famously known as the 'Chicago Typewriter'?",
        "options": ["A. Colt M1911", "B. Thompson Submachine Gun", "C. BAR M1918", "D. Remington Shotgun"],
        "answer": "B"
    },
    {
        "question": "Who directed the 2017 epic World War I movie titled '1917'?",
        "options": ["A. Christopher Nolan", "B. Sam Mendes", "C. Quentin Tarantino", "D. Ridley Scott"],
        "answer": "B"
    },
    {
        "question": "In 'Peaky Blinders', what weapon do the Shelby family members hide inside their caps?",
        "options": ["A. Switchblades", "B. Razor Blades", "C. Small Pistols", "D. Brass Knuckles"],
        "answer": "B"
    },
    {
        "question": "Which weapon is the iconic service rifle of the British Armed Forces?",
        "options": ["A. L85A2 (SA80)", "B. FAMAS", "C. Steyr AUG", "D. FN SCAR"],
        "answer": "A"
    },
    {
        "question": "In Call of Duty, what is the highest streak reward that instantly ends the match?",
        "options": ["A. Chopper Gunner", "B. Tactical Nuke", "C. AC-130", "D. Juggernaut"],
        "answer": "B"
    },
    {
        "question": "What was the name of the American project that developed the atomic bomb during WWII?",
        "options": ["A. Manhattan Project", "B. Apollo Project", "C. Horizon Project", "D. Valkyrie Project"],
        "answer": "A"
    },
    {
        "question": "Which weapon is a pump-action shotgun famously used by the US military since the Vietnam War?",
        "options": ["A. Remington 870", "B. Mossberg 500", "C. AA-12", "D. Benelli M4"],
        "answer": "B"
    },
    {
        "question": "Which movie franchise features a high-tech assassin hotel called 'The Continental'?",
        "options": ["A. Jason Bourne", "B. Mission Impossible", "C. John Wick", "D. Kingsman"],
        "answer": "C"
    },
    {
        "question": "In the series 'The Boys', what is the name of the chemical substance that gives humans superpowers?",
        "options": ["A. Mutant Serum", "B. Compound V", "C. Super-Soldier Serum", "D. Project Extis"],
        "answer": "B"
    },
    # 25 NEW QUESTIONS (total 75)
    {
        "question": "Which game franchise features the character 'Captain Price' prominently?",
        "options": ["A. Halo", "B. Call of Duty", "C. Battlefield", "D. Medal of Honor"],
        "answer": "B"
    },
    {
        "question": "What is the name of the iconic zombie map in Call of Duty: Black Ops that features the band members?",
        "options": ["A. Kino der Toten", "B. Five", "C. Ascension", "D. Call of the Dead"],
        "answer": "A"
    },
    {
        "question": "Which firearm is known as the 'Browning Auto-5'?",
        "options": ["A. Shotgun", "B. Rifle", "C. Machine Gun", "D. Pistol"],
        "answer": "A"
    },
    {
        "question": "In the movie 'Heat', which two legendary actors face off in the famous shootout scene?",
        "options": ["A. Al Pacino & Robert De Niro", "B. Brad Pitt & Leonardo DiCaprio", "C. Denzel Washington & Tom Hanks", "D. Matt Damon & Ben Affleck"],
        "answer": "A"
    },
    {
        "question": "Which World War II tank was known as the 'Tiger'?",
        "options": ["A. German Panzer VI", "B. Soviet T-34", "C. American Sherman", "D. British Churchill"],
        "answer": "A"
    },
    {
        "question": "What does 'SMG' stand for in firearms?",
        "options": ["A. Small Machine Gun", "B. Sub-Machine Gun", "C. Semi-automatic Machine Gun", "D. Special Military Gun"],
        "answer": "B"
    },
    {
        "question": "Which Call of Duty game introduced the 'Pick 10' create-a-class system?",
        "options": ["A. Black Ops 2", "B. Modern Warfare 3", "C. Black Ops 1", "D. Ghosts"],
        "answer": "A"
    },
    {
        "question": "Who is the main antagonist in 'Call of Duty: Modern Warfare 2' (2009)?",
        "options": ["A. General Shepherd", "B. Vladimir Makarov", "C. Imran Zakhaev", "D. Raul Menendez"],
        "answer": "A"
    },
    {
        "question": "What is the name of the fictional country in the rebooted 'Call of Duty: Modern Warfare' (2019)?",
        "options": ["A. Urzikstan", "B. Verdansk", "C. Kastovia", "D. Al-Qatala"],
        "answer": "A"
    },
    {
        "question": "Which handgun was standard issue for the US military from 1985 to 2017?",
        "options": ["A. SIG M17", "B. Glock 19", "C. Beretta M9", "D. Colt M1911"],
        "answer": "C"
    },
    {
        "question": "What caliber is the M2 Browning heavy machine gun?",
        "options": ["A. .50 BMG", "B. .30-06 Springfield", "C. 7.62×51mm", "D. 5.56×45mm"],
        "answer": "A"
    },
    {
        "question": "Which movie features the famous line 'You can't handle the truth!'?",
        "options": ["A. A Few Good Men", "B. Top Gun", "C. Full Metal Jacket", "D. Platoon"],
        "answer": "A"
    },
    {
        "question": "In 'Saving Private Ryan', which character is the sniper?",
        "options": ["A. Private Jackson", "B. Private Reiben", "C. Private Mellish", "D. Captain Miller"],
        "answer": "A"
    },
    {
        "question": "Which battle is considered the largest tank battle in history?",
        "options": ["A. Battle of Kursk", "B. Battle of the Bulge", "C. Battle of El Alamein", "D. Battle of Stalingrad"],
        "answer": "A"
    },
    {
        "question": "What is the primary explosive compound used in C-4?",
        "options": ["A. RDX", "B. TNT", "C. Nitroglycerin", "D. PETN"],
        "answer": "A"
    },
    {
        "question": "Which Call of Duty title first introduced exoskeleton movement (Exo Suit)?",
        "options": ["A. Advanced Warfare", "B. Infinite Warfare", "C. Black Ops 3", "D. Ghosts"],
        "answer": "A"
    },
    {
        "question": "In the 'John Wick' series, what is the name of the hotel that serves as neutral ground for assassins?",
        "options": ["A. The High Table", "B. The Continental", "C. The Syndicate", "D. The Camorra"],
        "answer": "B"
    },
    {
        "question": "Which weapon is also known as the 'Ma Deuce'?",
        "options": ["A. M2 Browning", "B. M249 SAW", "C. M240B", "D. M60"],
        "answer": "A"
    },
    {
        "question": "What does the 'AR' in 'AR-15' stand for?",
        "options": ["A. Assault Rifle", "B. Automatic Rifle", "C. ArmaLite Rifle", "D. Advanced Rifle"],
        "answer": "C"
    },
    {
        "question": "Which movie features the US Navy's 'Top Gun' flight school?",
        "options": ["A. Top Gun", "B. Iron Eagle", "C. Stealth", "D. Flight of the Intruder"],
        "answer": "A"
    },
    {
        "question": "In 'Call of Duty: Black Ops Cold War', which character returns as a playable operator?",
        "options": ["A. Frank Woods", "B. Alex Mason", "C. Jason Hudson", "D. Viktor Reznov"],
        "answer": "A"
    },
    {
        "question": "Which German WWII machine gun was known as 'Hitler's Buzzsaw'?",
        "options": ["A. MG34", "B. MG42", "C. FG42", "D. MP40"],
        "answer": "B"
    },
    {
        "question": "What is the effective firing range of an M16 assault rifle (approx)?",
        "options": ["A. 300 m", "B. 550 m", "C. 800 m", "D. 1200 m"],
        "answer": "B"
    },
    {
        "question": "Which video game series features the 'Battlefield' franchise?",
        "options": ["A. EA DICE", "B. Activision", "C. Ubisoft", "D. Bethesda"],
        "answer": "A"
    },
    {
        "question": "In 'The Dark Knight', what is the make of the Batmobile?",
        "options": ["A. Lamborghini", "B. Tumbler (custom)", "C. Ferrari", "D. Porsche"],
        "answer": "B"
    }
];

class MyCustomError(Exception):
    pass
choice=None


def inp(opt1):
    
    user=input('Choose an option wisely \n').strip().upper()
    if not user:
            raise MyCustomError('Warning error!!! >>>> input not provided or being interrupted')
    if not user in opt1:
            raise MyCustomError('Warnig >>>> invalid option given or custom input error ')
    return user
             
score=0
wroans=0
def check(opt1,choice):
    global score,wroans
    try:
        ch=inp(opt1)
        print('checking....')
        time.sleep(1)
        if(ch==choice['answer']):
            print(f'correct !!!!{choice['answer']} is the right answer')
            score+=1
        else:
            print(f'wrong ,the correct answer is {choice['answer']}')
            wroans+=1
    except MyCustomError as e:
         print(e)
    except Exception as e:
         print(e)

def ques(questions,no):
    random.shuffle(questions)
    global score,wroans
    total=no
    print()
    print('QUIZ STARTED....................')
    time.sleep(1)
    selected=random.sample(questions,total)
    # for i in range(0,total):
    for i,selected in enumerate(selected,start=1):
        choice=selected
        diag='-'
        le=len(choice['question'])
        print(le*diag)

        print(f'the question {i} is : \n{le*diag}\n{choice['question']}')
        print(f'the options are :')
        opt1=[]
        for i in choice['options']:
            print(i)
            opt=i.split('.')
            opt1.append(opt[0])
        check(opt1,choice)
    time.sleep(2)
    print(f"\n{'='*40}")
    print(f" QUIZ COMPLETE!")
    print('Final Result!!!!!!')
    print(f"Your Score: {score} / {total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")
    print(f"{'='*40}")
    if(wroans>0):
         print(f'your wrong answers are : {wroans}')

print('loading...')
for i in range(40):
    print('-',end='')
    time.sleep(0.05)
print()
print("Welcome to the Quiz APP!!!!")
time.sleep(2)
no=int(input('enter the no. of ques for quiz'))
ques(questions,no)



