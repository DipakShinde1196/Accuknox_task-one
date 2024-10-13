Question 1: By default, are Django signals executed synchronously or asynchronously?
Answer: 
By default, Django signals are executed synchronously. When a signal is sent, the connected receivers are invoked synchronously, and the signal sender waits until the receivers finish processing before continuing execution.
