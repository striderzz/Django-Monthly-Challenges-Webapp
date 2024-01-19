from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string


monthly_challenges ={
    "january": "This is January Task!",
    "february": "This is February Task!",
    "march": "This is March Task!",
    "april": "This is April Task!",
    "may": "This is May Task!",
    "june": "This is June Task!",
    "july": "This is July Task!",
    "august": "This is August Task!",
    "september": "This is September Task!",
    "october": "This is October Task!",
    "november": "This is November Task!",
    "december": None

}


# Create your views here.
def index(request):
 
  months = list(monthly_challenges.keys())
  content = {"months":months}
  return render(request,"challenges/index.html",content)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    raise Http404()
  redirect_month=months[month-1]
  redirect_path = reverse("monthly-challenge",args = [redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
  try:
    challenges_text = monthly_challenges[month]
    content = {"month_name":month, "text":challenges_text}
    return render(request,"challenges/challenge.html",content)
   
  except:
    raise Http404()
  
  