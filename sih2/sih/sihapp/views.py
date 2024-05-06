from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
def home(request):
    return render(request,'home.html')

def details(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        username=request.POST['username']
        followers=request.POST['followers']
        follows=request.POST['follows']
        description=request.POST['description']
        profile=request.POST['profile']
        private=request.POST['private']
        
        print(fullname,username,followers,follows,description,profile,private)
    return render(request,'details.html')
def fun(x):
    if x=="Yes":
        return 1
    else:
        return 0
def fbdetails(request):
    if request.method=="POST":
        status=request.POST['status']
        favourites=request.POST['favourites']
        followers=request.POST['followers']
        friends=request.POST['friends']
        description=request.POST['description']
        lc=request.POST['listed_Count']
        utc=fun(request.POST['utc'])
        with open('C:/Users/Dell/model_pickle1','rb') as file:
            model = pickle.load(file)
        my_list = [status,followers,friends,favourites,lc,len(description),utc]
        my_array = np.array(my_list)
        prediction = model.predict(my_array.reshape(1,-1))
        print(prediction)
        if prediction==1:
            print("fake")
        else:
            print("real")
    return render(request,'fbdetails.html')