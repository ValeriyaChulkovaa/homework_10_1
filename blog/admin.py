from django.contrib import admin, messages


from blog.models import Blog


@admin.action(description='Удалить выбранные посты')
def delete_selected_posts(modeladmin, request, queryset):
    # Ваш код для удаления
    deleted_count, _ = queryset.delete()
    messages.success(request, f'Успешно удалено {deleted_count} постов.')

@admin.action(description='Опубликовать выбранные посты')
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description='Снять публикацию с выбранных постов')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'is_published')
    search_fields = ('title', 'is_published')
    actions = [make_published, make_unpublished, delete_selected_posts]
