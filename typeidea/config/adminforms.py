# -*- coding: utf-8 -*-

from django import forms


class SideBarAdminForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea, label='内容',
                              required=False, help_text="如果设置的不是HTML类型的话，可为空")

    def clean(self):
        display_type = self.cleaned_data.get('display_type')
        content = self.cleaned_data.get('content')
        if display_type == 1 and not content:
            raise forms.ValidationError("当展示类型为HTML时，内容不能为空")
        return self.cleaned_data
