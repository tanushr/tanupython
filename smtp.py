# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("tanushreenagaraj@gmail.com", "mummy510") 
  
# message to be sent 
message = "hii"
  
# sending the mail 
s.sendmail("tanushreenagaraj@gmail.com","rakbops@gmail.com", message) 
  
# terminating the session 
s.quit() 
