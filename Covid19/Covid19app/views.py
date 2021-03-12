from django.shortcuts import render

import requests

url = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    'x-rapidapi-key': "848cfc830dmshb600f6ea59e35bep1da43fjsndca13cd65eb7",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
respons = requests.request("GET", url, headers=headers).json()

def index(request):
    # print(respons)
    if request.method == "POST":
        country = request.POST.get('country')
        no=int(respons['results'])
        for x in range(0,no):
            # if country==respons['response'][x]['country']:
            #     print(respons['response'][x]['cases']['new'])
            if country==respons['response'][x]['country']:
                           New=respons['response'][x]['cases']['new']
                           Active=respons['response'][x]['cases']['active']
                           Discharge=respons['response'][x]['cases']['recovered']
                           Deaths=respons['response'][x]['deaths']['total']
                           Total=respons['response'][x]['cases']['total']
                           country=respons['response'][x]['country']
                           lastupdate=respons['response'][x]['day']
                           param = {'respons': respons, 'New': New, 'Active': Active, 'Discharge': Discharge, 'Deaths': Deaths,
                                    'Total': Total,'country':country,'lastupdate':lastupdate}
                           return render(request, 'index.html', param)



    param={'respons':respons}
    return render(request,'index.html',param)



