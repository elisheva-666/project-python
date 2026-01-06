from django import forms
from .models import Profile,Task

class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        labels = {
            'team': 'Choose your team',
            'role': 'What is your role in the system?',
        }
        widgets = {
            'team': forms.Select(attrs={
                'class': 'bg-slate-800 border border-slate-700 text-white rounded-xl w-full p-4 focus:ring-2 focus:ring-purple-500 transition-all outline-none appearance-none'
            }),
            'role': forms.Select(attrs={
                'class': 'bg-slate-800 border border-slate-700 text-white rounded-xl w-full p-4 focus:ring-2 focus:ring-purple-500 transition-all outline-none appearance-none'
            }),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'date']
        widgets = {
            'name': forms.TextInput(attrs={})
        }
        help_texts = {
            "name": "Should contains only letters",
            "date":"in format YYYY-MM-DD"
        }

        def clean_name(self):
            name = self.cleaned_data["name"]
            if not name.isalpha():
                raise forms.ValidationError("Should contains only letters")
            return name




