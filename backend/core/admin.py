from django.contrib import admin
from .models import (
    User, Profile, UserSetting, Checkup, CheckupFile,
    InspectionItem, CheckupDetail, AiAnalysis, AiConsultationQuestion,
    DiseaseCode, Medication, CheckupDiseaseRel, CheckupMedicationRel, ProfileMedication
)

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(UserSetting)
admin.site.register(Checkup)
admin.site.register(CheckupFile)
admin.site.register(InspectionItem)
admin.site.register(CheckupDetail)
admin.site.register(AiAnalysis)
admin.site.register(AiConsultationQuestion)
admin.site.register(DiseaseCode)
admin.site.register(Medication)
admin.site.register(CheckupDiseaseRel)
admin.site.register(CheckupMedicationRel)
admin.site.register(ProfileMedication)