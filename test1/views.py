from django.http import HttpResponse
from django.template import loader
import traceback

def googleCap(request):
    template = loader.get_template('testing1/googlecapacha.html')
    return HttpResponse(template.render({}, request))

def googleconfirm(request):
    try:
        recaptcha = request.POST.get('g-recaptcha-response')
        print("recaptcha:",recaptcha)
        return HttpResponse("Done")
    except:
        print("Exception in googleconfirm", Exception)
        traceback.print_exc()
        return HttpResponse("error")