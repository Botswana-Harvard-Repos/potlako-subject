from django.contrib import admin

from ..admin_site import potlako_subject_admin
from ..forms import PatientCallFollowUpForm
from ..models import PatientCallFollowUp


@admin.register(PatientCallFollowUp, site=potlako_subject_admin)
class PatientCallFollowUpAdmin(admin.ModelAdmin):

    form = PatientCallFollowUpForm

    fieldsets = (
        (None, {
            'fields': ('visit_date_time',
                       'facility_visited',
                       'call_clinician',
                       'call_clinician_type',
                       'facility_unit',
                       'facility_unit_other',
                       'visit_type',
                       'perfomance_status',
                       'pain_score',
                       'general_comments',
                       'patient_disposition',
                       'referral_date',
                       'referral_facility',
                       'referral_reason',
                       'referral_discussed',
                       'referral_discussed_clinician',
                       'return_visit_scheduled',
                       'return_visit_date',
                       'investigation_ordered',
                       'triage_status',
                       'transport_support'
                       )
        }),
    )

    radio_fields = {'facility_visited': admin.VERTICAL,
                    'call_clinician_type': admin.VERTICAL,
                    'facility_unit': admin.VERTICAL,
                    'visit_type': admin.VERTICAL,
                    'patient_disposition': admin.VERTICAL,
                    'referral_facility': admin.VERTICAL,
                    'referral_discussed': admin.VERTICAL,
                    'return_visit_scheduled': admin.VERTICAL,
                    'investigation_ordered': admin.VERTICAL,
                    'triage_status': admin.VERTICAL,
                    'transport_support': admin.VERTICAL,
                    }
