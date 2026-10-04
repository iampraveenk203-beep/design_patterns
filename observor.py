"""
Observor: Behavioural design pattern, when one object watches the other object for state changes and reacts immediatly when notified.
Also called as publisher-subscriber pattern.
"""
# Subscribers
class NotificationObservor:
    def update(self, msg: str):
        raise NotImplementedError("Subclass must implement the update method")

class EmailAlert(NotificationObservor):
    def update(self, msg: str):
        return "Sending Email Alert."
    
class SmsAlert(NotificationObservor):
    def update(self, msg: str):
        return "Sending SMS Alert."

#Publishers
class Publisher:
    def __init__(self):
        self._observers = []
        self._status = 'Healthy'
    
    def register(self, observor):
        if observor not in self._observers:
            self._observers.append(observor)
            print(f"Registered: {observor.__class__.__name__}")
    def deregister(self, observor):
        if observor in self._observers:
            self._observers.remove(observor)
            print(f"Deregistered: {observor.__class__.__name__}")
    
    def simulate_event(self, new_status: str, msg: str):
        print(f"[Server Alert] Status changed to {new_status}")
        self._status = new_status
        self._notify_all(msg)
    
    def _notify_all(self, msg: str):
        for observor in self._observers:
            print(observor.update(msg))

email = EmailAlert()
sms = SmsAlert()
publisher = Publisher()
publisher.register(email)
publisher.register(sms)
publisher.simulate_event("Healthy", "Back to form")


