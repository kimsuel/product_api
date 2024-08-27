class MappingViewSetMixin(object):
    serializer_action_map = {}

    def get_serializer_class(self):
        if self.serializer_action_map.get(self.action, None):
            return self.serializer_action_map.get(self.action)
        return self.serializer_class
