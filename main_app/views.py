from django.shortcuts import render
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, age):
    self.name = name
    self.age = age

finches = [
  Finch('Lolo', 3),
  Finch('Sachi', 0),
  Finch('Fancy', 4),
  Finch('Bonk', 6)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Buttercup ᓚᘏᗢ</h1>')
def about(request):
  return render(request, 'about.html')
def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })