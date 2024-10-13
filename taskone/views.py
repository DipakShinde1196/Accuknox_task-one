# views.py
import time
from django.http import HttpResponse
from .signals import my_signal

def trigger_signal(request):
    print("Signal sending started")
    start_time = time.time()

    # Send the signal
    my_signal.send(sender=None)

    # Execution time after signal handling
    end_time = time.time()
    duration = end_time - start_time
    print(f"Signal sending finished. Duration: {duration:.2f} seconds")

    return HttpResponse(f"Signal processing took {duration:.2f} seconds")
