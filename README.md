# Service Status Alert with Email Notification
--------------------------------------------------

When will the alert be generated
-------------------------------------------------
* If the service with name provided to the script is in inactive state


How Script Works:
----------------------------------------------------
* Get the service name from command line argument
* Check the state of the service
* If service is in active state, do nothing
* If service is in inactive state, send email with provided configurations

How to Run:
----------------------------------------------------

./service_monitor_alert.py {Service name}

For Example:
service_monitor_alert.py rsync

