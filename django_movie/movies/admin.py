from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(
        label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_desription = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 row was updated"
        else:
            message_bit = f"{row_update} rows was updated"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 row was updated"
        else:
            message_bit = f"{row_update} rows was updated"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    unpublish.short_description = "Снять с публикации"

    publish.allowed_permissions = ('change', )
    unpublish.allowed_permissions = ('change', )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_desription = "Image"


#admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(MovieShots)
# admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Reviews)


admin.site.site_title = "My Movies"
admin.site.site_header = "My Movies"
