from django import forms
from .models import RecordingDetail


class RecordingDetailForm(forms.ModelForm):
    class Meta:
        model = RecordingDetail
        fields = [
                    "name",
                    "ethnicity",
                    "age",
                    "gender",
                    "date",
                    "height",
                    "beard",
                    "hair",
                    "eyecolour",
                    "workpackage",
                    "workpackagetype",
                    "carnumber",
                    "carstatus",
                    "action",
                    "clothingaccessories",
                    "glasses",
                    "makeup",
                    "recordingstatus"
                    ]
        