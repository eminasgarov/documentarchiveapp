from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from category.models import DocumentVariation, Department
from contact.models import Email, SupportTeam, AccessRequest
from django.contrib.auth.models import User
from accounts.views import login

# Create your views here.


@login_required(login_url=login)
def contact(request):
    team        = SupportTeam.objects.all().order_by('-created_date')
    subdoc      = DocumentVariation.objects.all()
    data = {
        'team':      team,
        'subdoc':    subdoc,
        }

    
    if request.method == 'POST':
        user_id         = request.POST['user_id']
        first_name      = request.POST['first_name']
        last_name       = request.POST['last_name']
        email           = request.POST['email']
        subject         = request.POST['subject']
        message         = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id

        email_contact = Email(user_id=user_id, first_name=first_name, last_name=last_name, subject=subject, email=email, message=message)
        
        #Sending notification mails:
        # admin_info  = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        
        # send_mail(
        #    'Yeni sorğu',
        #    'Sizə, ' + first_name + " "+ last_name + '-dan sorğu daxil olmuşdur.',
        #    'asgarov.emin@gmail.com',
        #    [admin_email],
        #    fail_silently=False,
        # )

        #Saving in DB:

        email_contact.save()
    
        messages.success(request, 'Sizin sorğunuz uğurla göndərilmişdir')

    return render(request, 'pages/contact.html', data)


@login_required(login_url=login)
def access_request(request):

    subdep      = Department.objects.all()
 
    data = {
        'subdep':    subdep,
        }

    
    if request.method == 'POST':
        user_id                    = request.POST['user_id']
        first_name                 = request.POST['first_name']
        last_name                  = request.POST['last_name']
        email                      = request.POST['email']
        employee_last_name         = request.POST['employee_last_name']
        employee_first_name        = request.POST['employee_first_name']
        employee_email             = request.POST['employee_email']
        employee_department        = request.POST['employee_department']
        employee_position          = request.POST['employee_position']
        employee_is_management     = request.POST['employee_is_management']
        employee_access_to_request = request.POST['employee_access_to_request']
        employee_is_admin          = request.POST['employee_is_admin']
        employee_admin_descr       = request.POST['employee_admin_descr']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = AccessRequest.objects.all().filter(employee_email=employee_email, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Sizin, sorğu yaradılan əməkdaş ilə bağlı, sorğunuz artıq mövcuddur')
                return redirect('access_request')

        access_request = AccessRequest(user_id=user_id, first_name=first_name, last_name=last_name, email=email, 
                                       employee_last_name=employee_last_name, employee_first_name=employee_first_name, 
                                       employee_email=employee_email, employee_department=employee_department, 
                                       employee_position=employee_position, employee_is_management=employee_is_management,
                                       employee_access_to_request=employee_access_to_request, employee_is_admin=employee_is_admin,
                                       employee_admin_descr=employee_admin_descr)
        
        #Sending notification mails:
        # admin_info  = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        
        # send_mail(
        #    'Yeni sorğu',
        #    'Sizə, ' + first_name + " "+ last_name + '-dan yeni əməkdaşın əlavə olunması sorğusu daxil olmuşdur.',
        #    'asgarov.emin@gmail.com',
        #    [admin_email],
        #    fail_silently=False,
        # )

        #Saving in DB:

        access_request.save()
    
        messages.success(request, 'Sizin sorğunuz uğurla göndərilmişdir')

    return render(request, 'pages/access_request.html', data)