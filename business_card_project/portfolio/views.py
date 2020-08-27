from django.shortcuts import render
from .models import Project
from .models import Skills
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from decouple import config
# Create your views here.


def home(request):
    return render(request,'portfolio/home.html')

def about_me(request):
    return render(request,'portfolio/aboutme.html')

def skills(request):
    my_skill = Skills.objects.all()
    content = {
        'my_skill' : my_skill,
    }
    return render(request,'portfolio/skills.html', content)

def projects(request):
    projects = Project.objects.all()
    content = {
        'projects':projects
    }
    return render(request,'portfolio/projects.html', content)

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            admin_address = config('admin_address')
            responder_address = config('responder_address')
            client_address = request.POST['email']
            message_for_admin = f"""
            name: {request.POST['name']}
            email: {request.POST['email']}
            message: {request.POST['message']}
            """feat (33): smtp configuration for sending e-mail added to the settings file
            message_for_client = f"""
            Thank you {request.POST['name'].capitalize()} for your message - I will answer to your question as soon as possible.
            Have a nice day! :)
            Tomasz Pasternak
             
            --- message generated automatically --- please do not reply to this email ---
            """
            try:
                send_mail(request.POST['subject'], message_for_admin, responder_address,[admin_address])
                send_mail(request.POST['subject'], message_for_client, responder_address,[client_address])
            except BadHeaderError:
                print('-----incorrect header-----')
            form = ContactForm()


    else:
        form = ContactForm()

    info = "Message sent - thank you!"
    content = {
        'form': form,
        'info': info,
    }
    return render(request,'portfolio/contact_form.html',content)