#! /usr/bin/python3

import subprocess
import smtplib
import socket
import sys
from email.mime.text import MIMEText

service = sys.argv[1]
hostname = socket.gethostname()
ip_address = "13.68.147.249"

def send_email():
 msg = MIMEText("Service %s is down!! \nCheck the service %s immediately on host %s!"%(service,service,hostname))
 msg["Subject"] = "SERVICE %s DOWN"%(service.upper())
 msg["From"] = "etashsingh29@gmail.com"
 msg["To"] = "etash.singh@knoldus.com"
 with smtplib.SMTP("smtp.gmail.com", 587) as server:
  server.ehlo()
  server.starttls()
  server.login("etashsingh29@gmail.com","wutifrrziksqsvbp")
  server.sendmail("etashsingh29@gmail.com","etash.singh@knoldus.com",msg.as_string())

def check_service():
 p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
 output = p.stdout.read().decode("utf-8")
 if "inactive" in output:
  send_email()

check_service()

