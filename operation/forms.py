from django import forms

class RegistrationForm(forms.Form):

    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-2"}))

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))

#_______________________________________________________

class VehicleForm(forms.Form):  

    name=forms.CharField()

    running_km=forms.IntegerField()

    OWNER_CHOICES=(
        ("first","first"),
        ("second","second"),
        ("third","third"),
    )

    owner_type=forms.ChoiceField(choices=OWNER_CHOICES)

    price=forms.IntegerField()

    FUEL_CHOICES=(
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("cng","cng"),
        ("electric","electric")
    )

    fuel_type=forms.ChoiceField(choices=FUEL_CHOICES)


#_______________________________________________

class BmrForm(forms.Form):

    weight=forms.IntegerField()

    height=forms.IntegerField()

    age=forms.IntegerField()

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=GENDER_CHOICES)

    ACTIVITY_CHOICES=(
        ("sedentary","sedentary"),
        ("little active","little active"),
        ("moderately active","moderately active"),
        ("very active","very active"),
        ("extra active","extra active")
    )

    activity_level=forms.ChoiceField(choices=ACTIVITY_CHOICES)

#___________________________________________________________

class AppointmentForm(forms.Form):

    first_name=forms.CharField()
    last_name=forms.CharField()

    contact_number=forms.IntegerField()
    email_addres=forms.EmailField()

    street_address=forms.CharField()
    street_address_line_2=forms.CharField()
    city=forms.CharField()
    state=forms.CharField()
    pincode=forms.IntegerField()

    date=forms.DateField()

#_________________________________________________________

class BmiForm(forms.Form):

    height=forms.IntegerField()
    weight=forms.IntegerField()

#________________________________________________________

class MilageForm(forms.Form):

    distance=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    consumption=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

#___________________________________________________________

class EmiForm(forms.Form):

    principal=forms.FloatField()
    tenure=forms.FloatField()
    rate_of_interest=forms.FloatField()

#__________________________________________________________

class CalorieForm(forms.Form):

    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    gender_choices=(
        ("male","MALE"),
        ("female","FEMALE")
    )

    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={"class":"form-control mb-3"}))

    activity_choices=(
        (1.2,"Sedentary"),
        (1.375,"lightly active"),
        (1.55,"moderatly active"),
        (1.725,"very active"),
        (1.9,"extra active")
    )

    activity=forms.ChoiceField(choices=activity_choices,widget=forms.Select(attrs={"class":"form-control mb-3"}))
              

    

