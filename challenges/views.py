from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges ={
   "jan":"This is Jan Task! ",
   "feb":"This is Feb Task! ",
   "mar":"This is March Task! ",
   "apr":"This is April Task! ",
   "may":"This is May Task! ",
   "jun":"This is June Task! ",
   "jul":"This is July Task! ",
   "aug":"This is August Task! ",
   "sep":"This is September Task! ",
   "oct":"This is October Task! ",
   "nov":"This is November Task! ",
   "dec":"This is Dec Task! ",

}


# Create your views here.
def index(request):
  list_items=""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path =  reverse("monthly-challenge",args =[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
  

  response_data =f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound("Month not found ! ")
  redirect_month=months[month-1]
  redirect_path = reverse("monthly-challenge",args = [redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
  try:
    challenges_text = monthly_challenges[month]
    return HttpResponse(f'<h1>{challenges_text}</h1>')
  except:
    return HttpResponseNotFound("This month is not supported! ")