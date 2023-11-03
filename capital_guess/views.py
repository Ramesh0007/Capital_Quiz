from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render, redirect
import random
#global variable to store the previous country's information
def guess_capital(request):
    # Fetch country data from the API if it's the first request
    api_url = "https://countriesnow.space/api/v0.1/countries/capital"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code != 200:
        message = "Failed to fetch data from the API."
        random_country = None
    else:
        countries = data["data"]
        random_country = random.choice(countries)
  

    context = {
        'random_country': random_country,
    }

    return render(request, 'capital_guess/game.html', context)


def getting_capital(passingCountry):
    api_url = "https://countriesnow.space/api/v0.1/countries/capital"
    
    response = requests.get(api_url)
    data = response.json()
    datas= data['data']
    country_dict = {country['name']: country['capital'] for country in datas }
    capital = country_dict.get(passingCountry, 'Capital not found')
    return capital
    



    
def guess_capital_result(request):
    if request.method == 'POST':
        user_guess = request.POST.get('user_guess', '').strip()
        capital_name = request.POST.get('country').strip()
        get_the_capital_results = getting_capital(capital_name)
        # print('this is getting the results from json', get_the_capital_results)
        if user_guess.lower() == get_the_capital_results.lower():
            message = "Correct! You guessed the capital correctly."
        else:
            message = f"Sorry, the correct capital is {capital_name}."
    else:
        message = ''

    context = {
        'message': message,
    }

    return render(request, 'capital_guess/result.html', context)