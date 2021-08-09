from django.contrib import admin
from app.models import PatientRecords, MedicalHistory, TreatmentInfo
# Register your models here.


@admin.register(PatientRecords)
class PatientRecordsAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    # date_hierarchy = 'created_at'

    exclude = ('attending',)

    list_display = ('id', 'name', 'age','gender', 'attending', 'health_status')

    list_display_links = ('name',)

    # 激活过滤器，这个很有用
    list_filter = ('created_at', 'age', )

    list_per_page = 50  # 控制每页显示的对象数量，默认是100
    filter_horizontal = ('treatment_info', 'medical_history',)  

    def save_model(self, request, obj, form, change):
     
        obj.attending = request.user
        obj.save()
    # 限制用户权限，只能看到自己编辑的文章
    # def get_queryset(self, request):
    #     qs = super(PatientRecordsAdmin, self).get_queryset(request)
    #     if request.user.has_perm('view_medical_history',):
    #         return qs
    #     return qs.filter(author=request.user)
    
@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    # date_hierarchy = 'created_at'

    exclude = ('author',)

    list_display = ('id', 'title', 'content', 'desc', 'created_at',)

    # list_display_links = ('name',)

    # 激活过滤器，这个很有用
    list_filter = ('title',)

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
        
    # 限制用户权限，只能看到自己编辑的文章
    # def get_queryset(self, request):
    #     qs = super(PatientRecordsAdmin, self).get_queryset(request)
    #     if request.user.has_perm('view_medical_history',):
    #         return qs
    #     return qs.filter(author=request.user)
    
@admin.register(TreatmentInfo)
class TreatmentInfoAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    # date_hierarchy = 'created_at'

    exclude = ('author',)

    list_display = ('id', 'title', 'content', 'desc', 'created_at',)

    # list_display_links = ('name',)

    # 激活过滤器，这个很有用
    list_filter = ('title',)

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()