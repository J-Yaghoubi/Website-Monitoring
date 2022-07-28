

from time import sleep
import requests, smtplib, logging


class StartMonitoring:

    def __init__(self, config) -> None:

        self.interval = config['interval']
        self.target = config['target']
        self.sender_email = config['sender_email']
        self.sender_pass = config['sender_pass']
        self.receiver_email = config['receiver_email']
        self.email_subject = config['email_subject']
        self.email_massage = config;['email_massage']
        self.host = config['host']
        self.port = config['port']                                

        self._enable_logging()
        self.job()
        
    def job(self):
        self._send_email() if self._check_status() != 200 else self._recursive()

    def _recursive(self):
        sleep(self.interval)
        return self.job()

    def _enable_logging(self) -> None:
        fm = "%(asctime)s (%(name)s) %(levelname)-12s: %(message)s"
        logging.basicConfig(filename='log.txt', filemode='a', format=fm, level=logging.DEBUG)
        logging.info('Job Has been started')
              
    def _check_status(self):
        r = requests.get(self.target)
        return r.status_code

    def _send_email(self):

        logging.warning('Problem in connection')
        
        with smtplib.SMTP(self.host, self.port) as smtp:
            smtp.helo()
            smtp.starttls()
            smtp.helo()

            smtp.login(self.sender_email, self.sender_pass)

            msg = f'Subject: {self.email_subject}\n\n{self.email_massage}'
            smtp.sendmail(self.sender_email, self.receiver_email, msg)

        logging.info('Sended alert to destination')

        # Recursive Mode
        return self._recursive()   


if __name__ == "__main__":

    config = {
        # check time in second 
        # the website that we want to monitor it 
        # your email address
        # your email password  
        # receiver email 
        
        'interval'      : 5,                                  
        'target'        : 'http://google.com',       
        'sender_email'  : 'Email_Address',       
        'sender_pass'   : 'Email_Password',         
        'receiver_email': 'Destination Email',   

        # email service host and port
        'host' : 'smtp.gmail.com',                      
        'port' : 578,                          

        # sended email subject and massage
        'email_subject' : 'Target is done...',      
        'email_massage' : 'Please check the functionality of it',        
    }


    StartMonitoring(config)



