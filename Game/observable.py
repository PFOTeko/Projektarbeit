class Observable:

    def register_callback(self, fun):
        if not hasattr(self, 'callbacks'):
            self.callbacks = []
        if fun not in self.callbacks:
            self.callbacks.append(fun)

    def remove_callback(self, fun):
        if hasattr(self, 'callbacks') and fun in self.callbacks:
            self.callbacks.remove(fun)

    def remove_callbacks(self):
        if hasattr(self, 'callbacks'):
            self.callbacks.clear()

    def _notify(self, event_type, data=None):
        for f in getattr(self, 'callbacks', []):
            f(event_type, data)