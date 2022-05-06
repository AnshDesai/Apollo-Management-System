from django.shortcuts import render,redirect
from django.urls import path
from Rmsstores import models
import smtplib
def login(request):         
    finyear = list(models.Finyear.objects.order_by('-fin').values_list('fin_year','fin'))   
    if 'Users' in request.session:
        return redirect('apps/Rmsstores/')    
    if 'sendemail' in request.POST:
        email = request.POST.get('email')
        sendemail(email)
        return redirect('/')

    if 'login' in request.POST:
        emp_id = request.POST.get('emp_id')
        plt = request.POST.get('plt')
        passwd = request.POST.get('passwd')
        fin = request.POST.get('finyear')
        print('FIN_YEAR',fin)
        Query = list(models.EmpInfo.objects.filter(emp_id=emp_id,plt=plt).values_list("passwd","emp_name"))
        for password in Query:
            if password[0] == passwd:
                request.session['Users'] = emp_id        
                request.session['Name'] = password[1]
                request.session['PLT'] = plt
                request.session['Finyear'] = fin
                request.session['TYPE'] = None
                request.session['rows'] = 1
                request.session['role'] = None
                print(request.session['Finyear'])
                return redirect("apps/Rmsstores/")
           
                        
    return render(request,"login.html",{'year':finyear})

def apps(request):
    # sessions_fin = request.sessions.get('fin')
    if 'Users' not in request.session:
        return redirect('/')
    return render(request,"aodms_applist.html")
    
def logout(request):
    del request.session['Users']
    return redirect('/')

def sendemail(email):
    try:
        password = list(models.EmpInfo.objects.filter(email=email).values_list('passwd',flat=True))
        gmail_user = 'apollotyres.limdaltd@gmail.com' # (You should provide your gmail account name)
        gmail_pwd = 'Limda@1220' # (You should provide your gmail password)
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + email + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Your recovered password for login: \n'
        print(header)
        msg = header +"Password:"+ password[0]
        smtpserver.sendmail(gmail_user, email, msg)
        print('done!')
        smtpserver.close()
    except Exception as e:
        print(e)
        