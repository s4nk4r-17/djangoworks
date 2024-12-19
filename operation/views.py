from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")

        result=int(num1)+int(num2)

        print(result)

        data={
            "output":result
        }

        return render(request,"add.html",data)
    

class SubtractionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")

        result=int(num1)-int(num2)

        data={
            "output":result
        }

        return render(request,"sub.html",data)
    
class MultiplicationView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"multiple.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")

        result=int(num1)*int(num2)

        data={
            "output":result
        }

        return render(request,"multiple.html",data)
    
#_____________________________________________________

from operation.forms import RegistrationForm

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        data={
            "form":form_instance
        }

        return render(request,"register.html",data) 
    
#_________________________________________________

from operation.forms import VehicleForm

class VehicleAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=VehicleForm()

        data={
            "form":form_instance
        }

        return render(request,"vehicle.html",data)
    
#___________________________________________________

from operation.forms import BmrForm

class BmrView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BmrForm()

        data={
            "form":form_instance
        }

        return render(request,"bmr.html",data)
    
#____________________________________________________

from operation.forms import AppointmentForm

class AppointmentView(View):

    def get(self,request,*args,**kwargs):

        form_instance=AppointmentForm()

        data={
            "form":form_instance
        }

        return render(request,"appoint.html",data)

#_________________________________________________________

from operation.forms import BmiForm

class BmiView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BmiForm

        context={
            "form":form_instance
        }

        return render(request,"bmi.html",context)
    
    def post(self,request,*args,**kwargs):

        #step1 :- extract from form_data

        form_data=request.POST

        #step2:- Initialize form with form_data

        form_instance=BmiForm(form_data)

        #step3:- check form is valid

        if form_instance.is_valid():

            data=form_instance.cleaned_data #{"height":165,"weight":65}

            height=data.get("height")

            weight=data.get("weight")

            BMI=weight/(height/100)**2

            print(BMI)

        return render(request,"bmi.html",{"form":form_instance,"result":BMI})
    
#____________________________________________________________

from operation.forms import MilageForm

class MilageView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MilageForm()

        context={
            "form":form_instance
        }

        return render(request,"milage.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=MilageForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            distance=data.get("distance")

            consumption=data.get("consumption")

            milage=distance/consumption

            print(milage)

        return render(request,"milage.html",{"form":form_instance,"result":milage})
    

#_____________________________________________________________________________

from operation.forms import EmiForm

class EmiView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmiForm

        context={
            "form":form_instance
        }

        return render(request,"emi.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=EmiForm(form_data)

        if form_instance.is_valid():

           data=form_instance.cleaned_data

           principal=data.get("principal")

           rate_of_interest=data.get("rate_of_interest")

           tenure=data.get("tenure")

           monthly_interest_rate=rate_of_interest/(12*100)

           emi=(principal * monthly_interest_rate * ((1+monthly_interest_rate)**tenure))

           emi=round(emi,2)

        return render(request,"emi.html",{"form":form_instance,"result":emi})
    
#___________________________________________________________________________________--

from operation.forms import CalorieForm

class CalorieView(View):

    def get(self,request,*args , **kwargs):

        form_intance=CalorieForm()

        context={
            "form":form_intance
        }

        return render(request,"calorie.html",context)

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=CalorieForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            #{'weight': 65, 'height': 166, 'age': 22,
            #  'gender': 'male', 'activity': '1.375'}  
            #           
            weight=data.get("weight")

            height = data.get("height")

            age = data.get("age")  

            gender=data.get("gender")     


            if gender=="male":
            
                bmr= 10*weight+6.25*height-5*age+5

            else:

                bmr= 10*weight+6.25*height-5*age-161
            
            print(bmr)

            activity= float(data.get("activity")) #activity in float

            calorie=bmr*activity

            print(calorie)
        
        return render(request,"calorie.html",{"form":form_instance,"BMR":bmr,"Calorie":calorie})