from django import forms
from .models import Svcs, Sections, Participants, Country, Evcats, GovtOrder, Events, VacancyDistribution, CourseOffer

class SvcsForm(forms.ModelForm):
    class Meta:
        model = Svcs
        fields = '__all__'

class SectionsForm(forms.ModelForm):
    class Meta:
        model = Sections
        fields = '__all__'


class ParticipantsForm(forms.ModelForm):
    govt_order = forms.ModelChoiceField(queryset=GovtOrder.objects.all(), empty_label=None)

    class Meta:
        model = Participants
        fields = '__all__'
        labels = {
            'Service_Number': 'Service Number',
            'Rank': 'Rank',
            'name': 'Name',
            'svc': 'Service',
            'govt_order': 'Govt Order',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Service_Number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'e.g., BA-xxxx',
        })

        self.fields['Rank'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['svc'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['govt_order'].queryset = GovtOrder.objects.all()


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class EvcatsForm(forms.ModelForm):
    class Meta:
        model = Evcats
        fields = '__all__'

class GovtOrderForm(forms.ModelForm):
    class Meta:
        model = GovtOrder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['event_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Event Name',
        })

        self.fields['go_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Govt Order Number',
        })

        self.fields['go_pub_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Select Govt Order Publication Date',
            'type': 'date',
        })

        self.fields['start_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Select Start Date',
            'type': 'date',
        })

        self.fields['end_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Select End Date',
            'type': 'date',
        })

        self.fields['days_involved'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Automatically Calculated',
            'readonly': True,
        })

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class VacancyDistributionForm(forms.ModelForm):
    class Meta:
        model = VacancyDistribution
        fields = '__all__'

class CourseOfferForm(forms.ModelForm):
    class Meta:
        model = CourseOffer
        fields = '__all__'
