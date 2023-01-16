class Subject:
    observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        pass

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)
