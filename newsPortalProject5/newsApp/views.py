from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"newsApp/index.html")


def moviesInfo(request):
    head_msg = 'Latest Movies Information'
    msg1 = 'Sonali slowly getting cured.'
    msg2 = 'Salman going to marriage soon.'
    msg3 = 'Narendra Modi is going to act in some movie.'
    my_dict = {'head_msg':head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,"newsApp/news.html", context=my_dict)


def sportsInfo(request):
    head_msg = 'Latest Sports Information'
    msg1 = 'Kohli gave left and right to broadman record.'
    msg2 = 'Indian performance not upto themark in asian games.'
    msg3 = 'First gold Accquired by china.'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request,"newsApp/news.html",context=my_dict)


def politicsInfo(request):
    head_msg = 'Latest Politics Information'
    msg1 = 'In telengana election will come in just 2 months.'
    msg2 = 'Narendra Modi says, Achchedin AAyengee!!!'
    msg3 = 'Kerala money gaya... Center wont accept and wont give!!!'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request,"newsApp/news.html",context=my_dict)