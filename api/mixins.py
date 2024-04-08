from rest_framework.generics import get_object_or_404


class MultipleFieldLookupMixin:
    '''
    Apply this mixin to a view  to allow for multiple fields to be used in the lookup for the object.
    '''
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):              # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter) # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
