from django import forms

# ACTIVITY_STYLE = (("a", "地理"), ("b", "化学"), ("c", "历史"), ('d', '生物'), ('e', '物理'), ('f', '政治'))
# class HobbiesForm(forms.Form):  
#     hobbies = forms.MultipleChoiceField(label='sa', choices=ACTIVITY_STYLE, widget=forms.CheckboxSelectMultiple())
#print(HobbiesForm(data={"hobbies": ["a", "b", "c"]}).as_p())
#print(HobbiesForm(data={"hobbies": ["b", "c"]}).as_p())

class PageHop(forms.Form):
    跳页 = forms.IntegerField(label='',required=True)
    # def clean(self):
    # 	page_num = self.cleaned_data['跳页']
    # 	if page_num < 1 :
    # 		raise forms.ValidationError("请输入合理的页数")
    # 	return self.cleaned_data
    # class Meta:
    # 	labels = {'text': ''}
    # 	field = {'length':2}
    # def save(self):
    #     if not self.跳页:
    #         return            

    #     super(PageHop, self).save()
        

