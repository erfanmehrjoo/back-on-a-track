import smtplib
import email.message
import re
from app2 import password   

def read_email_from_txt(file_path):
  """Reads the email from the given text file.

  Args:
    file_path: The path to the text file.

  Returns:
    A string containing the email.
  """

  with open(file_path, "r") as f:
    email_content = f.read()

  return email_content

def send_email_to_multiple_addresses(email_content, to_addrs):
  """Sends the given email to the given list of email addresses.

  Args:
    email_content: The content of the email.
    to_addrs: A list of email addresses to send the email to.
  """

  msg = email.message.EmailMessage()
  msg["To"] = ",".join(to_addrs)
  msg["Subject"] = "Email from Python app"
  msg.set_content(email_content)

  smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
  smtp_server.starttls()
  smtp_server.login("e.mehrjoo.e@gmail.com", password)
  smtp_server.send_message(msg)
  smtp_server.quit()
  
  
def main():
  """Reads the email from the text file, extracts the email addresses, and sends the email to all of the extracted email addresses."""

  # Get the path to the text file.
  file_path = "email.txt"

  # Read the email from the text file.
  email_content = read_email_from_txt(file_path)

  # Extract the email addresses from the email content.
  email_addresses = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_content)

  # Send the email to all of the extracted email addresses.
  send_email_to_multiple_addresses(email_content, email_addresses)

if __name__ == "__main__":
  main()