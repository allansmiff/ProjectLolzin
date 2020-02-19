import requests
from django.shortcuts import render
from .forms import SummonerForm
from .models import Summoner
#class that creates functions to link the back to the front end
# Create your views here.


#method used in form view
def summoner_form(request):

    # the import from form SummonerForm set as a variable named form
    form = SummonerForm()

    #method that return that always needs a request and a template name, the third parameter is setting the form variable
    #as a form tag to use in html
    return render(request, 'CrudSummoner/summonerForm.html', {'form': form})


#method used in summoner view
def summoner_view(request):
    #my key in league of legends API website and stored in a variable named key
    key = 'RGAPI-cf84ca2b-ee07-49b1-aa4a-1832eaad5ed8'

    #get the name used in summoner form and stored in a variable named name
    name = request.GET['name']

    #url used in league of legends website to get data from summoner by name stored in a variable named url
    url = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name +'?api_key=' + key

    #do a request to the url above and stores in a variable named response
    response = requests.get(url)

    # gets the json of the request above and stores in a variable named json
    json = response.json()

    #uses the created method below to set the values form the json and sets it in a variable named summoner with is a
    # summoner model
    summoner = create_summoner(json)
    # method return that always needs a request, a view template name. the third parameter is defining the summoner
    # variable just above as a summoner tag to use in html
    return render(request, 'CrudSummoner/summonerView.html', {'summoner': summoner})


# method that recieves a json as parameter and return a summoner(as model)
def create_summoner(json):
    summoner = Summoner
    summoner.name = json['name']
    summoner.accountId = json['accountId']
    summoner.id = json['id']
    summoner.profileIconId = json['profileIconId']
    summoner.revisionDate = json['revisionDate']
    summoner.puuid = json['puuid']
    summoner.summonerLevel = json['summonerLevel']
    return summoner
