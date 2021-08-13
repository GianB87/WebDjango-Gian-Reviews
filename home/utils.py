from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from users.models import User
from django.contrib.auth.forms import UserCreationForm
values = {0: 'NOT RATED',
        1: 'DO NOT READ',
        2: 'VERY BAD',
        3: 'BAD',
        4: 'MEDIOCRE',
        5: 'SO SO',
        6: 'FINE',
        7: 'GOOD',
        8: 'VERY GOOD',
        9: 'GREAT',
        10:'MASTERWORK'}

def get_yt_video_id(url):
    """Returns Video_ID extracting from the given url of Youtube
    
    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',
      
      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    from urllib.parse import urlparse, parse_qs

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url
        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError

def loginPostHttp(request):
    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(username,password)
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('Wrong User Name or Password')
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        print(username,password)
        print(user)
        if user is not None:
            login(request, user) # this is how we establish an user is login
            messages.success(request,"Welcome Back Dear " + user.get_username().capitalize())
            return HttpResponse('Reload') 
        else:
            # messages.error(request,"Invalid Credential")
            return HttpResponse('Wrong User Name or Password')

def registerPostHttp(request):
    if request.method =='POST':
        username = request.POST['username'].lower()
        mail = request.POST['email'].lower()
        password = request.POST['password']
        # print(username)
        try:
            user = User(username=username,email=mail)
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request,"Thanks for Sign Up " + user.username.capitalize()+', now enjoy.')
            return HttpResponse('Reload') 
        except:
            # messages.error(request, 'Invalid')
            return HttpResponse('Username or mail already exist')
        # if user is not None:
        #     login(request, user) # this is how we establish an user is login

        # else:
        #     messages.error(request,"Invalid Credential")
            