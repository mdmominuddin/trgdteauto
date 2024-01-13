from django.contrib import admin
from .models import Svcs, Sections, Participants, Country, Evcats, GovtOrder, Events, VacancyDistribution, CourseOffer

@admin.register(Svcs)
class SvcsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('Service_Number', 'Rank', 'name', 'svc')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_class')

@admin.register(Evcats)
class EvcatsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GovtOrder)
class GovtOrderAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'go_number', 'go_pub_date', 'start_date', 'end_date', 'get_days_involved')

    def get_days_involved(self, obj):
        return obj.days_involved

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_category', 'institute_name', 'start_date', 'end_date', 'country', 'get_duration')

    def get_duration(self, obj):
        return obj.duration

    get_duration.short_description = 'Duration'

@admin.register(VacancyDistribution)
class VacancyDistributionAdmin(admin.ModelAdmin):
    list_display = ('course_offer', 'svc', 'vacancies_allocated')

@admin.register(CourseOffer)
class CourseOfferAdmin(admin.ModelAdmin):
    list_display = ('ff_country', 'event_name', 'vac_offered', 'vac_accepted', 'vac_regretted', 'financial')
