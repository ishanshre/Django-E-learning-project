from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveSmallIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                query_all = self.model.objects.all()
                if self.for_fields:
                    query = {
                        field: getattr(model_instance, field) for field in self.for_fields
                    }
                    query_all = query_all.filter(**query)
                last_item = query_all.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)