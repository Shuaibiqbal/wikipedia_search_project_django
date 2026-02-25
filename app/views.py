from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
# Create your views here.
def search(request):
    if request.method == "POST":
        text = request.POST["texttosearch"]
        result = wikipedia.summary(text,sentences = 100)
        # print(result)
        return render(request, "app/index.html", {"text": result})
    return render(request, "app/index.html")