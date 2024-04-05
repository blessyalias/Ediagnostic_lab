from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from datetime import date, datetime

# Create your views here.

def Index(request):
    return render(request,'index.html')

def login(request):
    if request.POST:
        usname = request.POST["username"]
        pasw = request.POST["password"]
        check_cust_user = authenticate(username=usname,password = pasw)
        if check_cust_user is not None:
                if check_cust_user.is_superuser == True:
                    messages.info(request,"Login successfull")
                    return redirect("/admin_home")
                elif check_cust_user.is_staff == True:
                    chef = LabReg.objects.get(email = usname)
                    request.session['uid'] = chef.id
                    messages.info(request,"Login successfull")
                    return redirect("/lab_home")
                elif check_cust_user.is_staff == False:
                    du = UserReg.objects.get(email = usname)
                    request.session['uid'] = du.id
                    messages.info(request,"Login successfull")
                    return redirect("/user_home")
                else:
                    messages.info(request,"User type not found")
        elif User.objects.filter(username = usname):
            cust = User.objects.get(username = usname)
            if cust.is_active == 0:
                messages.info(request,"User not approved")
            else:
                messages.info(request,"Password not matching")
        else:
            messages.info(request,"User dosent exist")
    return render(request,'login.html')

def client_reg(request):
    if request.POST:
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        contact =  request.POST["phone"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        address = request.POST["address"]
        health = request.POST["health"]
        if UserReg.objects.filter(Q(user__username = username) | Q(contact = contact)).exists():
            messages.info(request,"Email or phone no is taken")
        else:
            dataToUser = User.objects.create_user(first_name = first_name,
                                            last_name = last_name,
                                            username = username,
                                            email = email,
                                            password = password,
                                            is_staff = 0,
                                            is_active = 1)
            dataToUser.save()
            dataToReg = UserReg.objects.create(first_name = first_name,
                                                last_name = last_name,
                                                contact = contact,
                                                email = username,
                                                address = address,
                                                health = health,
                                                user = dataToUser)
            dataToReg.save()
            messages.info(request,"User Registered")
            return redirect("/login")
    return render(request,'client_reg.html')

def lab_reg(request):
    if request.POST:
        first_name = request.POST["fname"]
        location = request.POST["loc"]
        contact =  request.POST["phone"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        address = request.POST["address"]
        if LabReg.objects.filter(Q(user__username = username) | Q(contact = contact)).exists():
            messages.info(request,"Email or phone no is taken")
        else:
            dataToUser = User.objects.create_user(first_name = first_name,
                                            username = username,
                                            email = email,
                                            password = password,
                                            is_staff = 1,
                                            is_active = 1)
            dataToUser.save()
            dataToReg = LabReg.objects.create(name = first_name,
                                                location = location,
                                                contact = contact,
                                                email = username,
                                                address = address,
                                                user = dataToUser)
            dataToReg.save()
            messages.info(request,"Lab Registered")
            return redirect("/login")
    return render(request,'lab_reg.html')

def admin_home(request):
    return render(request,'admin_home.html')

def admin_client(request):
    data = UserReg.objects.all()
    return render(request,'admin_client.html',{"data":data})

def admin_lab(request):
    data = LabReg.objects.all()
    return render(request,'admin_lab.html',{"data":data})

def admin_action(request):
    id = request.GET.get("id")
    action = request.GET.get("action")
    if(action == "clientBlock"):
        client = UserReg.objects.get(id = id)
        client.user.is_active = 0
        client.user.save()
        return redirect("/admin_client")
    elif(action == "clientApprove"):
        client = UserReg.objects.get(id = id)
        client.user.is_active = 1
        client.user.save()
        return redirect("/admin_client")
    elif(action == "labBlock"):
        client = LabReg.objects.get(id = id)
        client.user.is_active = 0
        client.user.save()
        return redirect("/admin_lab")
    elif(action == "labApprove"):
        client = LabReg.objects.get(id = id)
        client.user.is_active = 1
        client.user.save()
        return redirect("/admin_lab")
    elif(action == "testDel"):
        client = Tests.objects.get(id = id)
        client.delete()
        return redirect("/admin_tests")

def admin_tests(request):
    data = Tests.objects.all()
    return render(request,'admin_tests.html',{"data":data})

def admin_orders(request):
    data = Slots.objects.all().order_by("-id")
    return render(request,'admin_orders.html',{"data":data})

def admin_payments(request):
    data = Payment.objects.all()
    return render(request,'admin_payments.html',{"data":data})

def lab_home(request):
    return render(request,'lab_home.html')

def lab_tests(request):
    userid = request.session["uid"]
    lab = LabReg.objects.get(id = userid)
    data = Tests.objects.filter(lab__id = userid)
    if request.POST:
        test = request.POST["test"]
        description = request.POST["description"]
        price = request.POST["price"]
        if Tests.objects.filter(Q(lab__id = userid) & Q(test = test)).exists():
            messages.info(request,"This test alredy eexists")
        else:
            toTest = Tests.objects.create(lab = lab,
                                        test = test,
                                        description = description,
                                        price = price)
            toTest.save()
    return render(request,'lab_tests.html',{"data":data})

def labDelTest(request):
    id = request.GET.get("id")
    Task = Tests.objects.get(id = id)
    Task.delete()
    return redirect("/lab_tests")

def lab_slots(request):
    userid = request.session["uid"]
    lab = LabReg.objects.get(id = userid)
    if request.POST:
        date = request.POST["date"]
        time = request.POST["time"]
        if Slots.objects.filter(Q(lab__id = userid) & Q(date = date) & Q(time = time)).exists():
            messages.info(request,"This slot alredy eexists")
        else:
            toTest = Slots.objects.create(lab = lab,
                                        date = date,
                                        time = time)
            toTest.save()
    data = Slots.objects.filter(lab__id=userid).order_by("-id")
    return render(request,'lab_slots.html',{"data":data})

def lab_completed(request):
    id = request.GET.get("id")
    Task = Slots.objects.get(id = id)
    Task.testStatus = 1
    Task.save()
    return redirect("/lab_slots")

def lab_addReport(request):
    id = request.GET.get("id")
    Task = Slots.objects.get(id = id)
    if request.POST:
        report = request.FILES["report"]
        Task.report = report
        Task.save()
    return render(request,"lab_addReport.html")

def user_home(request):
    return render(request,'user_home.html')

def user_labs(request):
    data = LabReg.objects.all()
    return render(request,'user_labs.html',{"data":data})

def user_slots(request):
    labid = request.GET.get("id")
    lab = LabReg.objects.get(id = labid)
    today = date.today()
    data = Slots.objects.filter(Q(lab__id = labid) & Q(date__gt = today))
    return render(request,'user_slots.html',{"data":data,"lab":lab.name})

def user_bookslot(request):
    userid = request.session["uid"]
    user = UserReg.objects.get(id = userid)
    slotid = request.GET.get("id")
    slot = Slots.objects.get(id = slotid)
    data = Tests.objects.filter(lab__id = slot.lab.id)
    if request.POST:
        testid = request.POST['test']
        test = Tests.objects.get(id = testid)
        slot.user = user
        slot.test = test
        slot.save()
        return redirect(f"/user_slots?id={slot.lab.id}")
    return render(request,'user_bookslot.html',{"data":data})

def user_bookings(request):
    userid = request.session["uid"]
    user = UserReg.objects.get(id = userid)
    slot = Slots.objects.filter(user__id=userid).order_by("-id")
    return render(request,'user_bookings.html',{"data":slot})

def user_tests(request):
    data = Tests.objects.all()
    return render(request,'user_tests.html',{"data":data})

def user_pay(request):
    userid = request.session["uid"]
    user = UserReg.objects.get(id = userid)
    slotid = request.GET.get("sid")
    slot = Slots.objects.get(id = slotid)
    amount = slot.test.price
    if request.POST:
        payment = Payment.objects.create(amount = amount,
                                        user = user,
                                        slot = slot)
        payment.save()
        slot.testStatus = 2
        slot.save()
        return redirect(f"/user_bookings")
    return render(request,'user_pay.html',{"amt":amount})

def user_payments(request):
    userid = request.session["uid"]
    data = Payment.objects.filter(user__id = userid)
    return render(request,'user_payments.html',{"data":data})
