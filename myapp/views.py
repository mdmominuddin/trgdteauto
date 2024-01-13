from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from . models import CourseOffer, GovtOrder, Participants
from django.db.models import Sum
from . forms import ParticipantsForm, GovtOrderForm




def home(request):
    if request.method == 'POST':
        entered_password = request.POST.get('password')
        correct_password = "998877113355"

        if entered_password == correct_password:
            return redirect('section')

        else:
            return render(request, 'home.html', {'message': 'Incorrect password. Please try again.'})

    return render(request, 'home.html')




def sections(request):
    Section_list = ['HQ Trg Dte', 'Army Trg', 'Navy Trg', 'Air Trg', 'Joint Trg', 'Jt College']

    return render(request, 'sections.html', {'Section_list': Section_list})




def armytrg(request):

    ff_trg = CourseOffer.objects.select_related('event_name', 'ff_country').prefetch_related('vacancydistribution_set').all()

    # Calculate totals
    total_offered = ff_trg.aggregate(Sum('vac_offered'))['vac_offered__sum'] or 0
    total_accepted = ff_trg.aggregate(Sum('vac_accepted'))['vac_accepted__sum'] or 0
    total_regretted = ff_trg.aggregate(Sum('vac_regretted'))['vac_regretted__sum'] or 0

    govt_orders_and_participants = GovtOrder.objects.select_related(
        'svc', 'country'
    ).prefetch_related('participants').all()

    context = {
       'ff_trg': ff_trg,
       'total_offered': total_offered,
       'total_accepted': total_accepted,
       'total_regretted': total_regretted,
        'govt_orders_and_participants': govt_orders_and_participants,
    }

    return render(request, 'armydashboard.html', context)






def navytrg(request):
    context = {}
    return render(request, 'navydashboard.html', context)

def airtrg(request):
    context = {}
    return render(request, 'airdashboard.html', context)

def jttrg(request):
    ff_trg = CourseOffer.objects.select_related('event_name', 'ff_country').prefetch_related(
        'vacancydistribution_set').all()

    # Calculate totals
    total_offered = ff_trg.aggregate(Sum('vac_offered'))['vac_offered__sum'] or 0
    total_accepted = ff_trg.aggregate(Sum('vac_accepted'))['vac_accepted__sum'] or 0
    total_regretted = ff_trg.aggregate(Sum('vac_regretted'))['vac_regretted__sum'] or 0

    context = {
        'ff_trg': ff_trg,
        'total_offered': total_offered,
        'total_accepted': total_accepted,
        'total_regretted': total_regretted,
    }
    return render(request, 'jtdashboard.html', context)

def hqtrg(request):
    ff_trg = CourseOffer.objects.select_related('event_name', 'ff_country').prefetch_related(
        'vacancydistribution_set').all()

    # Calculate totals
    total_offered = ff_trg.aggregate(Sum('vac_offered'))['vac_offered__sum'] or 0
    total_accepted = ff_trg.aggregate(Sum('vac_accepted'))['vac_accepted__sum'] or 0
    total_regretted = ff_trg.aggregate(Sum('vac_regretted'))['vac_regretted__sum'] or 0

    context = {
        'ff_trg': ff_trg,
        'total_offered': total_offered,
        'total_accepted': total_accepted,
        'total_regretted': total_regretted,
    }
    return render(request, 'hqdashboard.html', context)
def Summary(request):
    context = {
        }
    return render(request, 'summary.html', context)

def AddParticipants(request):
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('armytrg')
        else:
            message = "Your entry has not been successful"

    else:
        form = ParticipantsForm()

    return render(request, 'add_participants.html', {'form': form})


def GovtOrderandParticipations(request):
    if request.method == 'POST':
        form1 = GovtOrderForm(request.POST)
        form2 = ParticipantsForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            # Save GovtOrder data
            go_instance = form1.save()

            # Save Participants data with the selected GovtOrder
            participant_instance = form2.save(commit=False)
            participant_instance.govt_order = go_instance  # Assuming GovtOrder is related to Participants
            participant_instance.save()

            return redirect('armytrg')  # Redirect to a success page or another view after successful submission
        else:
            # Form(s) are not valid, handle errors or provide feedback
            pass
    else:
        form1 = GovtOrderForm()
        form2 = ParticipantsForm()

    return render(request, 'add_go.html', {'form1': form1, 'form2': form2})
