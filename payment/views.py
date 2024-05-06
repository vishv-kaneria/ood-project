from django.shortcuts import render
from django.http import HttpResponse
import json, requests
from django.shortcuts import render, redirect

def payment(request):
    if request.method == 'POST':
        cardNumber= str(request.POST.get('cardNumber'))
        expiryDate = str(request.POST.get('expiryDate'))
        cvv = str(request.POST.get('cvv'))
        name = str(request.POST.get('name'))
        cardtype = 'Mastercards'

        if cardNumber[0] == '4':
            cardtype = 'VISA'

        data = {
            "CardType": cardtype,
            "Owner": name,
            "CardNumber": cardNumber,
            "CardExpiry": expiryDate,
            "CVV": cvv
        }
    
        print(data)
        json_data = json.dumps(data)
        print(json_data)

        response = requests.post("https://ood-project-api-6452e2a331a7.herokuapp.com/paymentCheck/", data=json_data)
        print(response.status_code)

        if response.status_code == 200:
            api_response = response.json()
            if api_response:         
                return HttpResponse("<h1>Transaction Successfully Completed..</h1>")
            else:
                return HttpResponse("API returned False")
        else:
            return HttpResponse("<h1>Transaction Failed!!</h1>")
        
    return render(request, 'payment.html')