from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    # tags관련 레코드 가져오기 (다대다 관계) -> 오버라이딩
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    # obj의 모든 태그명을 , 로 연결해 태그 리스트 보여주기
    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())