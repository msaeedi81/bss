from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]

    actions = ["export_as_csv", "export_as_csv_and_send_telegram", "export_by_date_to_telegram"]
    model = None
    not_displayed_fields = []
    export_fields = ()

    def get_list_display(self, request):
        if self.model is not None:
            base_fields = ['created', 'updated']
            list_unsorted = [field.name for field in self.model._meta.fields if field.name not in base_fields + self.not_displayed_fields]
            displayable_base_fields = [field for field in base_fields if field not in self.not_displayed_fields]
            [list_unsorted.append(field) for field in displayable_base_fields]
            return list_unsorted
        else:
            return super().get_list_display(request)
