from django.contrib import admin

from .models import (UserProfile, CaseWorker, CityLinkStatusSource, Client, ClientAddress, ClientCrime,
                     ClientFollowUp, ClientInterest, ClientInterview, ClientNote, ClientPlacement,
                     ClientSkill, ClientUpdate, Company, CompanyInterest, Crime, Job,  #InterviewType, causes errors...
                     JobSkill, Login, Neighborhood, PlacementOption, ReferralSource, Skill,
                     StaffingAgency, StateSource, StatusSource)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CaseWorker)
admin.site.register(CityLinkStatusSource)
admin.site.register(Client)
admin.site.register(ClientAddress)
admin.site.register(ClientCrime)
admin.site.register(ClientFollowUp)
admin.site.register(ClientInterest)
admin.site.register(ClientInterview)
admin.site.register(ClientNote)
admin.site.register(ClientPlacement)
admin.site.register(ClientSkill)
admin.site.register(ClientUpdate)
admin.site.register(Company)
admin.site.register(CompanyInterest)
admin.site.register(Crime)
# admin.site.register(Interviewtype) gonna have to look into what's wrong with it
admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(Login)
admin.site.register(Neighborhood)
admin.site.register(PlacementOption)
admin.site.register(ReferralSource)
admin.site.register(Skill)
admin.site.register(StaffingAgency)
admin.site.register(StateSource)
admin.site.register(StatusSource)
