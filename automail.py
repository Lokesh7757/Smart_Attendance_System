import yagmail
import os

receiver = "mygmail@gmail.com"  # receiver email address
body = "Attendance File"  # email body
filename = "Attendance" + os.sep + "Attendance_2020-08-29_17-05-04.csv"  # file path

# Directly pass your email credentials here (Not recommended for production)
email = "lokeshk7757@gmail.com"
password = "Lokesh@60"

yag = yagmail.SMTP(email, password)

yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=filename,
)
