from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from documents.models import Document
from contact.models import Email, AccessRequest

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import  force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Siz uğurla sistemə daxil oldunuz')
            return redirect('home')
        else:
            messages.error(request, 'Daxil etdiyiniz məlumatlar düzgün deyil')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Siz uğurla sistemdən çıxış etdiniz')
        return redirect('login')
    return redirect('login')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            
            #Reset password email
            current_site     = get_current_site(request)
            mail_subject    = 'Şifrənin yenilənməsi'
            message         = render_to_string('accounts/reset_password_email.html', {
                'user':     user,
                'domain':   current_site,
                'uid':      urlsafe_base64_encode(force_bytes(user.pk)),
                'token':    default_token_generator.make_token(user),
            })
            to_email        = email
            send_email      = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Şirfənin yenilənməsi üçün link elektron poçt ünvanınıza göndərilmişdir')
            return redirect('login')
            
        else:
            messages.error(request, 'Poçt ünvanı məlumat bazasında mövcud deyil')
            return redirect('forgotPassword')
            
    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid  = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        return redirect('resetPassword')
    else:
        messages.error(request, 'Linkin vaxtı bitdiyindən aktiv deyil')
        return redirect('login')
    
    
    
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Şifrəniz uğurla yeniləndi')
            return redirect('login')
            
        else:
            messages.error(request, 'Password does not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')
    
    
@login_required(login_url = 'login')
def profile(request):
    documents   = Document.objects.order_by('-created_date')
    user        = User.objects.get(id=request.user.id)
    user_inquiry = Email.objects.order_by('-created_date').filter(user_id=request.user.id)
    user_request = AccessRequest.objects.order_by('-created_date').filter(user_id=request.user.id)
    
    data = {
        'user':         user,
        'documents':    documents,
        'inquiries':    user_inquiry,
        'requests':     user_request,
    }
    
    return render(request, 'accounts/profile.html', data)