from django.forms import ModelChoiceField

class MyChoiceModelField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.Info