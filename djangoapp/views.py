from django.contrib.auth import authenticate
from django.core.mail import send_mail
from djangonew.settings import EMAIL_HOST_USER

from django.shortcuts import render,redirect
from .forms import *
from .models import *

import os
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
def first(request):
    return HttpResponse("HEYY")
def audioupload(request):
    if request.method=='POST':
        a=audioform(request.POST,request.FILES)
        if a.is_valid():
            an=a.cleaned_data["audioname"]
            ai=a.cleaned_data["audioimage"]
            af=a.cleaned_data["audiofile"]
            b=audiomodel(audioname=an,audioimage=ai,audiofile=af)
            b.save()
            return HttpResponse("audio uploaded")
        else:
            return HttpResponse("audio failed")
    return render(request,'audioupload.html')

def audiodisplay(request):
    a=audiomodel.objects.all()
    name=[]
    image=[]
    audio=[]
    for i in a:
        an=i.audioname
        name.append(an)

        ai=i.audioimage
        image.append(str(ai).split('/')[-1])

        af=i.audiofile
        audio.append(str(af).split('/')[-1])


    mylist=zip(name,image,audio)
    return render(request,'audiodisplay.html',{'mylist':mylist})

def shopreg(request):
    if request.method=='POST':
        a=shopregform(request.POST)
        if a.is_valid():
            sn=a.cleaned_data["shopname"]
            sa=a.cleaned_data["address"]
            si=a.cleaned_data["shopid"]
            se=a.cleaned_data["email"]
            sp=a.cleaned_data["phone"]
            spass=a.cleaned_data["password"]
            scp=a.cleaned_data["cpass"]
            if spass==scp:
                b=shopregmodel(shopname=sn,address=sa,shopid=si,email=se,phone=sp,password=spass)
                b.save()
                return redirect(shoplog)
            else:
                return HttpResponse('pass incorect')
        else:
            return HttpResponse('regs failed')
    return render(request,'shopreg.html')

def shoplog(request):
    if request.method=='POST':
        a=shoploginform(request.POST)
        if a.is_valid():
            sname=a.cleaned_data["shopname"]
            sp=a.cleaned_data["password"]
            #to make variable global
            request.session['shopname']=sname

            b=shopregmodel.objects.all()

            for i in b:

                if sname==i.shopname and sp==i.password:
                    request.session['id']=i.id
                    return redirect(productprofile)
            else:
                return HttpResponse("login failed")


    return render(request,'shoplogin.html')



def productprofile(request):
    a=request.session['shopname']

    return render(request,'products-profile.html',{'sn':a})


def productupload(request):
    if request.method=='POST':
        a=productuploadform(request.POST,request.FILES)
        id=request.session['id']
        if a.is_valid():
            name=a.cleaned_data["pname"]
            p=a.cleaned_data["price"]
            d=a.cleaned_data["des"]
            im=a.cleaned_data["pimage"]
            b=productuploadmodel(shopid=id,pname=name,price=p,des=d,pimage=im)
            b.save()
            return redirect(productdisplay)
        else:
            return HttpResponse("Upload failed")


    return render(request,'productupload.html')


def productdisplay(request):
    shpid=request.session['id']
    a=productuploadmodel.objects.all()
    n=[]
    p=[]
    d=[]
    im=[]
    id=[]
    shopid=[]
    for i in a:
        sid=i.shopid
        shopid.append(sid)

        ide=i.id
        id.append(ide)

        nm=i.pname
        n.append(nm)

        pr=i.price
        p.append(pr)

        de=i.des
        d.append(de)

        ime=i.pimage
        im.append(str(ime).split('/')[-1])
    thelist=zip(n,p,d,im,id,shopid)

    return render(request,'productsdisplay.html',{'thelist':thelist,'shpid':shpid})


def allproductdisplay(request):

    a=productuploadmodel.objects.all()
    n=[]
    p=[]
    d=[]
    im=[]
    id=[]

    for i in a:


        ide=i.id
        id.append(ide)

        nm=i.pname
        n.append(nm)

        pr=i.price
        p.append(pr)

        de=i.des
        d.append(de)

        ime=i.pimage
        im.append(str(ime).split('/')[-1])
    thelist=zip(n,p,d,im,id)

    return render(request,'allproductsdisplay.html',{'thelist':thelist})


#models.objects.get(id=id)
def productdelete(request,id):
    a=productuploadmodel.objects.get(id=id)
    a.delete()
    return redirect(productdisplay)

def productedit(request,id):

    a=productuploadmodel.objects.get(id=id)
    im=a.pimage
    x= str(im).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES):#check new files
            if len(a.pimage)>0:#checking old files
                os.remove(a.pimage.path)
            a.pimage=request.FILES['edimage']
        a.pname=request.POST.get('edname')
        a.price=request.POST.get('edprice')
        a.des=request.POST.get('eddes')
        a.save()
        return redirect(productdisplay)


    return render(request,'editproduct.html',{'a':a,'img':x})






def userreg(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password=request.POST.get('password')
        #checking wheather the username exists,User is our builtin model-import User
        if User.objects.filter(username=username).first():#first is for getting first object from filter query
            messages.success(request,'username already exists')#messages.success is a framework that allows you to store messages in one request  and retrive them in the request page
            return redirect(userreg)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already taken')
            return redirect(userreg)
        user_obj=User(username=username,email=email,first_name=firstname,last_name=lastname)
        user_obj.set_password(password) #set_password is used to secure the password
        user_obj.save()
        #import uuid module
        auth_token=str(uuid.uuid4())
        #newmodel creation depending on data ie,create
        #profile model-objects
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)#mail sending function
        return render(request,'success.html')
    return render(request,'userregister.html')

def success(request):
    return render(request,'success.html')



#email sending function django
def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    #f is a string literal which contains expressions inside curley brackets,the expressions are replaced by values
    message=f'click the link to verify the account http://127.0.0.1:8000/djangoapp/verify/{auth_token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    #inbuilt fn sendmail
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:#false
            messages.success(request,'your account is already verified')
            return redirect(ulogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(ulogin)
    else:
        messages.success(request,'user not found')
        return redirect(ulogin)


def ulogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username']=username

        user_obj = User.objects.filter(username=username).first()#username search give first obj


        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(ulogin)
        profile_obj = profile.objects.filter(user=user_obj).first()#searching username in profilemodel
        request.session['id'] = user_obj.id
        if not profile_obj.is_verified:#true allenkil
            messages.success(request,'profile not verfied check your mail')
            return redirect(ulogin)
        user = authenticate(username=username,password=password)



        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(ulogin)
        return redirect(userprofile)
    return render(request,'userlogin.html')


def userprofile(request):
    un=request.session['username']
    return render(request,'userprofile.html',{'un':un})


def userallproducts(request):

    a=productuploadmodel.objects.all()
    n=[]
    p=[]
    d=[]
    im=[]
    id=[]
    for i in a:

        ide=i.id
        id.append(ide)

        nm=i.pname
        n.append(nm)

        pr=i.price
        p.append(pr)

        de=i.des
        d.append(de)

        ime=i.pimage
        im.append(str(ime).split('/')[-1])
    thelist=zip(n,p,d,im,id)


    return render(request,'userallproducts.html',{'thelist':thelist})

def addcart(request,id):
    un = request.session['username']
    a=productuploadmodel.objects.get(id=id)

    if cart.objects.filter(pname=a.pname):
        return HttpResponse("already in cart")
    b=cart(username=un,pname=a.pname,price=a.price,des=a.des,pimage=a.pimage)
    b.save()
    return redirect(displaycart)

def wishlist(request,id):
    a=productuploadmodel.objects.get(id=id)
    usid=request.session['id']
    b=wishlistm(userid=usid,pname=a.pname,price=a.price,des=a.des,pimage=a.pimage)
    b.save()
    return redirect(displaywishlist)

def wishlisttocart(request,id):
    usn=request.session['username']
    a=wishlistm.objects.get(id=id)
    if cart.objects.filter(pname=a.pname):
        return HttpResponse('Item already in cart')
    b=cart(username=usn,pname=a.pname,price=a.price,des=a.des,pimage=a.pimage)
    b.save()
    return redirect(displaycart)


def displaycart(request):
    un=request.session['username']
    a=cart.objects.all()
    pn=[]
    pp=[]
    d=[]
    pim=[]
    id=[]
    usernm=[]
    for i in a:
        uname=i.username
        usernm.append(uname)

        ide=i.id
        id.append(ide)

        pnm=i.pname
        pn.append(pnm)

        pric=i.price
        pp.append(pric)

        di=i.des
        d.append(di)

        im=i.pimage
        pim.append(str(im).split('/')[-1])
    x=zip(pn,pp,d,pim,id,usernm)
    return render(request,'cartdisplay.html',{'x':x,'username':un})

def displaywishlist(request):
    usid=request.session['id']
    a=wishlistm.objects.all()
    pnme=[]
    ppe=[]
    descr=[]
    pima=[]
    id=[]
    userid=[]
    for i in a:
        uside=i.userid
        userid.append(uside)

        ide=i.id
        id.append(ide)

        pnm=i.pname
        pnme.append(pnm)

        pric=i.price
        ppe.append(pric)

        di=i.des
        descr.append(di)

        im=i.pimage
        pima.append(str(im).split('/')[-1])
    y=zip(pnme,ppe,descr,pima,id,userid)
    return render(request,'wishlistdisplay.html',{'y':y,'userid':usid})

def removecart(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(displaycart)

def wishremove(request,id):
    a=wishlistm.objects.get(id=id)
    a.delete()
    return redirect(displaywishlist)



def cartbuy(request,id):
    a=cart.objects.get(id=id)
    img = a.pimage
    x = str(img).split('/')[-1]
    if request.method=='POST':

        nm = request.POST.get('name')
        pr = request.POST.get('price')
        des=request.POST.get('description')
        quan = request.POST.get('quantity')
        b=buy(pname=nm,price=pr,des=des,quantity=quan)
        b.save()
        total=int(pr)*int(quan)
        return render(request,'finalbill.html',{'b':b,'t':total,'x':x})
    return render(request,'buyproduct.html',{'a':a,'x':x})

def cardpay(request):
    if request.method=='POST':
        cardname=request.POST.get('cname')
        cardnumber=request.POST.get('cnumber')
        cardexpiry=request.POST.get('expiry')
        securitycode=request.POST.get('security')
        b=customerdetailsmodel(name=cardname,cardno=cardnumber,cardexpiry=cardexpiry,security=securitycode)
        b.save()
        from datetime import timedelta
        a=datetime.date.today()
        d=a+timedelta(15)
        return render(request,'ordersuccess.html',{'date':d})
    return render(request,'placeorder.html')


def shopnotification(request):
    c = []
    t = []
    a=shop_notification.objects.all()
    for i in a:
        ct=i.content
        c.append(ct)
        ti=i.Datetimeshop
        t.append(ti)
    x=zip(c,t)
    return render(request,'shopnot.html',{'x':x})

def usernotification(request):
    a=user_notification.objects.all()
    uc=[]
    ut=[]
    for i in a:
        cnt=i.content
        uc.append(cnt)
        usd=i.datetimeuser
        ut.append(usd)
    x=zip(uc,ut)
    return render(request,'usernot.html',{'x':x})



