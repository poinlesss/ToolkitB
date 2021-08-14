import time
import os.path

i = 0
time_to_wait = 180
found = False

while i <= time_to_wait:
    invoice_file_status = ""
    cert_file_status = ""
    invoice_file_status = os.path.exists("/Users/me/Desktop/aaa.png")
    cert_file_status = os.path.exists("/Users/me/Desktop/bbb.png")

    if invoice_file_status == True:
        if cert_file_status == True:
            print("I'm done.")
            found = True
            i = time_to_wait

    i = i + 1
    time.sleep(1)

    if i > time_to_wait and found == False:
        print("I'm giving up")




