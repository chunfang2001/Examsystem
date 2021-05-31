from django.shortcuts import render, redirect
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
# Create your views here.
data = pd.read_csv("PredictSystem/static/example.csv")
inputs = data.drop(columns=['overtime','overlevel','overstress','fail','notinterested'])
target = data['overtime']

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs,target)


def index(request):
    return render(request,"index.html")

def ques(request):
    if request.method == "POST":
        age = request.POST['age']
        review_fre = request.POST['review_fre']
        study_time = request.POST['study_time']
        prepare_exam = request.POST['prepare_exam']
        sleeptime = request.POST['sleeptime']
        if request.POST.get('sleep') == None:
            return render(request,"ques.html",{
                "name" : request.POST['name'],
                "age" : request.POST['age'],
            })
        leisure = request.POST['leisure']
        prediction = model.predict([[age,review_fre,study_time,prepare_exam,sleeptime,request.POST['sleep'],leisure]])
        return render(request,"answer.html",{
            "prediction":prediction[0]
        })
    else:
        if request.GET.get('name')==None :
            return redirect(index)
        else : 
            if request.GET['name'] == "":
                return redirect(index)
        if request.GET.get('email')==None :
            return redirect(index)
        else : 
            if request.GET['email'] == "":
                return redirect(index)
        if request.GET.get('age')==None :
            return redirect(index)
        else : 
            if request.GET['age'] == "":
                return redirect(index)
        
        return render(request,"ques.html",{
            "name" : request.GET['name'],
            "age" : request.GET['age'],
        })