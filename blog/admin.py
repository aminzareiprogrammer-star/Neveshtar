from django.contrib import admin

from blog.models import Article, Category,Comment,Message,Like,LikeComment

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','status','show_image')
    search_fields = ('title',)
    inlines = (CommentInline,)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','article', 'user', 'parent')

admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(LikeComment)

