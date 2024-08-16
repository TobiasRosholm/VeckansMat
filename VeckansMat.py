# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:59:52 2024

@author: Tobia
"""

import random as rnd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Mon = {
       "Krämig pasta med halloumi och tomat" : ["4  port pasta", "150 g haricots verts (bönor)", "2  vitlöksklyftor", "2  tomater", "400 g halloumi", "2 dl crème fraiche", "1 tsk torkad persilja", "1 tsk torkad basilika", "65 g babyspenat"],
       "Vegetarisk lasange" : ["2 st gul lök", "4 dl röda linser", "8 dl krossade tomater", "6 dl vatten", "4 st morötter", "2 buljongtärningar", "2 msk tomatpiré", "2 vitlöksklyftor", "5 dl creme fraishe", "2 dl riven ost", "500 g lasange plattor", "2 dl osttopping"],
       "Kyckling pasta" : ["700 g Kyckling", "4 port pasta", "2 dl creme fraiche", "Körsbärstomater", "Riven ost"],
       "Lax pasta" : ["2 bitar lax", "Pasta", "2 dl creme fraiche", "Körsbärstomater", "Spenat"],
       "Pasta med tomatsås" : ["2 pkt Krossad tomat", "Grönsaksbuljong", "Tomatpuré", "1 Morot", "1 gul lök", "1 vitlöksklyfta"]
       }

Tue = {
       "Lax med potatis" : ["2 lax bitar", "500 g potatis", "sparris eller broccoli", "valfri passande sås"],
       "Fiskpinnar" : ["1 paket fisk pinnar", "Valfri grönsak", "ris, pasta eller potatis"],
       "Torskgryta" : ["1 paket torsk", "Basmatiris", "400 ml kokosmjölk", "2 vitlöksklyfta", "400 g paket wookade grönsaker", "2 buljongtärningar"]
       }

Wed = {
       "Kycklinggryta röd curry" : ["700 g Kyckling", "Röd curry krydda", "Basmatiris", "0,5 paket jordnötter", "5 dl creme fraiche", "400 g paket wookade grönsaker"],
       "Kycklinggryta gul curry" : ["700 g Kyckling", "Gul curry krydda", "Basmatiris", "1 gul lök", "300 g potatis", "5 dl creme fraiche", "400 g paket wookade grönsaker"],
       "Kyckling i ugn" : ["700 g Kyckling", "500 g potatis", "Bearnise sås", "Spenat", "Broccoli"]
       }

Thu = {
       "Potatissoppa" : ["500g potatis","1 Purjolök", "2 buljongtärningar", "8 dl vatten", "3 dl Matlagningsgrädde", "1 paket vitlöksbröd", "2 vitlöksklyftor"],
       "Tomatsoppa" : ["4 Tomater", "1 Gul lök", "500 g krossade tomater", "2 msk tomatpure", "1 buljongtärningar", "5 dl vatten", "3 dl Matlagningsgrädde"],
       "Broccolisoppa" : ["250 g broccoli", "1 Gul lök", "300 g potatisar", "2 buljongtärningar", "8 dl vatten","3 dl Matlagningsgrädde", "1 paket vitlöksbröd"]
       }

Fri = {
       "Taco" : ["500 g Sojafärs", "2 Tomater", "1 Romansallad", "1 paket taco krydda", "1 paket burritobröd", "Valfria grönsaker"],
       "Vegetarisk tacopaj" : ["500 g Sojafärs", "1 paket taco krydda", "2 dl creme fraishe", "1 röd paprika", "1 röd chilli", "1 pajdeg", "300 g riven ost", "1 tomat"],
       "Enchilatas" : ["200 g riven ost", "burrito bröd", "500 g Sojafärs", "1 paket taco krydda", "2 dl creme fraishe", "1 röd paprika", "1 röd chilli", "majs"],
       "Hallumiburgare" : ["500 g potatis", "1 halloumi", "sallad", "1 tomat", "hamburgardressing", "rostad lök", "hamburgarbröd"]
       }

Sat = {
       "Burgare" : ["ÄTA UTE!"],
       "Burrito" : ["ÄTA UTE!"],
       "Sushi" : ["ÄTA UTE!"],
       "Italienskt" : ["ÄTA UTE!"],
       "Falafel" : ["ÄTA UTE!"],
       "Thai" : ["ÄTA UTE!"],
       "Indiskt" : ["ÄTA UTE!"],
       "Spoonery" : ["ÄTA UTE!"]
       }

Sun = {
       "Linsgryta i kokosmjölk" : ["Basmatiris", "1 Gul lök", "1 vitlöksklyfta" , "1 tsk curry", "2 msk tomatpure", "400 ml kokoasmjölk", "2,5 dl vatten", "1 buljongtärningar", "2 dl torkade röda linser", "1 tsk sambal oelek", "250 g körsbärstomater" ],
       "Halloumistroganoff" : ["1  gul lök", "1  vitlöksklyfta", "1  röd paprika", "400 g halloumi", "1 msk tomatpuré", "2 tsk torkad oregano", "1 tsk paprikapulver", "1  förp passerade tomater", "1 dl vispgrädde", "1/2 dl vatten"],
       "Palak paneer med tomat och halloumi" : ["Basmatiris", "1  gul lök", "2  vitlöksklyftor", "2  tomater", "2 msk riven ingefära", "3 msk olivolja", "2 msk tomatpuré", "1 msk garam masala", "390 g krossade tomater", "1 dl vatten", "2 dl vispgrädde", "1 buljongtärning", "200 g färsk spenat", "400 g halloumi"],
       "Risoni och färskost" : ["2 dl risoni", "200 g färskost", "60 g soltorkadetomater", "10 st körsbärstomater", "2 nävar spenat", "1 vitlöksklyfta", "5 dl grönsaksbuljong", "1 dl riven ost", "Oregano"],
       "Paj med feta och tomater" : ["1 förp pajdeg", "4 ägg", "2 dl grädde", "2 dl riven ost", "150 g fetaost", "8 soltorkade tomater", "65 g spenat", "0,5 förp pinjenötter"]
       }

ValMon = rnd.choice(list(Mon.items()))
ValTue = rnd.choice(list(Tue.items()))
ValWed = rnd.choice(list(Wed.items()))
ValThu = rnd.choice(list(Thu.items()))
ValFri = rnd.choice(list(Fri.items()))
ValSat = rnd.choice(list(Sat.items()))
ValSun = rnd.choice(list(Sun.items()))
   
with open(r'VeckansMat.txt', 'r') as Ftxt:
        # read all content from a file using read()
        content = Ftxt.read()
        # check if string present or not
        while ValMon[0] in content:
            ValMon = rnd.choice(list(Mon.items()))
        while ValTue[0] in content:
            ValTue = rnd.choice(list(Tue.items()))
        while ValWed[0] in content:
            ValWed = rnd.choice(list(Wed.items()))
        while ValThu[0] in content:
            ValThu = rnd.choice(list(Thu.items()))
        while ValFri[0] in content:
            ValFri = rnd.choice(list(Fri.items()))
        while ValSat[0] in content:
            ValSat = rnd.choice(list(Sat.items()))
        while ValSun[0] in content:
            ValSun = rnd.choice(list(Sun.items()))

print(content)



with open("VeckansMat.txt", "w") as f:
    f.write(str(ValMon[0]) + "\n")
    f.write(str(ValTue[0]) + "\n")
    f.write(str(ValWed[0]) + "\n")
    f.write(str(ValThu[0]) + "\n")
    f.write(str(ValFri[0]) + "\n")
    f.write(str(ValSat[0]) + "\n")
    f.write(str(ValSun[0]) + "\n")



VeckansMat = str([ValMon[0], ValTue[0], ValWed[0], ValThu[0], ValFri[0], ValSat[0], ValSun[0]])
VeckansMatVaror = str([ValMon[1], ValTue[1], ValWed[1], ValThu[1], ValFri[1], ValSat[1], ValSun[1]])

def send_email(sender_email: str, password: str, receiver_email: str, subject: str, body: str) -> None:
    """Send an email using Gmail."""
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
    finally:
        server.quit()
def read_credentials(filename: str) -> tuple:
    """Read email and password from a text file."""
    with open(filename, "r") as file:
        email = file.readline().strip()
        password = file.readline().strip()
    return email, password
if __name__ == "__main__":
    # Specify the filename where email and password are stored
    filename = "credentials.txt"
    # Read email and password from the file
    sender_email, password = read_credentials(filename)
    receiver_email = "<email>"
    subject = VeckansMat.replace(", ", "---")
    subject = subject.replace("[", " ")
    subject = subject.replace("]", " ")
    subject = subject.replace("'", " ")         
    body = VeckansMatVaror.replace(", ", "\n")
    body = body.replace("]\n[", "\n\n")
    body = body.replace("[[", "")
    body = body.replace("]]", "")
    body = body.replace("'", "")    
send_email(sender_email=sender_email, password=password, receiver_email=receiver_email, subject=subject, body=body)

#print(subject)
#print(body)
