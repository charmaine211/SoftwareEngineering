"""
Admin module, a dashboard for the site admins.
This dashboard provides all helpdesk functionality.

Only registered users with role 'superuser' can login to this area.
This area is available at http://127.0.0.1/admin
"""

from django.contrib import admin
from .models import Keys, Platform, Signatures

class KeysAdmin(admin.ModelAdmin):
    """
    Custom class for the Keys Admin Area.
    This class hides the actual key-field to prevent it from modifications.

    Args:
        admin.ModelsAdmin

    Returns:
        The new admin class.
    """
    fieldsets = (

        (None, {
            'fields': ('role', 'platform_used', 'owner'),
            'description': 'Let op, om fouten te voorkomen kan de key hier niet gewijzigd worden.'
        }),

    )

admin.site.register(Platform)
admin.site.register(Keys, KeysAdmin)
admin.site.register(Signatures)