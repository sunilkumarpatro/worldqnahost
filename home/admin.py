from django.contrib import admin
from home.models import Qna,Comment,Related,Contact
from django.utils.html import format_html
# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
    search_fields = ['id']  # Add search filter input for multiple fields
    class Media:
        js = (
            'admin/js/jquery.init.js',  # Include jQuery if not already included
            'admin/js/comment_admin.js',  # Your custom JavaScript file
        )
admin.site.register(Comment, CommentModelAdmin)




class QnaModelAdmin(admin.ModelAdmin):
    search_fields = ['english_title_question']  # Add search filter input for multiple fields
    class Media:
        js = (
            'admin/js/jquery.init.js',  # Include jQuery if not already included
            'admin/js/qna_admin.js',  # Your custom JavaScript file
        )
admin.site.register(Qna, QnaModelAdmin)


class RelatedModelAdmin(admin.ModelAdmin):
     search_fields = [ 'qna_catagary__english_title_question']  # Add search filter input for multiple fields
     class Media:
        js = (
            'admin/js/jquery.init.js',  # Include jQuery if not already included
            'admin/js/related_admin.js',  # Your custom JavaScript file
        )
admin.site.register(Related, RelatedModelAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['email']  # Add search filter input for multiple fields

    class Media:
        js = (
            'admin/js/jquery.init.js',  # Include jQuery if not already included
            'admin/js/contact_admin.js',  # Your custom JavaScript file
        )

admin.site.register(Contact, ContactModelAdmin)

# admin.site.register(Comment)

