class SerializerActionMixin:
    def get_serializer_class(self):
        return getattr(
            self,
            f'serializer_class_{self.action}',
            self.serializer_class,
        )
