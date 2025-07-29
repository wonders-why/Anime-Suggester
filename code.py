import random 

try:
    with open("Anime Suggester/Anime-Names.txt", "rt", encoding="utf-8") as anime:
        lines = anime.readlines() #creating a list of all the lines present in the anime-names.txt
       
        for x in range(1,len(lines)): #Removing extra spaces using Strip() also we can write [line.strip() for line in lines]
            lines[x]= lines[x].strip()
               
        anime_number = range(0, len(lines)) # getting a random number to choose anime from
        chosen_anime = random.choice(anime_number)
       
        print(lines[chosen_anime])
except FileNotFoundError:
    print("There was an error")

#version 2 will be out soon. this is like 3/10 right now. atleast i learned something