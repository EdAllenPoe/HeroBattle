
from django.shortcuts import render, redirect
import json
import requests
import random



def home(request):
    
    return render(request, 'home.html', {})


def battle(request):

    # Random number for hero ID

    number = random.randint(1,730)
    number2 = random.randint(1,730)

    # Retrieve random hero number 1 information from API

    # Hero 1 Image URL
    url = "https://superheroapi.com/api/10212461243244710/"+str(number)+"/image"
    # Hero 1 Name URL
    urlx = "https://superheroapi.com/api/10212461243244710/" + \
        str(number)+"/name"
    #Hero 1 Power Statistics URL
    urlp = "https://superheroapi.com/api/10212461243244710/" + \
        str(number)+"/powerstats"
    
    # Retrieve random hero number 2 information from API

    # Hero 2 Image URL
    url2 = "https://superheroapi.com/api/10212461243244710/"+str(number2)+"/image"
    # Hero 2 Name URL
    urlx2 = "https://superheroapi.com/api/10212461243244710/" + \
        str(number2)+"/name"
    #Hero 2 Power Statistics URL
    urlp2 = "https://superheroapi.com/api/10212461243244710/" + \
        str(number2)+"/powerstats"

    # Parse Json 

    api_request = requests.get(
        url)
    apihero = json.loads(api_request.content)


    api_requestx = requests.get(
        urlx)
    apiherox = json.loads(api_requestx.content)


    api_requestp = requests.get(
        urlp)
    apiherop = json.loads(api_requestp.content)


    api_request2 = requests.get(
        url2)
    apihero2 = json.loads(api_request2.content)


    api_requestx2 = requests.get(
        urlx2)
    apiherox2 = json.loads(api_requestx2.content)


    api_requestp2 = requests.get(
        urlp2)
    apiherop2 = json.loads(api_requestp2.content)

    api_requestp2 = requests.get(
        urlp2)
    apiherop2 = json.loads(api_requestp2.content)

    # API stats for template hero number 1

    name = apihero['name']
    intelligence = apiherop['intelligence']
    combat = apiherop['combat']
    power = apiherop['power']
    strength = apiherop['strength']
    speed = apiherop['speed']
    durability = apiherop['durability']

    # Handle 'null' returns from hero 1 API by returning random stats

    if combat == 'null':
        combat = random.randrange(1, 100)
    if power == 'null':
        power = random.randrange(1, 100)
    if intelligence == 'null':
        intelligence = random.randrange(1, 100)
    if strength == 'null':
        strength = random.randrange(1, 100)
    if speed == 'null':
        speed = random.randrange(1, 100)
    if durability == 'null':
        durability = random.randrange(1, 100)
    
    # API stats for template hero number 2

    name2 = apihero2['name']
    intelligence2 = apiherop2['intelligence']
    combat2 = apiherop2['combat']
    power2 = apiherop2['power']
    strength2 = apiherop2['strength']
    speed2 = apiherop2['speed']
    durability2 = apiherop2['durability']

    # Handle 'null' returns from hero 2 API by returning random stats

    if combat2 == 'null':
        combat2 = random.randrange(1, 100)
    if power2 == 'null':
        power2 = random.randrange(1, 100)
    if intelligence2 == 'null':
        intelligence2 = random.randrange(1, 100)
    if strength2 == 'null':
        strength2 = random.randrange(1, 100)
    if speed2 == 'null':
        speed2 = random.randrange(1, 100)
    if durability2 == 'null':
        durability2 = random.randrange(1, 100)

    # Calculate hero 'power' for comparison

    total1 = int(intelligence)+int(combat)+int(power) + int(strength)+int(speed)+int(durability)

    total2 = int(intelligence2)+int(combat2)+int(power2) + int(strength2)+int(speed2)+int(durability2)

    # Compare hero 'power' stats to determine the winner
    
    if total1 > total2:
        victor = name
        color = 'success'
        text = 'WINNER'
        color2 = 'danger'
        text2 = 'LOSER'
    elif total2 > total1:
        victor = name2
        color = 'danger'
        text = 'LOSER'
        color2 = 'success'
        text2 = 'WINNER'
    

    return render(request, 'battle.html', {'apihero': apihero,
                                         'apiherox': apiherox, 'apihero2': apihero2, 'apiherox2': apiherox2,
                                         'apiherop': apiherop, 'apiherop2': apiherop2,'victor':victor, 'name':name, 'intelligence': intelligence, 'combat': combat,
                                         'power': power, 'strength': strength, 'speed': speed, 'durability': durability,'total1':total1, 'name2':name2,
                                         'intelligence2': intelligence2, 'combat2': combat2,
                                         'power2': power2, 'strength2': strength2, 'speed2': speed2, 'durability2': durability2,'total2':total2,'text':text,'text2':text2,
                                         'color':color,'color2':color2})




