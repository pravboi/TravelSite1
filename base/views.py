from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from matplotlib.pyplot import title
from sqlalchemy import null
from .models import CurrentVehicle, Expedition, Module, Question, User, Vehicle, Ticket, OrderItem
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .pdf import html2pdf

def home(request):
    context = {}
    return render(request, "base/home.html", context)

def logout_user(request):
    logout(request)  # logs the user off
    return redirect("home")  # redirecting to home page

def login_page(request):
    page = "login"
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if user is not None:
                login(request, user)
                return redirect("home")
        except:
            print("wrong info")
            messages.error(request, "User no exist adn wrong info")

    context = {"page":page}
    return render(request, "base/login_register.html", context)

def register_page(request):
    page = "register"
    if request.method == "POST":
        first = request.POST.get("first-name")
        last = request.POST.get("last-name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if first != None and last != None and username != None and email != None and password1 != None and password2 != None and password1==password2:
            user= User.objects.create(first_name=first,last_name=last,username=username.lower(),email=email,password=password1)
            user.save()
            login(request, user)

            # Create users own modules and questions
            mods = ["Space Operation and Emergency Procedures","In-Flight Procedures","Spacesuit Training"]

            for mod_name in mods:
                m1 = Module.objects.create(title=mod_name) # unique module-obj for each user, all users share the same question-obj because it is not altered and is not dependent on the user.
                m1.save()
                if m1.title=="Space Operation and Emergency Procedures": # Optimized version we can create Question-objs in the admin panel and loop through them here. Cant do this for module because each user has unique progress
                    for q in Question.objects.all():
                        if q.mod_name == "Space Operation and Emergency Procedures":
                            m1.questions.add(q)
                            m1.save()
                    """m1.questions.add(Question.objects.create(prompt="What is the purpose of the emergency oxygen supply system?", choice1="To provide passengers with a scent of fresh air", choice2="To supply passengers with oxygen in the event of a depressurization", choice3="To provide extra oxygen for the crew members", answer="To supply passengers with oxygen in the event of a depressurization"))                                                                                                                                                                                                                                                                                                                   
                    m1.questions.add(Question.objects.create(prompt="How long can a spacecraft operate on backup power?", choice1="1 hour", choice2="24 hours", choice3="48 hours", answer="48 hours"))
                    m1.questions.add(Question.objects.create(prompt="What is the name of the emergency escape system used in case of a rocket malfunction during launch?", choice1=" Launch Escape System", choice2="Emergency Evacuation System", choice3="Rocket Rescue System", answer="Launch Escape System"))
                    m1.questions.add(Question.objects.create(prompt="How are fires extinguished in space?", choice1="Using water",choice2="Using foam",choice3="Using a carbon dioxide extinguisher", answer="Using a carbon dioxide extinguisher"))
                    m1.questions.add(Question.objects.create(prompt="What is the first step in an emergency situation?", choice1="Panic", choice2="Follow the crew's instructions", choice3="Try to fix the problem yourself", answer="Follow the crew's instructions"))
                    m1.questions.add(Question.objects.create(prompt="What is the purpose of the spacesuit?", choice1="To keep passengers warm", choice2="To provide oxygen to passengers", choice3="To protect passengers from the vacuum of space", answer="To protect passengers from the vacuum of space"))
                    m1.questions.add(Question.objects.create(prompt="What is the maximum number of passengers allowed on a Galaxy Tours spacecraft?", choice1="6",choice2="8",choice3="10",answer="8"))
                    m1.questions.add(Question.objects.create(prompt="What is the role of the flight crew during an emergency situation?", choice1="To evacuate passengers", choice2="To try to fix the problem themselves", choice3="To follow emergency procedures and keep passengers calm", answer="To follow emergency procedures and keep passengers calm"))
                    m1.questions.add(Question.objects.create(prompt="What is the purpose of the communications system on the spacecraft?", choice1="To play music for passengers", choice2="To communicate with ground control and other spacecraft", choice3="To provide entertainment to passengers", answer="To communicate with ground control and other spacecraft"))
                    m1.questions.add(Question.objects.create(prompt="How long does it take for a spacecraft to reach suborbital space?", choice1="5 minutes", choice2="10 minutes", choice3="15 minutes", answer="10 minutes"))"""
                if m1.title=="In-Flight Procedures":
                    for q in Question.objects.all():
                        if q.mod_name == "In-Flight Procedures":
                            m1.questions.add(q)
                            m1.save()
                    """m1.questions.add(Question.objects.create(prompt="During the in-flight phase, passengers must remain strapped in their seats until what signal is given?", choice1="A beep from the intercom", choice2="A green light on the control panel", choice3="A click from the seat belt buckle", choice4="An announcement from the pilot", answer="An announcement from the pilot"))
                    m1.questions.add(Question.objects.create(prompt="In case of sudden loss of cabin pressure, what should passengers do?", choice1="Put on their oxygen masks and remain in their seats", choice2="Open the emergency exit and jump out", choice3="Hold their breath and remain calm", choice4="Quickly unbuckle and run to the cockpit", answer="Put on their oxygen masks and remain in their seats"))
                    m1.questions.add(Question.objects.create(prompt="What should passengers do if they feel motion sickness during the flight?", choice1="Take off their headset and close their eyes", choice2="Try to sleep through the remainder of the flight", choice3="Request anti-nausea medication from the crew", choice4="Notify the pilot to return to Earth immediately", answer="Request anti-nausea medication from the crew"))
                    m1.questions.add(Question.objects.create(prompt="What is the primary source of communication between passengers and crew during the flight?", choice1="Intercom system", choice2="Hand signals", choice3="Text messaging", choice4="Morse code", answer="Intercom system"))
                    m1.questions.add(Question.objects.create(prompt="What is the maximum weight limit for personal items that passengers can bring on board the spacecraft?", choice1="10 pounds", choice2="20 pounds", choice3="30 pounds", choice4="40 pounds", answer="20 pounds"))
                    m1.questions.add(Question.objects.create(prompt="During takeoff and landing, what should passengers do with their arms and legs?", choice1="Cross them and remain still", choice2="Stretch them out and relax", choice3="Keep them close to their body", choice4="Wave them in the air", answer="Keep them close to their body"))
                    m1.questions.add(Question.objects.create(prompt="How often do passengers need to perform exercises to prevent muscle atrophy during the flight?", choice1="Once every hour", choice2="Once every two hours", choice3="Once every three hours", choice4="Once every four hours", answer="Once every two hours"))
                    m1.questions.add(Question.objects.create(prompt="What should passengers do in case of a fire on board the spacecraft?", choice1="Use the fire extinguisher provided in their seat", choice2="Notify the crew and evacuate immediately", choice3="Jump out of the spacecraft", choice4="Wait for the fire to extinguish on its own", answer="Use the fire extinguisher provided in their seat"))
                    m1.questions.add(Question.objects.create(prompt="What is the maximum duration of an in-flight restroom break allowed for passengers?", choice1="5 minutes", choice2="10 minutes", choice3="15 minutes", choice4="20 minutes", answer="10 minutes"))
                    m1.questions.add(Question.objects.create(prompt="What is the emergency procedure for a loss of communication between the spacecraft and the ground control?", choice1="The spacecraft will automatically return to Earth", choice2="The pilot will try to re-establish communication", choice3="Passengers should take over and operate the spacecraft", choice4="Passengers should remain calm and continue the mission", answer="The pilot will try to re-establish communication"))"""
                if m1.title=="Spacesuit Training":
                    for q in Question.objects.all():
                        if q.mod_name == "Spacesuit Training":
                            m1.questions.add(q)
                            m1.save()
                    """m1.questions.add(Question.objects.create(prompt="What is the purpose of a spacesuit during a spaceflight?", choice1="To keep the passenger warm", choice2="To provide oxygen to the passenger", choice3="To protect the passenger from the vacuum of space", choice4="To provide a comfortable environment", answer="To protect the passenger from the vacuum of space"))
                    m1.questions.add(Question.objects.create(prompt="How does a spacesuit regulate the temperature of the passenger?", choice1="By using a built-in air conditioner", choice2="By providing insulation", choice3="By circulating cool water through the suit", choice4="By using a heating element", answer="By circulating cool water through the suit"))
                    m1.questions.add(Question.objects.create(prompt="What is the purpose of a visor on a spacesuit helmet?", choice1="To provide a clear view of space", choice2="To protect the passenger from radiation", choice3="To protect the helmet from scratches", choice4="To prevent fogging of the helmet", answer="To provide a clear view of space"))
                    m1.questions.add(Question.objects.create(prompt="What is the maximum amount of time a passenger can spend in a spacesuit during a spaceflight?", choice1="1 hour", choice2="4 hours", choice3="8 hours", choice4="12 hours", answer="4 hours"))
                    m1.questions.add(Question.objects.create(prompt="How is the size of a spacesuit determined?", choice1="By the passenger's weight", choice2="By the passenger's height and weight", choice3="By the passenger's height, weight, and chest size", choice4="By the passenger's shoe size", answer="By the passenger's height, weight, and chest size"))
                    m1.questions.add(Question.objects.create(prompt="What is the purpose of the gloves on a spacesuit?", choice1="To provide a comfortable grip", choice2="To protect the hands from radiation", choice3="To protect the hands from extreme temperatures", choice4="All of the above", answer="All of the above"))
                    m1.questions.add(Question.objects.create(prompt="How does a space suit protect the passenger from radiation?", choice1="By using lead lining", choice2="By using a special reflective material", choice3="By using a layer of insulation", choice4="By using a radiation shield", answer="By using a radiation shield"))
                    m1.questions.add(Question.objects.create(prompt="How is the pressure inside a spacesuit regulated?", choice1="By a built-in air conditioning system", choice2="By a regulator that controls the flow of oxygen", choice3="By the passenger adjusting the suit manually", choice4="By a pump that circulates air through the suit", answer="By a pump that circulates air through the suit"))
                    m1.questions.add(Question.objects.create(prompt="How is a spacesuit tested for leaks before a spaceflight?", choice1="By submerging the suit in water", choice2="By pumping air into the suit and monitoring for leaks", choice3="By exposing the suit to extreme temperatures", choice4="By subjecting the suit to high levels of radiation", answer="By pumping air into the suit and monitoring for leaks"))
                    m1.questions.add(Question.objects.create(prompt="What is the purpose of the communication system on a spacesuit?", choice1="To provide a way for the passenger to communicate with ground control", choice2="To play music during the spaceflight", choice3="To provide a way for the passenger to listen to instructions", choice4="To monitor the passenger's vital signs", answer="To provide a way for the passenger to communicate with ground control"))"""
                user.modules.add(m1)
                user.save()

            return redirect("home")
        else:
            messages.error(request, "An error has occured during registration")
    context = {"page":page}
    return render(request, "base/login_register.html", context)

def spacecrafts_page(request):
    vehicles = Vehicle.objects.all()
    context = {"vehicles":vehicles}

    return render(request, "base/spacecrafts.html" ,context)

def expeditions_page(request):
    expeditions = Expedition.objects.all().reverse()
    cur_vehicles = CurrentVehicle.objects.all()
    context = {"expeditions": expeditions, "cur_vehicles": cur_vehicles}
    return render(request, "base/expeditions.html", context)

def view_expedition(request, pk):
    user = request.user
    is_valid_form = True
    exp = Expedition.objects.get(id=pk)
    cur_vehi = []
    for v in CurrentVehicle.objects.all():
        if v.expedition == exp:
            cur_vehi.append(v)

    succesful_payment = False
    if request.method == "POST":
        if str(user) == "AnonymousUser":
            return render(request, "base/error.html", {})
        asked_tics = int(request.POST.get("tickets"))
        choosen_vehicle = CurrentVehicle.objects.get(id=int(request.POST.get("vehicle")))

        if asked_tics > choosen_vehicle.ship.capacity-choosen_vehicle.passengers:
            is_valid_form = False
            print("Not Valid")
        else:
            price = asked_tics * choosen_vehicle.ship.ticket_cost
            o1 = OrderItem.objects.create(exp=choosen_vehicle.expedition, vehi=choosen_vehicle)

            for i in range(asked_tics):
                choosen_vehicle.passengers += 1                    
                t1 = Ticket.objects.create(price=price, date_purchased=datetime.now(), exped=choosen_vehicle.expedition)
                o1.tics.add(t1)
                o1.save()
                t1.save()
                choosen_vehicle.save()
            succesful_payment = True

        user.orders.add(o1)
        user.save()

    count = 0
    for v in cur_vehi:
        if v.passengers >= v.ship.capacity:
            count += 1
    if count >= len(cur_vehi):
        for v in cur_vehi:
            v.expedition.avalible = False
            v.expedition.save()
    

    context = {"cur_vehi":cur_vehi, "is_valid_form":is_valid_form, "exp":exp, "succesful_payment":succesful_payment}
    return render(request, "base/view_expedition.html", context)


def order_history(request):
    user = request.user
    orders = user.orders.all()
    context = {"orders":orders}
    return render(request, "base/order_history.html", context)


def view_modules(request):
    user = request.user
    if str(user) == "AnonymousUser":
        return render(request, "base/error.html", {})

    modules = user.modules.all()
    
    context = {"modules":modules}
    return render(request, "base/modules.html", context)


def take_module(request, pk):
    module = Module.objects.get(id=pk)
    total_questions = 10
    correct = 0
    if request.method == "POST":  # request = {prompt:1, prompt:2-ans}
        print(request.POST)
        for q in Question.objects.all():
            if request.POST.get(q.prompt) != "" and request.POST.get(q.prompt) != null and request.POST.get(q.prompt) != None:# if theres an answer
                if int(request.POST.get(q.prompt)) == 1: # if they entered choice-1 for this question
                    if q.choice1 == q.answer:  # if choice-1 is the answer
                        correct += 1
                        print("Correct")

            if request.POST.get(q.prompt) != "" and request.POST.get(q.prompt) != null and request.POST.get(q.prompt) != None:
                if int(request.POST.get(q.prompt)) == 2:
                    if q.choice2 == q.answer:  
                        correct += 1
                        print("Correct")

            if request.POST.get(q.prompt) != "" and request.POST.get(q.prompt) != null and request.POST.get(q.prompt) != None:
                if int(request.POST.get(q.prompt)) == 3: 
                    if q.choice3 == q.answer:  
                        correct += 1
                        print("Correct")

            if request.POST.get(q.prompt) != "" and request.POST.get(q.prompt) != null and request.POST.get(q.prompt) != None:
                if int(request.POST.get(q.prompt)) == 4: 
                    if q.choice4 == q.answer:  
                        correct += 1
                        print("Correct")
        
        print(str(correct) + "/" + str(total_questions))
        final_score = correct/total_questions * 100

        if final_score >= module.max_score:
            module.max_score = final_score
            module.save()

    questions = module.questions.all()
    context = {"module":module, "questions":questions}
    return render(request, "base/view_module.html", context)


def crew(request):
    context = {}
    return render(request, "base/crew.html", context) 


def pdf(request):
    pdf = html2pdf("base/pdf.html")
    return HttpResponse(pdf, content_type="application/pdf")



