from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from category.models import Document
from contact.models import Email, SupportTeam
from django.contrib.auth.models import User
from accounts.views import login

# Create your views here.


@login_required(login_url=login)
def contact(request):
    team = SupportTeam.objects.all().order_by('-created_date')
    subdoc   = Document.objects.all()
    data = {
        'team': team,
        'subdoc': subdoc,
        }

    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        

        email_contact = Email(first_name=first_name, last_name=last_name, subject=subject, email=email, message=message)
        
        #Sending notification mails:
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
           'Yeni sorğu',
           'Sizə, ' + first_name + " "+ last_name + '-dan sorğu daxil olmuşdur.',
           'asgarov.emin@gmail.com',
           [admin_email],
           fail_silently=False,
        )

        #Saving in DB:

        email_contact.save()
    
        messages.success(request, 'Sizin sorğunuz uğurla göndərilmişdir')

    return render(request, 'pages/contact.html', data)