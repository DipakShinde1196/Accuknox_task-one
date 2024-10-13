"""By default, Django signals are executed synchronously. When a signal is sent, the connected receivers are invoked synchronously, and the signal sender waits until the receivers finish processing before continuing execution."""


from django.dispatch import Signal, receiver
import time

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(3)  # Simulating a 3-second delay
    print("Receiver finished")
