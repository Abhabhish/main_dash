from django import forms
from .models import RecordingDetail


class RecordingDetailForm(forms.ModelForm):
    class Meta:
        model = RecordingDetail
        fields = [
                    "workpackage",
                    "workpackagetype",
                    "date",
                    "name",
                    "ethnicity",
                    "gender",
                    "age",
                    "height",
                    "beard",
                    "hair",
                    "eyecolour",
                    "clothingaccessories",
                    "glasses",
                    "makeup",
                    "action",
                    "carnumber",
                    "carstatus",
                    "recordingstatus"
                    ]
        labels = {  
            "workpackage" : "Work Package Group",
            "workpackagetype" : "Work Package Type",
            "clothingaccessories" : "Clothing Accessories",
            "carnumber" : "Car Number",
            "carstatus" : "Car Status",
            "recordingstatus" : "Recording Status"
            }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        required = {
            'beard': False,
            'carnumber': False,
            'carstatus': False,
            'action': False,
            'clothingaccessories': False,
            'glasses': False,
            'makeup': False,
            'recordingstatus': False,
        }

    def __init__(self, *args, **kwargs):
        super(RecordingDetailForm, self).__init__(*args, **kwargs)
        # Explicitly set required to False for specified fields
        self.fields['beard'].required = False
        self.fields['carnumber'].required = False
        self.fields['carstatus'].required = False
        self.fields['action'].required = False
        self.fields['clothingaccessories'].required = False
        self.fields['glasses'].required = False
        self.fields['makeup'].required = False
        self.fields['recordingstatus'].required = False
        