#//////////////////////////////////////////////////////////////////////////
#                      Website Monitoring Script                          #
#                                                                         #
#         Publish date  28-JUL-2022                                       #
#         Version  1.0.0                                                  #
#         By  Seyed Jafar Yaghoubi                                        #
#         License  MIT                                                    #
#         More info https://github.com/J-Yaghoubi/                        #
#         Contact  algo3xp3rt@gmail.com                                   #
#                                                                         #
#//////////////////////////////////////////////////////////////////////////

import logging
import requests, smtplib
from time import sleep

class Monitoring:
    """ Gets a website address and monitors its stability 
        by checking the status repeatedly. If found the problem 
        then sends an Email to the selected address

        Parameters
        ----------
        config : dict
            all data it need to do his job

    """

    def __init__(self, config: dict) -> None:

        self.interval = config['interval']
        self.target = config['target']
        self.sender_email = config['sender_email']
        self.sender_pass = config['sender_pass']
        self.receiver_email = config['receiver_email']
        self.email_subject = config['email_subject']
        self.email_massage = config;['email_massage']
        self.host = config['host']
        self.port = config['port'] 
        self.looping = config['looping']                               

        print('The program is ready and does its job...')

        self._enable_logging()
        self.job()

    def job(self) -> None:
        """Check the status, send email if there is problem, otherwise repeat this functionality"""
        self._send_email() if self._check_status() != 200 else self._recursive()

    def _recursive(self):
        """Protected method that provide looping"""

        sleep(self.interval)
        self.job()

    def _enable_logging(self) -> None:
        """Protected method for setup and enabling the logging"""

        fm = "%(asctime)s (%(name)s) %(levelname)-12s: %(message)s"
        logging.basicConfig(filename='log.txt', filemode='a', format=fm, level=logging.INFO)
        logging.info('Job Has been started')
              
    def _check_status(self) -> int:
        """Protected method to check the status"""

        r = requests.get(self.target)
        return r.status_code

    def _send_email(self):
        """Protected method for sending email"""

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
        return self._recursive() if self.looping else None   

    @staticmethod
    def start(config: dict) -> None:
        """starts the script and log on exit"""

        try:
            Monitoring(config)
        except:
            logging.warning('Job has been stopped') 
            print('The script has been stopped...')  


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
        'email_subject' : 'Target is out of range!',      
        'email_massage' : 'Please check the functionality of your site', 

        # stop when find a problem or do looping(repeatedly checking and emailing)  
        'looping' : False,    
    }

    Monitoring.start(config)




