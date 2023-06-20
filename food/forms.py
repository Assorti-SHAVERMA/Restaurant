from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Textarea
from .models import Contact, Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name','email','phone','date','time','persons','message']
        widgets = {
            'full_name': TextInput(attrs={
                'name' : 'name',
                'class': 'form-control',
                'id' : 'name',
                "placeholder":"Your Name", 
                "data-rule":"minlen:4" ,
                "data-msg":"Please enter at least 4 chars",
            }),
            'email' : EmailInput(attrs={
                "class":"form-control", 
                "name":"email", 
                "id":"email", 
                "placeholder":"Your Email", 
                "data-rule":"email", 
                "data-msg":"Please enter a valid email"
            }),
            'phone': TextInput(attrs={
                "class":"form-control" ,
                "name":"phone" ,
                "id":"phone" ,
                "placeholder":"Your Phone", 
                "data-rule":"minlen:4" ,
                "data-msg":"Please enter at least 4 chars",
            }),
            "date": TextInput(attrs={
                "name":"date", 
                "class":"form-control", 
                "id":"date", 
                "placeholder":"Date", 
                "data-rule":"minlen:4",
                "data-msg":"Please enter at least 4 chars",
            }),
            "time": TextInput(attrs={
                "class":"form-control", 
                "name":"time", 
                "id":"time", 
                "placeholder":"Time", 
                "data-rule":"minlen:4",
                "data-msg":"Please enter at least 4 chars",
            }),
            "persons": NumberInput(attrs={
                "class":"form-control" ,
                "name":"people" ,
                "id":"people" ,
                "placeholder":"# of people" ,
                "data-rule":"minlen:1" ,
                "data-msg":"Please enter at least 1 chars",
            }),
            "message": Textarea(attrs={
                "class":"form-control" ,
                "name":"message" ,
                "rows":"5" ,
                "placeholder":"Message",
            })
}


class ContactForm(ModelForm):
    model = Contact
    fields = []







