from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
# Create your views here.
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
import stripe


STRIPE_PUBLISH_KEY = 'pk_test_51Jw9n5IJR9m0PcVnotqaW0Nv3WRkiVbta6AWI0rwbgUYl4v4kidUXXPy0kHNOM2FoEaJ5X0s4aLShUyn3gJGaelY00G5lrXtqb'
STRIPE_SECRET_KEY = 'sk_test_51Jw9n5IJR9m0PcVnb7CaBjkTDPf0tgoWDuU2FCwOVrHql1NoKUHvanM7sDSb4eea5yuAMFv7fji3dNRwNHX8989J00Mh17pcCp'


def homeIndex(request):
    return render(request, 'home/homeIndex.html')



@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        #print('coming.....')
        stripe_config = {'publicKey': STRIPE_PUBLISH_KEY}
        return JsonResponse(stripe_config, safe=False)



@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = STRIPE_SECRET_KEY
        print("Check out.......")
        mylist = 'My Order'
        try:
            
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/?session_id={CHECKOUT_SESSION_ID}',
                payment_method_types=['card'],
                
                
                mode='payment',
                
                line_items=[
                    {
                        'name': mylist,
                        'quantity': 1,
                        'currency': 'euro',
                        'amount': '10555',
                    }
                ]
            )
            print('----->>>',checkout_session['id'])
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})    
        


def SuccessProcess(request):
    session_id = request.GET.get('session_id')
    print(session_id)
    return HttpResponse(f'success{session_id}')        


def CancleProcess(request):
    session_id = request.GET.get('session_id')
    print(session_id)
    return HttpResponse('Cancled Order')