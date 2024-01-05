from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html', {})

def contact(request):

    api_key='AIzaSyBpsimhniF4xRbQc_e63TEwtZMazWsy7xU'
    context={"landmark":'Bergamo viale giulio cesare,26', "api_key":api_key}

    if request.method=='POST':
        """
         message_name=
        message_email=
        message_=

        """
        pass

    return render(request, 'website/contact.html', context)