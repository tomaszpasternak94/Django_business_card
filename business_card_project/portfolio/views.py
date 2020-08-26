from django.shortcuts import render
from .models import Project
from .models import Skills
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
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
            admin_address = 't.pasternak94@gmail.com'
            responder_address = 'responder@pythondeveloper.pl'
            client_address = form.email
            message_for_admin = f"""
            name: {form.name}
            email: {form.email}
            message: {form.message}
            """
            message_for_client = f"""
            Thank you {form.name.capitalize()} for your message - I will answer to your question as soon as possible.
            Have a nice day! :)
            Tomasz Pasternak
             
            --- message generated automatically --- please do not reply to this email ---
            """
            try:
                send_mail(form.subject, message_for_admin, responder_address,[admin_address])
                send_mail(form.subject, message_for_client, responder_address,[client_address])
            except BadHeaderError:
                print('-----incorrect header-----')

    else:
        form = ContactForm()

    info = "Message sent - thank you!"
    content = {
        'form': form,
        'info': info,
    }
    return render(request,'portfolio/contact_form.html',content)